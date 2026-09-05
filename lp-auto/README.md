# lp-auto — AI LP制作自動化システム(半自動化 Ver.1)

クライアントから受け取ったヒアリング情報をもとに、ヒアリング整理からLPのHTML/CSS/JavaScript実装・QAまでを、案件ごとに同じ手順で進めるための仕組みです。

**現時点ではAI APIによる完全自動実行は行いません。** Claude Codeを制作エージェントとして使い、人が各工程を確認しながら進める「半自動化」の仕組みです。APIキーは使用しません。

## 使い方

### STEP 1: 案件フォルダを作成する

```
python3 scripts/init_project.py project-name
```

`project-name` には、その案件を表す英数字・ハイフン・アンダースコアの名前を指定します(例: `flexia-personal-gym`)。実行すると `projects/project-name/` に案件フォルダが作成されます。同名フォルダが既にある場合は上書きせずエラーになります。

### STEP 2: ヒアリング内容を入力する

```
projects/project-name/client-brief.md
```

を開き、クライアントから受け取った情報(基本情報・ターゲット・商品サービス・信頼材料・CTA・デザイン希望・素材・補足)を入力します。**空欄のままの項目は「未入力」として扱われ、後工程で勝手に埋められることはありません。**

### STEP 3: Claude Codeに制作を依頼する

Claude Codeに対して、次のように依頼します。

```
lp-auto/prompts/01〜07を順番に実行して、
projects/project-name の案件を制作してください
```

`prompts/01_brief_analysis.md` から `07_image_prompts.md` まで、前工程の出力を読みながら順番に `projects/project-name/outputs/` へMarkdownを出力していきます。

### STEP 4: 成果物を確認する

`projects/project-name/outputs/` に生成された各Markdown(ブリーフ分析・ターゲット分析・LP戦略・LP構成・LP本文・デザインガイド・画像プロンプト)を確認します。内容に違和感があれば、この時点で修正を依頼してください。

### STEP 5: HTML/CSS/JSを実装する

Claude Codeに、`05_lp_copy.md`(本文)と `06_design_guide.md`(デザイン方針)をもとに `projects/project-name/site/` 配下(`index.html` / `css/style.css` / `js/main.js`)への実装を依頼します。

### STEP 6: QAを行う

```
lp-auto/prompts/08_qa_review.mdを実行して、
projects/project-name のQAを行ってください
```

実装済みのサイトとこれまでの成果物を突き合わせ、`projects/project-name/outputs/08_qa_report.md` にCRITICAL/HIGH/MEDIUM/LOWで分類された結果が出力されます。

### STEP 7: 人間が最終チェックする

QAレポートの指摘内容を確認し、特に下記「必ず人間が確認する工程」の内容を人が最終確認したうえで、クライアントへ納品・公開します。

## AIが自動化してよい工程

- ヒアリング内容の整理(不足・矛盾の洗い出し)
- ターゲット分析
- 訴求・USP設計のたたき台作成
- LP構成案の作成
- LP本文の下書き作成
- デザイン仕様書の下書き作成
- 画像生成プロンプトの下書き作成
- HTML/CSS/JavaScriptの実装
- QAチェック(問題点の洗い出しとレポート作成)

## 必ず人間が確認する工程

- **ターゲット・訴求の最終決定**(AIのたたき台をそのまま採用しない)
- **法的・事実関係**(薬機法・景品表示法など、業種ごとの表現規制の最終確認)
- **料金**(brief記載内容との整合性、最新の料金であるかの確認)
- **実績**(捏造がないか、開示してよい実績かの最終確認)
- **デザイン**(クライアントのブランドイメージに合っているか)
- **CTA**(実際の申込・問い合わせ導線が正しく機能するか)
- **納品前確認**(公開前の最終目視チェック、本番へのアップロード作業)

## フォルダ構成

```
lp-auto/
├── README.md
├── .gitignore
├── prompts/                     各工程のプロンプト(01〜08)
├── templates/
│   └── client-brief-template.md ヒアリングシートの雛形
├── scripts/
│   └── init_project.py          案件フォルダ作成スクリプト
└── projects/                    案件ごとの制作物(案件フォルダはこの下に作成される)
```

## 制約事項

- npm、React、Next.js等のフレームワークは導入していません(HTML/CSS/JavaScriptのみ)
- `scripts/` はPython標準ライブラリのみで動作します
- APIキー・アクセストークンは使用しません。LP本文・デザイン・実装の生成はすべてClaude Codeとの対話で行います
- `note-auto/` および既存のポートフォリオサイト(`index.html` 等)とは独立したプロジェクトです
