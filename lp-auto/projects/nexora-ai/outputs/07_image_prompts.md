# NEXORA AI Image Prompts

本文書は画像生成AIへ入力するためのプロンプト設計書である。**この工程では画像の生成そのものは行わない。**

**基本方針**: NEXORA AIのLPでは、画像をデザインの主役にしない。HERO Dashboard mockup・Workflow visualization・Bento Grid・Floating UI・Support diagramはいずれもHTML/CSS/inline SVGで実装する(`06_design_guide.md`8章・9章・13章・14章・17章を参照)。画像は、それらのUI表現だけでは出しにくい"雰囲気"を補う用途に限定し、**最大1〜2点**とする。

---

## 1. 画像が必要かどうかの判断

**結論: IMAGE01(1点)のみを推奨する。IMAGE02は生成しない。**

**判断理由**:
- HERO・HOW IT WORKS・FEATURES・SUPPORTは、いずれも`06_design_guide.md`でHTML/CSS/inline SVGによる実装が既に具体的に設計されている(Dashboard mockup、connected workflow、Bento Grid、放射状のsupport diagram)。これらに写真的な画像を追加すると、CSSで作り込んだUI表現と競合し、かえって「テック感」を弱める可能性がある
- USE CASEは`06_design_guide.md`16章でbrowser-style card/workflow card(HTML/CSS)による表現が既に設計されており、活用イメージを"例"として示す目的には十分機能する。実写画像を加える必然性は低い
- 一方、INSIGHT(SECTION03)は`06_design_guide.md`12章で「カード・リストを使わずミニマルに」「余白を大胆に取る」と設計されており、装飾は薄いgrid線または1本のglowラインのみにとどまっている。ここに抽象的なテクノロジービジュアルを背景として**ごく控えめに**加えることで、LP全体の中で最も静かなセクションに奥行きを持たせられる可能性がある。ただし必須ではなく、CSSのみ(grid線+glow)でも十分に成立する
- IMAGE02(Premium Technology Workspace)は、NEXORA AIが「FLEXIA/LUMIELほど人物写真に依存しない」方針(`06_design_guide.md`25章)を採っていることと、USE CASE/SUPPORTが既にHTML/CSSで十分に機能することから、**生成しない**と判断する。将来的にSTEP08以降のレビューで「やはり必要」と判断された場合のみ、改めて設計する

**推奨画像数**: 1点(IMAGE01)。ただし、実装時にCSSのみ(grid線・glow・gradientの組み合わせ)で十分な質感が出せると判断された場合は、**0点(画像なし)でも成立する**設計とする。

---

## 2. IMAGE01：Abstract AI Workflow Visual

【使用セクション(候補)】
SECTION03(INSIGHT)の背景装飾として、控えめに使用する候補。使用有無・使用箇所の最終判断は実装時に行ってよい(必須要素ではない)。

【目的】
「AIそのもの」ではなく「業務とAIをつなぐ支援」というテーマを、抽象的な接続・構造のビジュアルで補強する。HTML/CSSの装飾(grid線・glow)だけでは出しにくい、奥行きのあるテクスチャを補う。

【推奨ファイル名】
`nexora-workflow.webp`

【推奨アスペクト比】
**16:9**(横長)。背景装飾として広い面に敷きやすく、UIやテキストを上に重ねやすい比率のため。

【構図】
中央〜片側に、接続されたノード(点と線)による抽象的なワークフロー/ネットワーク構造を配置する。ノードや線は幾何学的で秩序立っており、無秩序なパーティクルの乱舞にはしない。画面の大部分には十分なネガティブスペース(余白)を残し、Web側でテキストやUIを重ねられるようにする。

【被写体】
抽象的な接続ノード・ライン・構造体のみ。人物・ロボット・脳・顔は一切描写しない。

【背景】
Dark Navy(`#07111F`〜`#0B172A`)を基調とした、構造化されたダークな空間。具体的なオフィス・機材・実在製品は描写しない。

【光・ライティング】
Blue(`#3B82F6`)〜Cyan(`#22D3EE`)のsubtleな発光。強いネオンではなく、抑制の効いた光の線・グロー。

【カラートーン】
Deep Navy/Navyを基調に、Blue・Cyan・Light Blue(`#60A5FA`)を控えめな差し色として使用。White(`#F8FAFC`)は細い光の線・点のハイライト程度に留める。

【スタイル】
Premium BtoB SaaS、Abstract workflow、Enterprise-grade、Minimal、Structured、Intelligent、Modern、Clean。広告的な派手さではなく、企業向けプロダクトサイトの背景として違和感のない抑制されたトーン。

【日本語プロンプト】
```
BtoB SaaS企業のブランドビジュアルにふさわしい、抽象的でミニマルなテクノロジービジュアル。ダークネイビー(#07111F〜#0B172A)を基調とした構造化された暗い空間に、幾何学的に接続されたノードとライン(点と線によるネットワーク/ワークフロー構造)を配置する。ノードや線は秩序立っており、無秩序なパーティクルの乱舞にはしない。光は鮮やかなブルー(#3B82F6)からシアン(#22D3EE)にかけての抑制の効いた発光とし、強いネオンや過剰な輝きは避ける。画面の大部分に余白を残し、テキストやUIを重ねられる構図にする。人物・ロボット・人型AI・脳のような表現は一切含めない。企業向けプロダクトサイトの背景として使える、上品で構造的、知的な印象のミニマルなビジュアル。文字・ロゴ・数字・グラフ・UIラベルは一切含めない。
```

【English Prompt】
```
A minimal, abstract technology visual suitable for a premium BtoB SaaS brand. Compose a structured dark navy space (#07111F to #0B172A) featuring geometrically connected nodes and lines forming an abstract network or workflow structure. The nodes and lines are orderly and structured, not a chaotic scatter of particles. Lighting is a restrained glow ranging from vivid blue (#3B82F6) to cyan (#22D3EE), avoiding harsh neon or excessive brightness. Leave generous negative space across most of the frame so text and UI elements can be overlaid. Do not include any human figures, robots, humanoid AI, or brain imagery. The overall mood is sophisticated, structured, and intelligent — suitable as a background for an enterprise technology product site. No text, no logos, no numbers, no charts, no UI labels.
```

【Negative Prompt / Avoid】
```
text, typography, letters, numbers, percentages, charts, graphs, dashboards with readable metrics, logos, real company branding, watermark, glowing human brain, humanoid robot, robot hand touching screen, sci-fi hologram, giant "AI" lettering, neon cyberpunk city, excessive particles, futuristic tunnel, Matrix-style falling code, cliché AI imagery, human faces, identifiable people, testimonial imagery, review stars, award badges, "No.1" text, exaggerated lens flare, overly saturated neon colors
```

【alt方針】
`alt=""`(装飾画像として扱う)
(本画像はINSIGHTセクションの背景装飾であり、隣接するHTMLコピー(見出し・本文)で内容は完結している。画像自体に意味のある情報を依存させない設計のため、使用する場合は`alt=""`+コンテナへの`aria-hidden="true"`を基本とする)

【Mobileでの扱い】
背景装飾として使用する場合、Mobileでは画像の一部が意図せず切り取られても違和感がないよう、中央〜左右いずれかに寄せた構図とする(テキストと重なる中央領域は避ける)。データ量を抑えるため、Mobileでは非表示にする、またはより小さいサイズで読み込む(`loading="lazy"`)ことを検討する。画像を使わずCSSのみで代替する場合、Mobileでの追加対応は不要。

---

## 3. IMAGE02(Premium Technology Workspace)について

**生成しない。** 理由は1章を参照。USE CASE(SECTION07)はbrowser-style card、SUPPORT(SECTION08)は放射状のsupport diagramとして、いずれもHTML/CSS/inline SVGで実装する方針が`06_design_guide.md`で既に確定しており、写真的な画像を追加する必要性は低いと判断した。

もし実装後のレビューで「USE CASEセクションの雰囲気が単調」等の課題が見つかった場合に限り、以下の条件で改めて検討する。
- 人物を使う場合も顔を主役にせず、hands/silhouette/back view程度に留める
- 実在企業ロゴ・読めるUIテキスト・数値指標は一切描写しない
- ファイル名候補: `nexora-workspace.webp`(16:9)

---

## 4. HTML/CSS/inline SVGで代替する要素(画像化しないもの)

以下は`06_design_guide.md`の設計に基づき、画像ではなくHTML/CSS/inline SVGで実装する。

| 要素 | 実装方法 | 理由 |
|---|---|---|
| HERO Dashboard mockup | HTML/CSS(glassmorphism panel + CSSグラデーション) | レスポンシブ対応、テキストの正確な管理、架空数値混入の防止(`06_design_guide.md`8章) |
| Floating status cards | HTML/CSS(position/backdrop-filter) | Dashboardと同期した状態管理、Mobileでの再配置が容易(9章) |
| HOW IT WORKS(Workflow visualization) | HTML/CSS + inline SVG(接続線) | ステップ数・ラベルの変更に強く、Mobileでの縦組み換えが容易(13章) |
| FEATURES(Bento Grid) | CSS Grid | カードサイズの調整、レスポンシブ時の1カラム化が容易(14章) |
| USE CASE(browser-style/workflow card) | HTML/CSS | 「例であること」のテキスト明示とUIバッジの組み合わせを正確に管理できる(16章) |
| SUPPORT(放射状ノード図) | HTML/CSS + inline SVG(接続線) | HERO Dashboardと異なるレイアウトを軽量に実現できる(17章) |
| アイコン全般 | inline SVG | 外部ライブラリ・画像ファイルへの依存を避け、色(currentColor)を柔軟に制御できる(6章のアイコン方針を踏襲) |

---

## 5. 禁止要素(画像を生成する場合の共通ルール)

いずれの画像にも、以下を一切含めない。

数字 / % / ROI / 売上 / 成果指標 / 成功率 / 顧客数 / 導入企業数 / 満足度 / 削減率 / 実績グラフ / 架空企業ロゴ / 実在企業ロゴ / 読めるUIテキスト / testimonial / review stars / awards / No.1表記

また、以下のような「AIっぽすぎる」紋切り型の表現も避ける。

glowing human brain / humanoid robot / robot hand touching screen / sci-fi hologram / giant "AI" lettering / neon cyberpunk city / excessive particles / futuristic tunnel / Matrix風コード / その他のcliché AI imagery

---

## STEP07自己チェック

- 画像点数: 最大1点(IMAGE01)、生成なし(0点)でも成立する設計とした
- IMAGE02は必要性を検討したうえで生成しないと判断し、理由を明記した
- HERO Dashboardは画像化せず、HTML/CSSで実装する方針を維持した
- 使用セクション・目的を明記した(IMAGE01: INSIGHT背景装飾、任意)
- 日本語プロンプト・英語プロンプトともに、subject/composition/lighting/background/mood/color/styleを含む文章形式で記載した
- Negative/Avoidを明記した(AIクリシェ表現・数値実績・実在ロゴ・文字情報を含む)
- 推奨ファイル名を設定した(`nexora-workflow.webp`)
- alt方針を設定した(装飾画像として`alt=""`+`aria-hidden="true"`)
- 画像内文字(ロゴ・数字・料金・評価等)は要求していない
- 実在ブランド・実在人物・実在製品UIを要求していない
- 料金・導入企業数・成功事例・顧客の声等の数値実績は、いずれの画像にも要求していない
- HTML/CSS/inline SVGで代替する要素を一覧化した(4章)
- STEP08(実装)には進んでいない
- `site/`は編集していない
