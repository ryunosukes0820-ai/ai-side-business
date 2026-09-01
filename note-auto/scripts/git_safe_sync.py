#!/usr/bin/env python3
"""明示的に指定したファイルだけを安全にgit add -> commit -> pushするスクリプト。

git status(-z) で確認した変更/未追跡ファイルの集合が、
指定したファイル一覧と完全に一致する場合だけ処理を進める。
一致しない場合・削除ファイルがある場合・push先がorigin main以外の場合は
一切addせず(またはcommit/pushせず)中断する。

git add . は実装しない。force pushも実装しない。

Usage:
    python3 scripts/git_safe_sync.py --files <path1> [<path2> ...] --message "<commit message>"
"""

import argparse
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify_article_workflow as vaw  # noqa: E402

ROOT = vaw.ROOT


def _run(args):
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True)


def safe_sync(files, message, branch="main", remote="origin"):
    log = []

    if branch != "main":
        return False, [f"[ABORT] push先ブランチはmainのみ許可しています(指定: {branch})"]
    if remote != "origin":
        return False, [f"[ABORT] push先リモートはoriginのみ許可しています(指定: {remote})"]
    if not files:
        return False, ["[ABORT] filesが空です"]
    for f in files:
        if f in (".", "*", "-A", "--all") or f.startswith("-"):
            return False, [f"[ABORT] 許可されないファイル指定です: {f!r}"]

    try:
        entries = vaw.git_status_entries()
    except RuntimeError as e:
        return False, [f"[ABORT] git status取得に失敗しました: {e}"]

    deleted = [p for c, p in entries if "D" in c]
    if deleted:
        return False, [f"[ABORT] 削除されたファイルが検出されました。処理を中断します: {deleted}"]

    changed = {p for _, p in entries}
    requested = set(files)

    extra = changed - requested
    missing = requested - changed
    if extra or missing:
        msg = ["[ABORT] 指定ファイルとgit statusの変更ファイルが完全一致しません。"]
        if extra:
            msg.append(f"  想定外の変更ファイル: {sorted(extra)}")
        if missing:
            msg.append(f"  変更が確認できないファイル: {sorted(missing)}")
        return False, msg

    log.append(f"[OK] git status確認: 指定ファイルと完全一致 {sorted(requested)}")

    already_staged = [p for c, p in entries if c[0] not in (" ", "?")]
    if already_staged and set(already_staged) - requested:
        return False, [f"[ABORT] 想定外のファイルが既にstagedです: {set(already_staged) - requested}"]

    add_proc = _run(["git", "add", "--"] + sorted(files))
    if add_proc.returncode != 0:
        return False, [f"[ABORT] git add失敗: {add_proc.stderr}"]
    log.append(f"[OK] git add実行: {sorted(files)}")

    staged_proc = subprocess.run(
        ["git", "diff", "--name-only", "--cached", "-z"],
        cwd=ROOT,
        capture_output=True,
    )
    if staged_proc.returncode != 0:
        return False, [f"[ABORT] staged一覧取得に失敗しました: {staged_proc.stderr.decode('utf-8', 'replace')}"]
    prefix = vaw.repo_prefix()
    raw_staged = {p for p in staged_proc.stdout.decode("utf-8", "replace").split("\0") if p}
    staged_set = {
        (p[len(prefix):] if prefix and p.startswith(prefix) else p) for p in raw_staged
    }
    if staged_set != requested:
        return False, [
            "[ABORT] commit前検証: staged一覧と指定ファイルが完全一致しません。"
            f" staged={sorted(staged_set)} requested={sorted(requested)}"
            " (安全のためgit resetは行わず、stagedのまま中断します)"
        ]
    log.append("[OK] staged一覧が指定ファイルと完全一致")

    commit_proc = _run(["git", "commit", "-m", message])
    if commit_proc.returncode != 0:
        return False, [f"[ABORT] git commit失敗(pushは行いません): {commit_proc.stderr}"]
    log.append(f"[OK] git commit成功: {commit_proc.stdout.strip().splitlines()[0] if commit_proc.stdout else message}")

    push_proc = _run(["git", "push", remote, branch])
    if push_proc.returncode != 0:
        return False, [f"[ABORT] git push失敗(commitはローカルに残っています): {push_proc.stderr}"]
    log.append(f"[OK] git push成功: {remote} {branch}")

    try:
        final_entries = vaw.git_status_entries()
    except RuntimeError as e:
        return False, [f"[WARN] push後のgit status取得に失敗: {e}"]

    if final_entries:
        log.append(f"[WARN] working treeがcleanではありません: {final_entries}")
        return True, log
    log.append("[OK] working tree clean")
    return True, log


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--message", required=True)
    parser.add_argument("--branch", default="main", choices=["main"])
    parser.add_argument("--remote", default="origin", choices=["origin"])
    args = parser.parse_args()

    ok, log = safe_sync(args.files, args.message, args.branch, args.remote)
    print("\n".join(log))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
