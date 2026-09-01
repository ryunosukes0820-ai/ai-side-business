#!/usr/bin/env python3
"""「公開完了 + URL」後のローカル処理を1回にまとめるオーケストレーションスクリプト。

前提: SNS投稿文(social/article-XX-promotions.md)はClaude Codeが
このスクリプトの実行前に作成済みであること。投稿文そのものの生成は行わない。

行うこと:
  1. article_id/URL形式の検証
  2. draft候補の特定(1件のみ許可)
  3. topics.csvへの登録(未登録なら追加) + published更新
  4. draft -> published への移動
  5. SNS宣伝ファイルの存在確認とpromotions.csvへの10件登録
  6. verify_article_workflow.py による検証
  7. 問題なければ git_safe_sync.py で add -> commit -> push

危険が伴う操作(削除・上書き・巻き戻し)は一切行わない。
途中で条件を満たさない場合はその時点で中断し、状態をそのまま報告する
(自動ロールバックは行わない)。

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


def abort(msg):
    print(f"[ABORT] {msg}", file=sys.stderr)
    sys.exit(1)


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


def main():
    if len(sys.argv) != 3:
        print("Usage: complete_publish.py <article_id> <note_url>")
        sys.exit(1)

    article_id_arg = sys.argv[1]
    note_url = sys.argv[2]

    if not article_id_arg.isdigit():
        abort(f"article_idは整数である必要があります: {article_id_arg!r}")
    article_id = int(article_id_arg)

    if not URL_RE.match(note_url):
        abort(f"note URLの形式が不正です(note.com URLでない、または[]()を含む): {note_url!r}")

    draft_files = sorted(DRAFT_DIR.glob("*.md")) if DRAFT_DIR.exists() else []
    if len(draft_files) != 1:
        abort(f"draft候補が{len(draft_files)}件です(1件のみ許可): {[p.name for p in draft_files]}")
    draft_path = draft_files[0]

    title, keyword, category = parse_front_matter(draft_path)
    if not title or not keyword or not category:
        abort(f"draftのfront matterからtitle/keyword/categoryを取得できませんでした: {draft_path}")

    rows = mt.read_topics()
    existing = next((r for r in rows if r["id"] == str(article_id)), None)

    if existing is None:
        existing_ids = [int(r["id"]) for r in rows if r["id"].isdigit()]
        expected_next = max(existing_ids, default=0) + 1
        if expected_next != article_id:
            abort(
                f"article_idが一致しません(topics.csvの次のidは{expected_next}、"
                f"指定は{article_id})。topics.csvは変更していません。"
            )
        assigned_id = mt.cmd_add_topic(title, keyword, category)
        if assigned_id != str(article_id):
            abort(f"予期しないid割り当てです: {assigned_id}")
    else:
        if existing["title"] != title:
            abort(
                "topics.csvの既存タイトルとdraftのタイトルが一致しません。"
                f" topics.csv={existing['title']!r} draft={title!r}"
            )

    mt.cmd_mark_published(str(article_id), note_url)

    PUBLISHED_DIR.mkdir(parents=True, exist_ok=True)
    published_path = PUBLISHED_DIR / draft_path.name
    if published_path.exists():
        abort(f"移動先に同名ファイルが既に存在します(移動を中断): {published_path}")
    shutil.move(str(draft_path), str(published_path))
    print(f"[OK] draft -> published へ移動: {published_path.relative_to(ROOT)}")

    xx = f"{article_id:02d}"
    promo_md = SOCIAL_DIR / f"article-{xx}-promotions.md"
    if not promo_md.exists():
        abort(
            f"SNS宣伝ファイルが見つかりません: {promo_md}"
            "(先にClaude CodeでSNS投稿文を作成・保存してください。"
            "topics.csv更新とdraft移動はすでに完了しています)"
        )

    entries = parse_promotions_md(promo_md.read_text(encoding="utf-8"))
    x_entries = [e for e in entries if e[0] == "x"]
    th_entries = [e for e in entries if e[0] == "threads"]
    if len(x_entries) != 5 or len(th_entries) != 5:
        abort(
            f"SNS宣伝ファイルのパース結果が不正です(X={len(x_entries)} Threads={len(th_entries)})。"
            "promotions.csvへの登録は行っていません。"
        )

    for platform, post_type, timing in entries:
        mp.cmd_add(str(article_id), title, platform, post_type, note_url, timing)

    promo_rows = [r for r in mp.read_rows() if r["article_id"] == str(article_id)]
    x_n = sum(1 for r in promo_rows if r["platform"] == "x")
    th_n = sum(1 for r in promo_rows if r["platform"] == "threads")
    if len(promo_rows) != 10 or x_n != 5 or th_n != 5:
        abort(f"promotions.csv登録件数の検証に失敗しました: 合計{len(promo_rows)} X={x_n} Threads={th_n}")
    if not all(r["status"] == "ready" for r in promo_rows):
        abort("promotions.csvにstatus=ready以外の行があります")
    print(f"[OK] promotions.csv登録確認: 合計{len(promo_rows)} X={x_n} Threads={th_n} 全件ready")

    report_lines, verify_ok = vaw.run_checks(article_id)
    print("\n".join(report_lines))
    if not verify_ok:
        abort("verify_article_workflowでFAILが検出されたため、git保存を行いません")

    expected = vaw.expected_files_for(article_id, mt.read_topics())
    commit_msg = f"Publish article {article_id}: {title} with social promotion package"
    sync_ok, sync_log = gss.safe_sync(sorted(expected), commit_msg)
    print("\n".join(sync_log))
    if not sync_ok:
        abort("git_safe_syncが失敗しました(上記ログを確認してください)")

    print("complete_publish.py: 全工程成功")


if __name__ == "__main__":
    main()
