#!/usr/bin/env python3
"""social/promotions.csv の管理用スクリプト。

SNS投稿文の生成はClaude Codeが担当し(prompts/social-promotion.md に沿って作成)、
このスクリプトはCSVの初期化・行の登録(重複防止つき)・ステータス更新のみを行う。
SNSへの投稿・API接続は一切行わない。削除コマンドは実装しない。

Usage:
    python3 scripts/manage_promotions.py init
    python3 scripts/manage_promotions.py add <article_id> <article_title> <platform> <post_type> <article_url> <recommended_timing>
    python3 scripts/manage_promotions.py list-ready [article_id]
    python3 scripts/manage_promotions.py mark-posted <article_id> <platform> <post_type>
"""

import csv
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMOTIONS_CSV = ROOT / "social" / "promotions.csv"

FIELDNAMES = [
    "article_id",
    "article_title",
    "platform",
    "post_type",
    "article_url",
    "recommended_timing",
    "status",
    "posted_at",
]


def ensure_dir():
    PROMOTIONS_CSV.parent.mkdir(parents=True, exist_ok=True)


def read_rows():
    if not PROMOTIONS_CSV.exists():
        return []
    with PROMOTIONS_CSV.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_rows(rows):
    ensure_dir()
    with PROMOTIONS_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def cmd_init():
    ensure_dir()
    if PROMOTIONS_CSV.exists():
        print(f"既に存在します: {PROMOTIONS_CSV}")
        return
    write_rows([])
    print(f"作成しました: {PROMOTIONS_CSV}")


def cmd_add(article_id, article_title, platform, post_type, article_url, recommended_timing):
    rows = read_rows()

    for row in rows:
        if (
            row["article_id"] == article_id
            and row["platform"].lower() == platform.lower()
            and row["post_type"] == post_type
        ):
            print(
                f"既に登録済みのため追加しません: article_id={article_id}, "
                f"platform={platform}, post_type={post_type}"
            )
            return

    rows.append({
        "article_id": article_id,
        "article_title": article_title,
        "platform": platform.lower(),
        "post_type": post_type,
        "article_url": article_url,
        "recommended_timing": recommended_timing,
        "status": "ready",
        "posted_at": "",
    })
    write_rows(rows)
    print(f"登録しました: article_id={article_id}, platform={platform}, post_type={post_type}")


def cmd_list_ready(article_id=None):
    rows = read_rows()
    rows = [r for r in rows if r["status"] == "ready"]
    if article_id:
        rows = [r for r in rows if r["article_id"] == article_id]
    if not rows:
        print("readyの投稿がありません。")
        return
    for row in rows:
        print(
            f"[{row['article_id']}] {row['platform']} / {row['post_type']} "
            f"(推奨タイミング: {row['recommended_timing']})"
        )


def cmd_mark_posted(article_id, platform, post_type):
    rows = read_rows()
    if not rows:
        print("promotions.csv にデータがありません。")
        sys.exit(1)

    target = None
    for row in rows:
        if (
            row["article_id"] == article_id
            and row["platform"].lower() == platform.lower()
            and row["post_type"] == post_type
        ):
            target = row
            break

    if target is None:
        print(f"該当行が見つかりません: article_id={article_id}, platform={platform}, post_type={post_type}")
        sys.exit(1)

    now = datetime.now().isoformat(timespec="seconds")
    target["status"] = "posted"
    target["posted_at"] = now
    write_rows(rows)
    print(f"posted に更新しました(article_id={article_id}, platform={platform}, post_type={post_type}, posted_at={now})")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]

    if command == "init":
        cmd_init()
    elif command == "add":
        if len(sys.argv) != 8:
            print(
                "Usage: manage_promotions.py add <article_id> <article_title> <platform> "
                "<post_type> <article_url> <recommended_timing>"
            )
            sys.exit(1)
        cmd_add(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
    elif command == "list-ready":
        article_id = sys.argv[2] if len(sys.argv) == 3 else None
        cmd_list_ready(article_id)
    elif command == "mark-posted":
        if len(sys.argv) != 5:
            print("Usage: manage_promotions.py mark-posted <article_id> <platform> <post_type>")
            sys.exit(1)
        cmd_mark_posted(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print(f"不明なコマンドです: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
