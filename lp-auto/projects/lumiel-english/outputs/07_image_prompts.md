# LUMIEL ENGLISH Image Prompts

本文書は画像生成AIへ入力するためのプロンプト設計書である。**この工程では画像の生成そのものは行わない。** 画像は2点のみとし、STEP06(`06_design_guide.md`)で決定した構成・カラー・ブランド方向性に準拠する。

**共通ルール**: いずれの画像にも、ブランド名・キャッチコピー・CTA・数字・料金・評価・UIラベル等の文字は含めない(すべてHTML/CSS側で表示する)。実在する企業・サービス・人物・ロゴは再現・模倣しない。FLEXIA案件(黒背景・暗い照明・ストイック)とは完全に異なる、明るく自然光を基調としたトーンで統一する。

---

## IMAGE 01：HERO Main Visual

【使用セクション】
SECTION01 ファーストビュー(右側)

【目的】
「仕事で忙しい社会人でも、自宅から気軽にオンライン英会話を始められそう」という第一印象を作るブランドビジュアル。左側のコピー・CTAと干渉しない構図とする。

【推奨ファイル名】
`lumiel-hero.webp`

【推奨アスペクト比】
**4:5**(縦長)。Desktop HERO右カラムに収まりやすく、Mobileでも人物の顔・PC・上半身が自然にクロップできる比率のため。

【被写体】
25〜39歳程度の、日本人または東アジア系の社会人を想起させる成人1名。性別は限定しない。オフィスカジュアル、または清潔感のあるシンプルな私服(スーツ姿には限定しない)。

【構図】
人物は中央〜やや右寄りに配置し、左側には十分な余白を残す(HTML側でコピーを重ねる想定のため、画像内に大きな文字は入れない)。明るく整理された自宅またはワークスペースで、デスクのノートPCに向かいイヤホン等を使用し、オンラインで会話している自然な様子。過度にカメラ目線にしすぎない。PC画面は、シンプルなビデオ通話風・ぼかした人物・抽象的な画面程度に留め、細かい架空UI・文字・料金・講師プロフィールなどは表示しない。

【背景】
ホワイト〜淡いブルーを基調とした明るい空間。小さな観葉植物やデスク周辺のシンプルな小物程度の装飾に留め、過度な装飾は避ける。

【光・ライティング】
朝〜昼の自然光を想起させる、明るく柔らかい光。高コントラストな演出、強いネオンや暗い照明は使用しない。

【カラートーン】
白・ライトブルー・淡いグレーを基調とし、ネイビーを少量。オレンジまたはイエローを小物にごく控えめなアクセントとして使用してもよい。Primary Blue(`#245DEB`)とLP全体のトーンに馴染む配色にする。

【スタイル】
Natural lifestyle photography、Bright and clean、Editorial。過度なストックフォト感・広告的な作り込みを避け、自然な日常の一場面として見せる。

【日本語プロンプト】
```
明るく清潔感のあるオンライン英会話のブランドビジュアル。フレーム中央からやや右寄りに、25〜39歳程度の日本人または東アジア系の社会人を想起させる成人1名を配置する。オフィスカジュアル、または清潔感のあるシンプルな私服(スーツに限定しない)。明るく整理された自宅またはワークスペースで、デスクの上のノートPCに向かい、イヤホンを着けてオンラインで会話をしている自然な様子。カメラ目線を強調しすぎない、リラックスした表情。PC画面はぼかした人物やシンプルなビデオ通話風の抽象的な表示に留め、文字・数字・料金・プロフィールなどは描写しない。左側には人物にかからない余白を大きく残す。背景はホワイトから淡いブルーを基調とした明るい空間で、観葉植物やシンプルな小物を控えめに配置してもよい。朝から昼の自然光を思わせる、柔らかく明るい光。色数を抑え、ネイビーやオレンジ・イエローはごく小さなアクセントに留める。全体的に自然で親しみやすい、広告的すぎないライフスタイル写真のトーン。文字・ロゴ・ウォーターマーク・UIラベルは一切含めない。
```

【English Prompt】
```
A bright, clean lifestyle photograph for an online English conversation brand. Compose one adult, suggesting a Japanese or East Asian professional in their late 20s to 30s, positioned center-to-right of the frame. Business-casual attire or simple, clean everyday clothing (not limited to a suit). The setting is a bright, tidy home or workspace, with the person sitting at a desk in front of a laptop, wearing earphones, naturally engaged in an online conversation. Avoid an overly direct, posed gaze at the camera — keep the expression relaxed and natural. The laptop screen should show only a blurred figure or an abstract video-call-style interface — no visible text, numbers, pricing, or profile details. Leave generous empty space on the left side of the frame for overlaid copy. Background is a bright space in white to pale blue tones, with an optional small houseplant or simple desk accessories kept minimal. Lighting is soft, bright, morning-to-midday natural light — avoid harsh contrast, neon, or dim lighting. Keep the palette restrained: white, light blue, soft gray, with a touch of navy and an optional subtle orange or yellow accent on a small object. Style: natural lifestyle photography, bright and clean, editorial — not an overly staged stock-photo look. No text, no logos, no watermarks, no UI labels.
```

【Avoid / Negative】
```
text, typography, letters, numbers, logo, watermark, UI labels, pricing display, star ratings, reviews, distorted hands, extra fingers, malformed anatomy, unnatural laptop-typing posture, exaggerated toothy advertising smile, obvious stock-photo posing, children, school uniform, classroom with whiteboard, teacher lecturing, group lesson with multiple students, dark moody lighting, neon lighting, black background, luxury hotel atmosphere, aggressive or overly masculine styling, cheap commercial stock-photo look, real company branding, identifiable real people
```

【alt候補】
`alt=""`(装飾画像として扱うことを基本候補とする)
(本画像はFVの雰囲気補助が目的であり、隣接するHTMLコピー(ブランド名・メインコピー・サブコピー・補足コピー)でサービス内容はすでに伝わっている。画像自体に本文にない重要情報を依存させない設計のため、実装時は`alt=""`+コンテナへの`aria-hidden="true"`を基本候補とする。ただし実装時に画像の役割が変わる場合は、内容を簡潔に説明するalt(例:「オンライン英会話レッスンを受ける人物のイメージ」)への変更を検討する)

---

## IMAGE 02：Service / Usage Style Visual

【使用セクション】
SECTION05「LUMIEL ENGLISHの受講スタイル」

【目的】
1回25分・オンライン完結・PC/スマートフォン対応という受講スタイルを視覚的に補助する。IMAGE01が「人物主体」であるのに対し、本画像は「デスク・デバイス・学習環境主体」として役割を分ける。

【推奨ファイル名】
`lumiel-service.webp`

【推奨アスペクト比】
**16:9**(横長)。テキストと横並びになるセクションレイアウトに合わせる。

【構図】
ノートPCとスマートフォンが並んだ明るいデスク環境を中心とした構図。候補としてノート・イヤホン・飲み物などを添えてもよい。人物を入れる場合は手元や後ろ姿など部分的な描写に留め、IMAGE01とは異なるアングル・構図にする(全身・顔を強調しない)。PC・スマートフォンの画面には、料金・講師プロフィール・評価・星・予約時間・24時間表記・チャット内容・教材名・成績・スコアなど、いかなる文字情報・数値も表示しない。画面は抽象的な光の反射や、ぼかしたビデオ通話風の表示など最小限の描写に留める。

【被写体】
候補A(人物なし): ノートPC・スマートフォン・ノート・イヤホン・飲み物などを整えて配置した、学習環境の静物構成。候補B(人物あり): デスクに向かう手元やノートPCを操作する部分的な動作(顔全体は写さない)。

【背景】
明るいデスク環境、白〜淡いブルー・淡いグレーを基調とした空間。具体的な店舗・教室設備は描写しない(オンライン完結のサービスのため)。

【光・ライティング】
IMAGE01と同様、朝〜昼の自然光を想起させる柔らかく明るい光。

【カラートーン】
白・ライトブルー・淡いグレーを基調とし、ネイビーを少量。オレンジまたはイエローを小物(ノートの表紙、マグカップ等)にごく控えめに使用してよい。

【スタイル】
Minimal lifestyle photography、Clean desk setup、Natural light、Editorial。

【日本語プロンプト】
```
オンライン英会話の受講スタイルを伝える、明るく清潔感のある横長のライフスタイルビジュアル。ノートPCとスマートフォンが並んだ、整理された明るいデスクを中心に構成する。ノート、イヤホン、飲み物などを添えてもよい。人物を描く場合は、全身や顔を見せず、デスクに向かう手元やノートPCを操作する動作の一部だけを自然光の中で捉える。ノートPC・スマートフォンの画面には、文字・数字・料金・評価・星・時間表示・チャット内容・教材名などを一切表示せず、ぼかしたビデオ通話風の抽象的な表示や、光の反射程度に留める。背景は白から淡いブルー、淡いグレーを基調とした明るい空間で、具体的な教室や店舗の設備は描写しない。朝から昼の柔らかい自然光で、清潔感と落ち着いた前向きさを表現する。色数を抑え、ネイビーやオレンジ・イエローは小物の一部にごくわずかな差し色として使う程度に留める。文字・ロゴ・ウォーターマークは一切含めない。
```

【English Prompt】
```
A bright, clean, horizontal lifestyle visual conveying the online lesson experience of an English conversation service. Compose a tidy, well-lit desk setup featuring a laptop and a smartphone side by side, optionally with a notebook, earphones, or a beverage. If a person is included, avoid showing the full body or face — instead capture a partial, natural-light moment such as hands typing on the laptop or adjusting the phone. The laptop and smartphone screens must not display any text, numbers, pricing, ratings, stars, time schedules, chat content, or material names — keep the screens abstract, such as a blurred video-call interface or a soft light reflection. Background is a bright space in white, pale blue, and soft gray tones, with no specific classroom or storefront details depicted. Soft, natural morning-to-midday light conveys a clean, quietly positive mood. Keep the palette restrained, with navy and an optional subtle accent of orange or yellow on a small object only. No text, no logos, no watermarks.
```

【Avoid / Negative】
```
text, typography, letters, numbers, logo, watermark, UI labels, pricing display, star ratings, reviews, instructor profile, chat bubbles with readable text, distorted hands, extra fingers, malformed anatomy, visible face (if person used), children, school uniform, classroom with whiteboard, teacher lecturing, group lesson with multiple students, dark moody lighting, neon lighting, black background, luxury hotel atmosphere, cheap commercial stock-photo look, real company branding, identifiable real people, real app UI reproduction
```

【alt候補】
`alt=""`(装飾画像として扱うことを基本候補とする)
(本画像もSECTION05の本文(オンライン完結・PC/スマホ対応・予約制・1回25分・フィードバック)で内容がすでに説明されており、雰囲気補助が目的の装飾画像と判断する。実装時は`alt=""`+コンテナへの`aria-hidden="true"`を基本候補とする。画像に本文にない情報を依存させる設計は避ける)

---

## 画像ファイル仕様(後工程向け)

| 項目 | 推奨仕様 |
|---|---|
| フォーマット | WebP(最終生成時にWebPへ最適化する前提) |
| 元画像サイズ(Retina考慮) | 表示幅の2倍を目安に書き出す |
| IMAGE01表示サイズ目安 | PC: FV右カラム幅に収まるサイズ / SP: 幅100%、高さを抑えたトリミング |
| IMAGE02表示サイズ目安 | PC: SECTION05片カラム幅 / SP: 幅100% |
| object-fit | `cover`(両画像) |
| object-position | IMAGE01は人物の位置に応じて実装時に微調整、IMAGE02は`center` |
| lazy-loading | IMAGE02は`loading="lazy"` |
| IMAGE01(FV画像)のみ | ファーストビュー内で即時表示させるため`loading`属性なし(デフォルトeager)、必要に応じて`fetchpriority="high"` |

### Desktopでのトリミング方針

- IMAGE01: 4:5比率のままFV右カラムに配置。人物が中央〜やや右寄りに来るよう、object-positionは右寄り(例: 65%前後)を基本候補とする
- IMAGE02: 16:9比率のままSECTION05の片カラムに配置。中央基準のcoverで大きな破綻は生じない構図とする

### Mobileでのトリミング方針

- IMAGE01: 4:5比率を維持しつつ、幅100%で表示。縦横比を保ったまま人物の顔・PC・上半身が収まるよう、object-positionを実装時に微調整する(FLEXIA案件のhero画像と同様、コンテナのaspect-ratioを画像比率にできるだけ近づけることでクロップを最小化する方針を踏襲する)
- IMAGE02: 16:9比率を維持しつつ、幅100%で表示。横長画像のため、Mobileでも大きな破綻は生じにくい

## 画像とHTMLコピーの役割分担

2点の画像はいずれも、ブランド名・キャッチコピー・CTA・特徴・数字・見出しといった情報を担わない。これらはすべてHTML/CSS側でテキストとして表示する。画像はあくまで「雰囲気・親しみやすさ・受講イメージの理解補助」として設計している。

## STEP07自己チェック

- 画像数: 2点のみ(IMAGE01〜02)、不要に増やしていない
- STEP06のデザイン仕様(カラー・コンセプト・セクション対応)と一致
- 各画像の用途(使用セクション・目的)を明記
- 日本語プロンプト・英語プロンプトともに、subject/composition/lighting/background/mood/color/styleを含む文章形式で記載
- Negative/Avoidをすべての画像に明記
- 推奨ファイル名をすべて設定(`lumiel-hero.webp` / `lumiel-service.webp`)
- alt方針をすべて設定(隣接するHTMLコピーと内容が重複する装飾画像として`alt=""`+`aria-hidden="true"`を基本候補とし、画像に情報を依存させる設計は避けた)
- 画像内文字(ロゴ・コピー・数字・料金・評価等)は要求していない
- 実在ブランド・実在人物・実在店舗・実在アプリUIを要求していない
- 料金・利用者数・満足度・継続率・実績数・星評価・口コミ・講師人数・講師国籍・資格・受賞・No.1・成功率・TOEICスコア・Before/After・24時間・予約可能時間・架空レビュー・存在しない教材・架空のブランド提携ロゴは、いずれの画像にも要求していない
- グループレッスン・学校の教室風景・教師がホワイトボードの前に立つ構図は要求していない(マンツーマンサービスのため)
- FLEXIA案件(黒背景・暗い照明・ストイック)とは明確に異なる、明るい自然光基調のトーンで統一した
- STEP08(実装)には進んでいない
- `site/`は編集していない
