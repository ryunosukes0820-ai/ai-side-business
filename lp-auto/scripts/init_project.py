#!/usr/bin/env python3
"""LP制作案件の雛形フォルダを作成する補助スクリプト。

client-brief.md の作成とフォルダ構成のみを行う。
LP本文・デザイン・実装の生成は行わない(Claude Codeが prompts/ の
指示に沿って対話形式で行う)。

Usage:
    python3 scripts/init_project.py <project-name>
"""

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECTS_DIR = ROOT / "projects"
TEMPLATE = ROOT / "templates" / "client-brief-template.md"

NAME_RE = re.compile(r"^[A-Za-z0-9_-]+$")

INDEX_HTML_STUB = """<!-- {project_name} のLP本文をここに実装する -->
<!-- 05_lp_copy.md の文章、06_design_guide.md のデザイン方針に沿って作成する -->
"""

STYLE_CSS_STUB = """/* {project_name} のLPスタイルをここに実装する */
/* 06_design_guide.md のデザイン方針に沿って作成する */
"""

MAIN_JS_STUB = """// {project_name} のLP用JavaScript
// 必要な場合のみ実装する(ハンバーガーメニュー、FAQアコーディオンなど)
"""


def create_project(project_name):
    if not NAME_RE.match(project_name):
        print(
            f"エラー: project-nameに使用できるのは英数字・ハイフン・アンダースコアのみです: {project_name!r}",
            file=sys.stderr,
        )
        sys.exit(1)

    if not TEMPLATE.exists():
        print(f"エラー: テンプレートが見つかりません: {TEMPLATE}", file=sys.stderr)
        sys.exit(1)

    project_dir = PROJECTS_DIR / project_name
    if project_dir.exists():
        print(f"エラー: 同名の案件フォルダが既に存在します(上書きしません): {project_dir}", file=sys.stderr)
        sys.exit(1)

    site_dir = project_dir / "site"
    outputs_dir = project_dir / "outputs"
    css_dir = site_dir / "css"
    js_dir = site_dir / "js"
    images_dir = site_dir / "images"

    for d in (project_dir, outputs_dir, site_dir, css_dir, js_dir, images_dir):
        d.mkdir(parents=True, exist_ok=False)

    shutil.copy(TEMPLATE, project_dir / "client-brief.md")
    (site_dir / "index.html").write_text(INDEX_HTML_STUB.format(project_name=project_name), encoding="utf-8")
    (css_dir / "style.css").write_text(STYLE_CSS_STUB.format(project_name=project_name), encoding="utf-8")
    (js_dir / "main.js").write_text(MAIN_JS_STUB.format(project_name=project_name), encoding="utf-8")
    (images_dir / ".gitkeep").write_text("", encoding="utf-8")

    print(f"作成しました: {project_dir}")
    print(f"  - {project_dir / 'client-brief.md'}")
    print(f"  - {outputs_dir}/")
    print(f"  - {site_dir / 'index.html'}")
    print(f"  - {css_dir / 'style.css'}")
    print(f"  - {js_dir / 'main.js'}")
    print(f"  - {images_dir}/")
    print()
    print("次のステップ: client-brief.md に情報を入力してから、prompts/01〜08 を順番に進めてください。")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/init_project.py <project-name>")
        sys.exit(1)
    create_project(sys.argv[1])


if __name__ == "__main__":
    main()
