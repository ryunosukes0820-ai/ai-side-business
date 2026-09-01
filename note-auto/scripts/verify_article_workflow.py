#!/usr/bin/env python3
"""記事1本ぶんの状態を1回の実行でまとめて確認する読み取り専用スクリプト。

ファイルは一切書き換えない。topics.csv・social/promotions.csv・
articles/published/*・thumbnails/*・git status を読み取り、
PASS / WARN / FAIL 形式でレポートする。

Usage:
    python3 scripts/verify_article_workflow.py <article_id>
"""

import csv
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOPICS_CSV = ROOT / "topics.csv"
PROMOTIONS_CSV = ROOT / "social" / "promotions.csv"
PUBLISHED_DIR = ROOT / "articles" / "published"
DRAFT_DIR = ROOT / "articles" / "draft"
THUMBNAILS_DIR = ROOT / "thumbnails"
SOCIAL_DIR = ROOT / "social"

URL_RE = re.compile(r"^https://note\.com/[^\[\]()]+$")


def slugify(text):
    keep = [c if c.isalnum() else "-" for c in text]
    slug = "".join(keep).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.lower() or "article"


def read_topics():
    if not TOPICS_CSV.exists():
        return []
    with TOPICS_CSV.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def read_promotions():
    if not PROMOTIONS_CSV.exists():
        return []
    with PROMOTIONS_CSV.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def find_published_file(article_id, topics_rows=None):
    if topics_rows is None:
        topics_rows = read_topics()
    row = next((r for r in topics_rows if r["id"] == str(article_id)), None)
    if row is None:
        return None
    slug = slugify(row["title"])
    if not PUBLISHED_DIR.exists():
        return None
    for p in PUBLISHED_DIR.glob("*.md"):
        if slug in p.stem:
            return p
    return None


def compute_body(text):
    m = re.match(r"^---\n.*?\n---\n", text, re.S)
    rest = text[m.end():] if m else text
    end_idx = len(rest)
    idx = rest.find("\n## 執筆時の参考情報")
    if idx != -1:
        end_idx = min(end_idx, idx)
    return rest[:end_idx].strip("\n")


def extract_meta(text, field):
    m = re.search(rf"\*\*{re.escape(field)}\*\*:\s*(.+)", text)
    return m.group(1).strip() if m else None


def check_thumbnail(article_id):
    xx = f"{int(article_id):02d}"
    path = THUMBNAILS_DIR / f"article-{xx}-thumbnail.md"
    if not path.exists():
        return {"exists": False, "path": path}
    text = path.read_text(encoding="utf-8")
    required = ["メインコピー", "おすすめ構図", "文字配置", "背景イメージ", "画像生成AI用プロンプト"]
    optional = ["サブコピー", "アイコン/モチーフ", "アイコン／モチーフ"]
    missing_required = [
        k for k in required if not re.search(rf"-\s*{re.escape(k)}\s*:\s*\S", text)
    ]
    has_optional = any(
        re.search(rf"-\s*{re.escape(k)}\s*:\s*\S", text) for k in optional
    )
    return {
        "exists": True,
        "path": path,
        "missing_required": missing_required,
        "has_optional": has_optional,
    }


def repo_prefix():
    """Path of ROOT relative to the git repository top-level (e.g. "note-auto/"),
    empty string if ROOT itself is the repository top-level.

    git's --porcelain output is always relative to the repository top-level
    regardless of cwd, so this prefix must be stripped to get ROOT-relative paths.
    """
    proc = subprocess.run(
        ["git", "rev-parse", "--show-prefix"], cwd=ROOT, capture_output=True, text=True
    )
    if proc.returncode != 0:
        return ""
    return proc.stdout.strip()


def git_status_entries():
    proc = subprocess.run(
        ["git", "status", "--porcelain=v1", "-z", "--untracked-files=all"],
        cwd=ROOT,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"git status failed: {proc.stderr.decode('utf-8', 'replace')}")
    prefix = repo_prefix()
    data = proc.stdout.decode("utf-8", "replace")
    parts = data.split("\0")
    entries = []
    i = 0
    while i < len(parts):
        part = parts[i]
        if not part:
            i += 1
            continue
        code = part[:2]
        path = part[3:]
        if code[0] in ("R", "C"):
            i += 1  # skip the accompanying old-path field
        i += 1
        if prefix and not path.startswith(prefix):
            continue  # outside the ROOT subtree, not our concern
        rel_path = path[len(prefix):] if prefix else path
        entries.append((code, rel_path))
    return entries


def expected_files_for(article_id, topics_rows=None):
    if topics_rows is None:
        topics_rows = read_topics()
    xx = f"{int(article_id):02d}"
    expected = {"topics.csv", "social/promotions.csv", f"social/article-{xx}-promotions.md"}
    if int(article_id) >= 9:
        thumb = THUMBNAILS_DIR / f"article-{xx}-thumbnail.md"
        if thumb.exists():
            expected.add(f"thumbnails/article-{xx}-thumbnail.md")
    pf = find_published_file(article_id, topics_rows)
    if pf is not None:
        expected.add(str(pf.relative_to(ROOT)))
    return expected


def run_checks(article_id):
    lines = []
    fails = 0
    warns = 0

    def ok(msg):
        lines.append(f"[PASS] {msg}")

    def warn(msg):
        nonlocal warns
        warns += 1
        lines.append(f"[WARN] {msg}")

    def fail(msg):
        nonlocal fails
        fails += 1
        lines.append(f"[FAIL] {msg}")

    topics_rows = read_topics()
    row = next((r for r in topics_rows if r["id"] == str(article_id)), None)

    # topics.csv
    if row is None:
        warn(f"topics.csvにid={article_id}の行がありません(未登録の段階の可能性)")
    else:
        if row["status"] == "published":
            if row["note_url"] and URL_RE.match(row["note_url"]):
                ok(f"topics.csv: status=published, note_url形式OK ({row['note_url']})")
            elif not row["note_url"]:
                fail("topics.csv: status=publishedだがnote_urlが空です")
            else:
                fail(f"topics.csv: note_urlの形式が不正です(角括弧/丸括弧混入の疑い): {row['note_url']!r}")
        else:
            warn(f"topics.csv: status={row['status']!r}(publishedではありません)")

    # published article body
    pf = find_published_file(article_id, topics_rows)
    if pf is None:
        warn("articles/published/ に該当記事が見つかりません(未移動の可能性)")
    else:
        text = pf.read_text(encoding="utf-8")
        body = compute_body(text)
        count = len(body)
        if 2800 <= count <= 3200:
            ok(f"本文文字数: {count}字(2,800〜3,200字の範囲内)")
        else:
            fail(f"本文文字数: {count}字(2,800〜3,200字の範囲外)")

        if "<!--" in text or "-->" in text:
            fail("HTML/Markdownコメントが混入しています")
        else:
            ok("HTML/Markdownコメントの混入なし")

        paid_line = extract_meta(text, "有料ラインの位置")
        if paid_line:
            ok(f"有料ラインの位置(メタ情報記載): {paid_line}")
        else:
            warn("有料ラインの位置がnote投稿メタ情報に見つかりません")

        meta_count = extract_meta(text, "本文の文字数")
        if meta_count:
            digits = re.sub(r"[^\d]", "", meta_count)
            if digits and int(digits) == count:
                ok(f"メタ情報の文字数記載が実測値と一致: {meta_count}")
            else:
                fail(f"メタ情報の文字数記載が実測値と不一致: メタ={meta_count!r} 実測={count}")

    # thumbnail
    if int(article_id) >= 9:
        th = check_thumbnail(article_id)
        if not th["exists"]:
            fail(f"thumbnailファイルが見つかりません: {th['path']}")
        else:
            if th["missing_required"]:
                fail(f"thumbnail必須項目が不足: {th['missing_required']}")
            else:
                ok("thumbnail必須5項目そろっています")
            if not th["has_optional"]:
                warn("thumbnailの任意項目(サブコピー/アイコン・モチーフ)が両方とも未記載です")

    # promotions.csv
    promo_rows = [r for r in read_promotions() if r["article_id"] == str(article_id)]
    if not promo_rows:
        warn("promotions.csvに該当行がありません(未登録の段階の可能性)")
    else:
        x_rows = [r for r in promo_rows if r["platform"] == "x"]
        th_rows = [r for r in promo_rows if r["platform"] == "threads"]
        keys = [(r["platform"], r["post_type"]) for r in promo_rows]
        dupes = {k for k in keys if keys.count(k) > 1}
        if len(promo_rows) == 10 and len(x_rows) == 5 and len(th_rows) == 5 and not dupes:
            ok("promotions.csv: 10件(X=5/Threads=5)、重複なし")
        else:
            fail(
                f"promotions.csv件数異常: 合計{len(promo_rows)} X={len(x_rows)} "
                f"Threads={len(th_rows)} 重複={dupes}"
            )
        bad_urls = [r for r in promo_rows if not URL_RE.match(r["article_url"])]
        if bad_urls:
            fail(f"promotions.csvにURL形式不正な行があります: {[r['post_type'] for r in bad_urls]}")
        else:
            ok("promotions.csv: article_urlはすべて純粋なURL形式")
        bad_status = [r for r in promo_rows if r["status"] not in ("ready", "posted")]
        if bad_status:
            fail(f"promotions.csvに不正なstatus値があります: {bad_status}")
        else:
            ready_n = sum(1 for r in promo_rows if r["status"] == "ready")
            posted_n = sum(1 for r in promo_rows if r["status"] == "posted")
            ok(f"promotions.csv: status内訳 ready={ready_n} posted={posted_n}")

    # git status / unexpected files
    try:
        entries = git_status_entries()
    except RuntimeError as e:
        fail(str(e))
        entries = []

    expected = expected_files_for(article_id, topics_rows)
    deleted = [p for c, p in entries if "D" in c]
    unexpected = [p for c, p in entries if p not in expected]

    if deleted:
        fail(f"削除されたファイルがgit statusにあります: {deleted}")
    else:
        ok("git status: 削除ファイルなし")

    if unexpected:
        fail(f"想定外の変更ファイルがあります: {unexpected}")
    else:
        ok("git status: 想定外の変更ファイルなし")

    lines.append(f"---\nOVERALL: {'FAIL' if fails else 'PASS'} (FAIL={fails}, WARN={warns})")
    return lines, fails == 0


def main():
    if len(sys.argv) != 2:
        print("Usage: verify_article_workflow.py <article_id>")
        sys.exit(1)
    article_id = sys.argv[1]
    lines, ok = run_checks(article_id)
    print("\n".join(lines))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
