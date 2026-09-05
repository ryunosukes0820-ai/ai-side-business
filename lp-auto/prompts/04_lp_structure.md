# 04. LP Structure プロンプト

**目的**: LPのセクション構成(骨格)を設計する。

## 入力ファイル

- `projects/<project-name>/outputs/01_brief_analysis.md`
- `projects/<project-name>/outputs/02_target_analysis.md`
- `projects/<project-name>/outputs/03_lp_strategy.md`

## 使い方

上記3ファイルを読み込んだ上で、以下を設計する。

---

あなたはLPディレクターです。以下の情報をもとに、LPのセクション構成を設計してください。

- ブリーフ分析結果: {{brief_analysis}}
- ターゲット分析結果: {{target_analysis}}
- LP戦略: {{lp_strategy}}

## 基本のセクション候補

以下を基本候補としつつ、**案件の目的・業種・ターゲットに応じて過不足なく最適化する**(すべてを機械的に使う必要はない。不要なら省き、必要なら追加する)。

- FV(ファーストビュー)
- 悩み・共感
- 解決策
- 選ばれる理由
- サービス特徴
- 利用メリット
- 実績・信頼材料
- 料金
- 利用の流れ
- FAQ
- 最終CTA

## 各セクションについて記載する項目

1. **セクション名**
2. **目的**: このセクションで何を達成するか
3. **見出し案**: 実際に使う見出し文言の案
4. **入れる情報**: このセクションに含める具体的な情報(brief・戦略で確認できる範囲)
5. **CTAの有無**: このセクションにCTAボタンを置くか

## 出力

`projects/<project-name>/outputs/04_lp_structure.md` として、セクションを上から順に並べたMarkdownで保存する。
