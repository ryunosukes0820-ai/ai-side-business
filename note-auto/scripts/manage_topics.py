#!/usr/bin/env python3
"""topics.csv の進捗管理と、下書きファイルの雛形作成を行う補助スクリプト。

記事本文の生成は行わない(Claude Codeが対話形式でprompts/の指示に沿って執筆する)。
このスクリプトが担当するのは、CSVの状態更新とファイルの雑用のみ。

Usage:
    python3 scripts/manage_topics.py list
    python3 scripts/manage_topics.py set-status <id> <status>
    python3 scripts/manage_topics.py new-draft <id>
"""

import csv
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOPICS_CSV = ROOT / "topics.csv"
DRAFT_DIR = ROOT / "articles" / "draft"

FIELDNAMES = ["id", "title", "keyword", "category", "status", "note_url", "memo"]


def read_topics():
    with TOPICS_CSV.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_topics(rows):
    with TOPICS_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def cmd_list():
    rows = read_topics()
    if not rows:
        print("topics.csv にデータがありません。")
        return
    for row in rows:
        print(f"[{row['id']}] ({row['status']}) {row['title']} / {row['keyword']}")


def cmd_set_status(topic_id, new_status):
    rows = read_topics()
    target = next((r for r in rows if r["id"] == topic_id), None)
    if target is None:
        print(f"id={topic_id} が見つかりません。")
        sys.exit(1)
    target["status"] = new_status
    write_topics(rows)
    print(f"[{topic_id}] status -> {new_status}")


def slugify(text):
    keep = [c if c.isalnum() else "-" for c in text]
    slug = "".join(keep).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.lower() or "article"


def cmd_new_draft(topic_id):
    rows = read_topics()
    target = next((r for r in rows if r["id"] == topic_id), None)
    if target is None:
        print(f"id={topic_id} が見つかりません。")
        sys.exit(1)

    DRAFT_DIR.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat().replace("-", "")
    filename = f"{today}-{slugify(target['title'])}.md"
    path = DRAFT_DIR / filename

    if path.exists():
        print(f"既に存在します: {path}")
        return

    front_matter = (
        "---\n"
        f"title: \"{target['title']}\"\n"
        f"keyword: \"{target['keyword']}\"\n"
        f"category: \"{target['category']}\"\n"
        f"status: draft\n"
        f"created: {date.today().isoformat()}\n"
        "---\n\n"
        "<!-- prompts/research.md -> outline.md -> writing.md -> review.md の順に進めて本文を作成してください -->\n"
    )
    path.write_text(front_matter, encoding="utf-8")

    target["status"] = "下書き中"
    write_topics(rows)

    print(f"作成しました: {path}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]

    if command == "list":
        cmd_list()
    elif command == "set-status":
        if len(sys.argv) != 4:
            print("Usage: manage_topics.py set-status <id> <status>")
            sys.exit(1)
        cmd_set_status(sys.argv[2], sys.argv[3])
    elif command == "new-draft":
        if len(sys.argv) != 3:
            print("Usage: manage_topics.py new-draft <id>")
            sys.exit(1)
        cmd_new_draft(sys.argv[2])
    else:
        print(f"不明なコマンドです: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
