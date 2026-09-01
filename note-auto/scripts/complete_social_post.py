#!/usr/bin/env python3
"""SNS投稿完了(mark-posted)後の一連の処理を1回にまとめるスクリプト。

対象行(article_id + platform + post_type)が一意に特定できない場合、
または対象行が見つからない・既にposted済みの場合は、推測せず中断する。

行うこと:
  1. 対象行がreadyであることを確認
  2. mark-posted実行
  3. posted/posted_atを確認
  4. 他の行のstatusが変化していないことを確認
  5. social/promotions.csv だけを対象に git_safe_sync.py で保存

Usage:
    python3 scripts/complete_social_post.py <article_id> <platform> <post_type>
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import git_safe_sync as gss  # noqa: E402
import manage_promotions as mp  # noqa: E402


def abort(msg):
    print(f"[ABORT] {msg}", file=sys.stderr)
    sys.exit(1)


def main():
    if len(sys.argv) != 4:
        print("Usage: complete_social_post.py <article_id> <platform> <post_type>")
        sys.exit(1)

    article_id, platform, post_type = sys.argv[1], sys.argv[2], sys.argv[3]
    platform = platform.lower()

    rows = mp.read_rows()
    matches = [
        r for r in rows
        if r["article_id"] == str(article_id)
        and r["platform"].lower() == platform
        and r["post_type"] == post_type
    ]
    if len(matches) == 0:
        abort(f"該当行が見つかりません: article_id={article_id} platform={platform} post_type={post_type}")
    if len(matches) > 1:
        abort(f"該当行が複数あり一意に特定できません(推測しません): {matches}")

    target = matches[0]
    if target["status"] != "ready":
        abort(f"対象行はstatus={target['status']!r}のため処理しません(readyのみ処理可能)")

    others_before = [dict(r) for r in rows if r is not target]

    mp.cmd_mark_posted(str(article_id), platform, post_type)

    rows2 = mp.read_rows()
    target2 = next(
        (r for r in rows2 if r["article_id"] == str(article_id) and r["platform"].lower() == platform and r["post_type"] == post_type),
        None,
    )
    if target2 is None or target2["status"] != "posted" or not target2["posted_at"]:
        abort("mark-posted後の状態確認に失敗しました(status=posted / posted_at設定を確認できません)")
    print(f"[OK] 対象行を確認: article_id={article_id} platform={platform} post_type={post_type} status=posted posted_at={target2['posted_at']}")

    changed_others = []
    for before in others_before:
        after = next(
            (r for r in rows2
             if r["article_id"] == before["article_id"]
             and r["platform"] == before["platform"]
             and r["post_type"] == before["post_type"]),
            None,
        )
        if after != before:
            changed_others.append((before, after))
    if changed_others:
        abort(f"他の行が変化しています(想定外、git保存を中断します): {changed_others}")
    print(f"[OK] 他の{len(others_before)}件の行に変化なし")

    commit_msg = f"Mark article {article_id} {platform} {post_type} post as posted"
    sync_ok, sync_log = gss.safe_sync(["social/promotions.csv"], commit_msg)
    print("\n".join(sync_log))
    if not sync_ok:
        abort("git_safe_syncが失敗しました(上記ログを確認してください)")

    print("complete_social_post.py: 全工程成功")


if __name__ == "__main__":
    main()
