#!/usr/bin/env python3
"""「公開完了 + URL」後のローカル処理を1回にまとめるオーケストレーションスクリプト。

前提: SNS投稿文(social/article-XX-promotions.md)はClaude Codeが
このスクリプトの実行前に作成済みであること。投稿文そのものの生成は行わない。

安全設計: すべてのpreflightチェック(読み取りのみ)を先に完了し、
1件でもFAILした場合はファイルへの書き込みを一切行わずに中断する。
書き込み(topics.csv更新・draft移動・promotions.csv登録)は、
preflightがすべて通過した後にのみ行う。

行うこと(preflight):
  - article_id/URL形式の検証
  - draft候補の特定(1件のみ許可)
  - topics.csvの対象行/article_id一致の検証
  - SNS宣伝ファイルの存在・パース(X5+Threads5・重複や不足がないか)
  - promotions.csvの既存行が今回の登録内容と矛盾しないか
  - git statusに、今回想定している新規ファイル(draft・SNS宣伝ファイル)以外の
    変更・削除・staged済みファイルがないか

行うこと(preflight通過後の書き込み):
  - topics.csvへの登録/更新
  - draft -> published への移動
  - promotions.csvへの10件登録
  - verify_article_workflow.py による検証
  - 問題なければ git_safe_sync.py で add -> commit -> push

途中で条件を満たさない場合はその時点で中断し、状態をそのまま報告する
(自動ロールバックは行わない)。preflight通過後の書き込み段階でも、
各ステップ自体が失敗した場合はそこで中断する。

Usage:
    python3 scripts/complete_publish.py <article_id> <note_url>
"""

import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify_article_workflow as vaw  # noqa: E402
import git_safe_sync as gss  # noqa: E402
import manage_topics as mt  # noqa: E402
import manage_promotions as mp  # noqa: E402

ROOT = vaw.ROOT
DRAFT_DIR = vaw.DRAFT_DIR
PUBLISHED_DIR = vaw.PUBLISHED_DIR
SOCIAL_DIR = vaw.SOCIAL_DIR

URL_RE = re.compile(r"^https://note\.com/[^\[\]()]+$")


def parse_front_matter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, None, None

    def get(key):
        mm = re.search(rf'^{key}:\s*"?([^"\n]*)"?\s*$', m.group(1), re.M)
        return mm.group(1).strip() if mm else None

    return get("title"), get("keyword"), get("category")


def parse_promotions_md(text):
    entries = []

    def parse_section(section_text, platform):
        items = []
        blocks = re.split(r"^### \d+\.\s*(.+)$", section_text, flags=re.M)
        for i in range(1, len(blocks), 2):
            post_type = blocks[i].strip()
            body = blocks[i + 1] if i + 1 < len(blocks) else ""
            timing_m = re.search(r"おすすめ投稿タイミング:\s*(.+)", body)
            timing = timing_m.group(1).strip() if timing_m else "随時"
            items.append((platform, post_type, timing))
        return items

    x_match = re.search(r"^## X\n(.*?)(?=^## Threads|\Z)", text, re.S | re.M)
    th_match = re.search(r"^## Threads\n(.*?)\Z", text, re.S | re.M)
    if x_match:
        entries += parse_section(x_match.group(1), "x")
    if th_match:
        entries += parse_section(th_match.group(1), "threads")
    return entries


def preflight(article_id, note_url):
    """読み取りのみ。ファイルへの書き込みは一切行わない。

    Returns (issues: list[str], ctx: dict). issuesが空ならすべて通過。
    """
    issues = []
    ctx = {}

    if not URL_RE.match(note_url):
        issues.append(f"note URLの形式が不正です(note.com URLでない、または[]()を含む): {note_url!r}")

    draft_files = sorted(DRAFT_DIR.glob("*.md")) if DRAFT_DIR.exists() else []
    if len(draft_files) != 1:
        issues.append(f"draft候補が{len(draft_files)}件です(1件のみ許可): {[p.name for p in draft_files]}")
    else:
        ctx["draft_path"] = draft_files[0]
        title, keyword, category = parse_front_matter(draft_files[0])
        if not title or not keyword or not category:
            issues.append(f"draftのfront matterからtitle/keyword/categoryを取得できませんでした: {draft_files[0]}")
        else:
            ctx["title"], ctx["keyword"], ctx["category"] = title, keyword, category

    rows = mt.read_topics()
    ctx["topics_rows"] = rows
    existing = next((r for r in rows if r["id"] == str(article_id)), None)
    if existing is None:
        existing_ids = [int(r["id"]) for r in rows if r["id"].isdigit()]
        expected_next = max(existing_ids, default=0) + 1
        if expected_next != article_id:
            issues.append(
                f"article_idが一致しません(topics.csvの次のidは{expected_next}、指定は{article_id})"
            )
        ctx["topics_action"] = "add"
    else:
        if "title" in ctx and existing["title"] != ctx["title"]:
            issues.append(
                "topics.csvの既存タイトルとdraftのタイトルが一致しません。"
                f" topics.csv={existing['title']!r} draft={ctx['title']!r}"
            )
        ctx["topics_action"] = "update"
        ctx["existing_topics_row"] = existing

    xx = f"{article_id:02d}"
    promo_md = SOCIAL_DIR / f"article-{xx}-promotions.md"
    if not promo_md.exists():
        issues.append(f"SNS宣伝ファイルが見つかりません: {promo_md}")
    else:
        ctx["promo_md"] = promo_md
        entries = parse_promotions_md(promo_md.read_text(encoding="utf-8"))
        x_entries = [e for e in entries if e[0] == "x"]
        th_entries = [e for e in entries if e[0] == "threads"]
        if len(x_entries) != 5 or len(th_entries) != 5:
            issues.append(
                f"SNS宣伝ファイルのパース結果が不正です(X={len(x_entries)} Threads={len(th_entries)}、"
                "それぞれ5件必要です)"
            )
        keys = [(p, pt) for p, pt, _ in entries]
        dupes = {k for k in keys if keys.count(k) > 1}
        if dupes:
            issues.append(f"SNS宣伝ファイル内でplatform/post_typeが重複しています: {sorted(dupes)}")
        if len(x_entries) == 5 and len(th_entries) == 5 and not dupes:
            ctx["promo_entries"] = entries

    if "promo_entries" in ctx:
        target_keys = {(p, pt) for p, pt, _ in ctx["promo_entries"]}
        existing_promo_rows = [r for r in mp.read_rows() if r["article_id"] == str(article_id)]
        stray = [
            r for r in existing_promo_rows
            if (r["platform"], r["post_type"]) not in target_keys
        ]
        if stray:
            issues.append(
                "promotions.csvに、今回のSNS宣伝ファイルの内容と一致しない既存行があります"
                f"(安全に再実行できません): {stray}"
            )
        ctx["existing_promo_rows"] = existing_promo_rows

    try:
        git_entries = vaw.git_status_entries()
    except RuntimeError as e:
        issues.append(f"git status取得に失敗しました: {e}")
        git_entries = []

    deleted = [p for c, p in git_entries if "D" in c]
    if deleted:
        issues.append(f"削除されたファイルがgit statusにあります: {deleted}")

    already_staged = [p for c, p in git_entries if c[0] not in (" ", "?")]
    if already_staged:
        issues.append(f"既にstagedされているファイルがあります(想定外): {already_staged}")

    # このスクリプト実行前に許可される変更は、まだcommitされていない
    # draft本体とSNS宣伝ファイル(いずれもClaude Codeが直前に作成したもの)のみ。
    allowed_pre_existing = set()
    if "draft_path" in ctx:
        allowed_pre_existing.add(str(ctx["draft_path"].relative_to(ROOT)))
    if "promo_md" in ctx:
        allowed_pre_existing.add(str(ctx["promo_md"].relative_to(ROOT)))
    xx_thumb = f"{article_id:02d}"
    thumb_path = vaw.THUMBNAILS_DIR / f"article-{xx_thumb}-thumbnail.md"
    if article_id >= 9 and thumb_path.exists():
        allowed_pre_existing.add(str(thumb_path.relative_to(ROOT)))

    unexpected = [p for _, p in git_entries if p not in allowed_pre_existing]
    if unexpected:
        issues.append(f"git statusに想定外の変更ファイルがあります: {unexpected}")

    return issues, ctx


def main():
    if len(sys.argv) != 3:
        print("Usage: complete_publish.py <article_id> <note_url>")
        sys.exit(1)

    article_id_arg = sys.argv[1]
    note_url = sys.argv[2]

    if not article_id_arg.isdigit():
        print(f"[ABORT] article_idは整数である必要があります: {article_id_arg!r}", file=sys.stderr)
        sys.exit(1)
    article_id = int(article_id_arg)

    issues, ctx = preflight(article_id, note_url)

    print(f"[PREFLIGHT] {len(issues)}件の問題" if issues else "[PREFLIGHT] すべて通過(書き込みはまだ行っていません)")
    for issue in issues:
        print(f"[FAIL] {issue}")

    if issues:
        print(
            "[ABORT] preflightチェックで問題が見つかったため、"
            "topics.csv・draft・promotions.csvへの書き込みは一切行っていません。",
            file=sys.stderr,
        )
        sys.exit(1)

    # --- ここから書き込み(preflightをすべて通過した場合のみ到達) ---

    title = ctx["title"]

    if ctx["topics_action"] == "add":
        assigned_id = mt.cmd_add_topic(title, ctx["keyword"], ctx["category"])
        if assigned_id != str(article_id):
            print(f"[ABORT] 予期しないid割り当てです: {assigned_id}", file=sys.stderr)
            sys.exit(1)

    mt.cmd_mark_published(str(article_id), note_url)

    draft_path = ctx["draft_path"]
    PUBLISHED_DIR.mkdir(parents=True, exist_ok=True)
    published_path = PUBLISHED_DIR / draft_path.name
    if published_path.exists():
        print(f"[ABORT] 移動先に同名ファイルが既に存在します(移動を中断): {published_path}", file=sys.stderr)
        sys.exit(1)
    shutil.move(str(draft_path), str(published_path))
    print(f"[OK] draft -> published へ移動: {published_path.relative_to(ROOT)}")

    for platform, post_type, timing in ctx["promo_entries"]:
        mp.cmd_add(str(article_id), title, platform, post_type, note_url, timing)

    promo_rows = [r for r in mp.read_rows() if r["article_id"] == str(article_id)]
    x_n = sum(1 for r in promo_rows if r["platform"] == "x")
    th_n = sum(1 for r in promo_rows if r["platform"] == "threads")
    if len(promo_rows) != 10 or x_n != 5 or th_n != 5:
        print(
            f"[ABORT] promotions.csv登録件数の検証に失敗しました: 合計{len(promo_rows)} X={x_n} Threads={th_n}"
            "(ここまでの変更は残っています。ロールバックは行いません)",
            file=sys.stderr,
        )
        sys.exit(1)
    if not all(r["status"] == "ready" for r in promo_rows):
        print("[ABORT] promotions.csvにstatus=ready以外の行があります", file=sys.stderr)
        sys.exit(1)
    print(f"[OK] promotions.csv登録確認: 合計{len(promo_rows)} X={x_n} Threads={th_n} 全件ready")

    report_lines, verify_ok = vaw.run_checks(article_id)
    print("\n".join(report_lines))
    if not verify_ok:
        print("[ABORT] verify_article_workflowでFAILが検出されたため、git保存を行いません", file=sys.stderr)
        sys.exit(1)

    expected = vaw.expected_files_for(article_id, mt.read_topics())
    commit_msg = f"Publish article {article_id}: {title} with social promotion package"
    sync_ok, sync_log = gss.safe_sync(sorted(expected), commit_msg)
    print("\n".join(sync_log))
    if not sync_ok:
        print("[ABORT] git_safe_syncが失敗しました(上記ログを確認してください)", file=sys.stderr)
        sys.exit(1)

    print("complete_publish.py: 全工程成功")


if __name__ == "__main__":
    main()
