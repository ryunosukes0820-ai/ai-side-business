# FLEXIA Image Prompts

本文書は画像生成AIへ入力するためのプロンプト設計書である。**この工程では画像の生成そのものは行わない。** 画像は3点のみとし、STEP06(`06_design_guide.md`)で決定した構成・カラー・ブランド方向性に準拠する。

**共通ルール**: いずれの画像にも、ブランド名・キャッチコピー・CTA・数字・見出し等の文字は含めない(すべてHTML/CSS側で表示する)。実在するジム・トレーナー・企業・人物・店舗・ロゴは再現・模倣しない。

---

## IMAGE 01：FV Main Visual

【使用セクション】
SECTION01 ファーストビュー(右側)

【目的】
「都会的で静かな強さ」を一目で伝えるブランドビジュアル。左側のコピー・CTAと干渉しない、右寄りの主役配置とする。

【推奨ファイル名】
`flexia-hero.webp`

【推奨アスペクト比】
**4:5**(縦長)。PCのFV右カラムに収まりやすく、SPでも上部トリミングしやすい比率のため、4:5を最終推奨とする。

【構図】
フレーム右寄りに人物シルエットを配置し、左側〜中央に十分な余白(ネガティブスペース)を残す。人物は正面ではなくやや斜め・後ろ姿寄りの角度で、動きの一瞬(腕を上げる、体を捻る等)を切り取る。顔は明確に描写しない、または画角外・影の中に収める。

【被写体】
25〜39歳程度の会社員男性を想起させる、自然で健康的な体型のシルエット(過度な筋肉表現・ボディビル体型は避ける)。トレーニングウェアはブランドロゴなしの無地。

【背景】
Primary Dark(`#14171C`)を基調としたダークニュートラルな空間。具体的な店舗内装・設備は描写しない(抽象的な暗い空間・グラデーションのみ)。

【光・ライティング】
コントラストの高い、絞り込んだ単一光源(リムライト/サイドライト)。赤や強いネオンではなく、Accent Blue(`#2F6FFF`)の光を輪郭やジオメトリックなライン状に添える。

【カラートーン】
黒〜チャコールを基調とし、Accent Blueを差し色として一箇所〜数箇所に配置。彩度は全体的に抑えめ。

【スタイル】
Premium commercial photography、Cinematic、Minimal、Editorial。写実的すぎる広告写真ではなく、ブランドビジュアルとしての抽象度を残す。

【日本語プロンプト】
```
都会的でミニマルなパーソナルジムのブランドビジュアル。フレーム右側に、25〜39歳程度の会社員男性を想起させる自然な体型の男性シルエットを配置し、やや斜め後ろから、腕を上げる・体を捻るなど一瞬の動きを捉えた構図。顔ははっきり見せず、影または画角外に収める。左側から中央にかけては何もない暗い余白を大きく残す。背景はチャコールブラック(#14171C)を基調とした抽象的な暗い空間で、具体的な店舗設備は描写しない。単一光源によるリムライトで輪郭を強調し、鮮やかなブルー(#2F6FFF)の光を輪郭線または細いジオメトリックなラインとして添える。全体的に彩度を抑えたシネマティックで高級感のあるトーン。ミニマルで洗練された、広告写真というよりブランドビジュアルとしての一枚。文字・ロゴ・ウォーターマークは一切含めない。
```

【English Prompt】
```
A minimal, urban brand visual for a premium personal training gym. Compose a male silhouette on the right side of the frame, suggesting a professional man in his late 20s to 30s with a natural, healthy build (not a bodybuilder physique), captured mid-motion from a slight rear/side angle — an arm raised or torso twisting. The face is not clearly visible, kept in shadow or just outside the frame. Leave a large empty negative space from the center to the left of the frame. Background is an abstract dark charcoal-black (#14171C) space with no specific gym equipment or interior details. Use a single rim/side light source to define the silhouette's edge, with a vivid blue (#2F6FFF) light accent forming a thin edge glow or subtle geometric line. Desaturated, cinematic color grading with a premium, quiet-strength mood. Style: minimal, editorial, premium commercial photography, more of a brand visual than a literal advertising photo. No text, no logos, no watermarks.
```

【Avoid / Negative】
```
text, typography, letters, logo, watermark, brand marks, visible face / identifiable facial features, distorted hands, extra fingers, malformed anatomy, exaggerated muscles, bodybuilder physique, before and after comparison, extreme weight loss imagery, red aggressive gym lighting, neon overload, real company branding, identifiable real people, medical imagery, cheap commercial stock-photo look, gym equipment logos, visible interior signage
```

【alt候補】
`alt=""`(装飾画像として扱う)
(STEP08 QAでの再検討の結果、本画像は隣接するHTMLコピー(ブランド名・メインコピー・サブコピー等)で内容がすでに伝わっており、画像自体は雰囲気を補助する装飾要素と判断した。HTMLコピーと内容が重複する装飾画像のため、実装時はalt=""+コンテナへのaria-hidden="true"を推奨する)

---

## IMAGE 02：Benefit Visual

【使用セクション】
SECTION06 目指せる状態・ベネフィット

【目的】
筋肉や減量結果を見せるのではなく、「忙しい生活の中に運動を取り入れ、前向きなリズムを整えていく」という状態を静かに表現する。

【推奨ファイル名】
`flexia-benefit.webp`

【推奨アスペクト比】
**1:1**(正方形)。IMAGE01(縦長)とは異なる比率にすることで、セクションごとの視覚的リズムをつける。

【構図】
仕事と運動の両立を想起させる、日常の一場面の抽象的な切り取り。人物を使う場合は全身を写さず、上半身の一部や手元、後ろ姿など部分的な描写に留める。中央〜片側に主題を置き、残りは余白で構成する。

【被写体】
候補A(人物あり): スポーツバッグやシューズを持つ、または羽織る動作の一部(手・肩・背中など)。候補B(人物なし): 整えられたスポーツバッグ・シューズ・タオルなど、生活と運動の両立を示す静物。**briefにない店舗設備やロッカールーム等の具体的な空間は作り込まない。**

【背景】
Background Light(`#FFFFFF`)またはごく淡いグレーを基調とした、明るくクリーンな空間。装飾を最小限にする。

【光・ライティング】
自然光を想起させる柔らかい順光〜サイドライト。強いコントラストは避け、明るく清潔感のある印象にする。

【カラートーン】
白を基調に、Accent Blueを小物(バッグの一部やライン等)にごく控えめに配置してもよい。

【スタイル】
Minimal editorial photography、Clean lifestyle visual、Premium commercial photography。

【日本語プロンプト】
```
忙しい生活の中に運動を取り入れる落ち着いたライフスタイルを表現する、ミニマルなビジュアル。人物を描く場合は全身や顔を見せず、スポーツバッグを肩にかける手元や、シューズを整える後ろ姿など、身体の一部分だけを自然光の中で捉える。人物を描かない場合は、整えられたスポーツバッグ・シューズ・タオルなどを、生活感のある明るい空間に静かに配置した静物として構成する。背景は白またはごく淡いグレーを基調とした、装飾の少ないクリーンな空間。柔らかい自然光による順光〜サイドライトで、清潔感と落ち着いた前向きさを表現する。色数を抑え、必要であれば鮮やかなブルー(#2F6FFF)を小物の一部にごくわずかに差し色として使う程度に留める。過度な身体変化や筋肉、ビフォーアフターを連想させる要素は一切含めない。文字・ロゴ・ウォーターマークは含めない。
```

【English Prompt】
```
A minimal lifestyle visual representing a calm, sustainable way of bringing exercise into a busy professional life. If a person is included, avoid showing the full body or face — instead capture a partial, natural-light moment such as a hand adjusting a gym bag strap or feet slipping into sport shoes from behind. Alternatively, compose it as a still life of neatly arranged gym essentials (a sports bag, shoes, a towel) in a bright, everyday space. Background is white or a very light neutral gray, clean and minimally decorated. Soft, natural front or side lighting conveys a fresh, quietly positive mood. Keep the palette restrained, with an optional subtle accent of vivid blue (#2F6FFF) on a small detail only. Do not include any imagery suggesting dramatic body transformation, exaggerated muscles, or before/after comparisons. No text, no logos, no watermarks.
```

【Avoid / Negative】
```
text, typography, letters, logo, watermark, brand marks, visible face (if person used), distorted hands, extra fingers, malformed anatomy, exaggerated muscles, bodybuilder physique, before and after comparison, extreme weight loss imagery, specific gym interior / locker room details, real company branding, identifiable real people, medical imagery, cheap commercial stock-photo look
```

【alt候補】
`alt=""`(装飾画像として扱う)
(STEP08 QAでの再検討の結果、本画像も隣接するHTMLコピー(SECTION06の見出し・本文・リスト)で内容がすでに伝わっており、装飾画像と判断した。HTMLコピーと内容が重複する装飾画像のため、実装時はalt=""+コンテナへのaria-hidden="true"を推奨する)

---

## IMAGE 03：Usage Image Visual

【使用セクション】
SECTION07 利用イメージ / トレーニングの流れ

【目的】
「完全マンツーマン」「1回60分」「仕事帰りの利用」という雰囲気を視覚的に補助する。具体的なセッション手順や店舗設備を事実として描写しない。

【推奨ファイル名】
`flexia-session.webp`

【推奨アスペクト比】
**16:9**(横長)。テキストと横並びになるセクションレイアウトに合わせ、横長構図を推奨する。

【構図】
2人のシルエット、または手元・トレーニング動作の一部を切り取った構図。マンツーマンであることが伝わるよう、2つの人影(トレーナーと利用者を想起させる)を近い距離感で配置するが、顔や個人が特定できる特徴は描かない。

【被写体】
候補A: 向き合う、または隣に並ぶ2人の抽象的なシルエット(トレーナーと利用者を想起させる)。候補B: トレーニング動作の一部(手元でのフォーム確認、ストレッチの補助など)のクローズアップ。**特定の器具・特定のブランドのマシンは詳細に描写しない。**

【背景】
Background LightまたはPrimary Darkのいずれか、他セクションとのコントラストを考慮して設定可(推奨: Light基調で明るく開放的な印象)。具体的な店舗内装は作り込まない。

【光・ライティング】
柔らかく均一な光。緊張感や苦痛を強調するような強いコントラスト・汗の強調は避ける。

【カラートーン】
白〜ライトグレーを基調とし、必要に応じてAccent Blueを控えめに使用。

【スタイル】
Minimal editorial photography、Premium commercial photography、Abstract sports visual。

【日本語プロンプト】
```
完全マンツーマンのパーソナルトレーニングの雰囲気を伝える、横長のミニマルなビジュアル。2人の人物のシルエット(トレーナーと利用者を想起させる)が近い距離感で向き合う、または並ぶ構図とし、顔や個人が特定できる特徴は描かない。あるいは、フォームを確認する手元やストレッチを補助する動作の一部だけをクローズアップで捉えてもよい。特定のトレーニング器具やブランドのマシンは詳細に描写しない。背景は明るくクリーンな空間を基調とし、具体的な店舗内装は作り込まない。柔らかく均一な光で、緊張感や苦痛、汗を強調しない、落ち着いた雰囲気にする。白を基調とした色調に、必要であれば鮮やかなブルー(#2F6FFF)を控えめに添える程度に留める。過度な筋肉表現やビフォーアフターを想起させる要素は含めない。文字・ロゴ・ウォーターマークは含めない。
```

【English Prompt】
```
A minimal, horizontal visual conveying the feeling of a fully one-on-one personal training session. Compose two human silhouettes — suggesting a trainer and a client — positioned close together, either facing one another or standing side by side, with no identifiable facial features. Alternatively, focus on a close-up of a partial gesture, such as hands adjusting form or assisting a stretch. Avoid detailing any specific training equipment or branded machines. Background is a bright, clean space without a specific gym interior being fully depicted. Use soft, even lighting that avoids tension, strain, or visible sweat — keep the mood calm and composed. Palette is white-based with an optional subtle accent of vivid blue (#2F6FFF). Do not include exaggerated muscles or any before/after implication. No text, no logos, no watermarks.
```

【Avoid / Negative】
```
text, typography, letters, logo, watermark, brand marks, visible/identifiable faces, distorted hands, extra fingers, malformed anatomy, exaggerated muscles, bodybuilder physique, before and after comparison, extreme weight loss imagery, red aggressive gym lighting, neon overload, specific branded gym equipment, real company branding, identifiable real people, medical imagery, strained/painful facial expression, visible sweat emphasis, cheap commercial stock-photo look
```

【alt候補】
`alt=""`(装飾画像として扱う)
(STEP08 QAでの再検討の結果、本画像も隣接するHTMLコピー(SECTION07の見出し・本文・ポイントリスト)で内容がすでに伝わっており、装飾画像と判断した。HTMLコピーと内容が重複する装飾画像のため、実装時はalt=""+コンテナへのaria-hidden="true"を推奨する)

---

## 画像ファイル仕様(後工程向け)

| 項目 | 推奨仕様 |
|---|---|
| フォーマット | WebP(フォールバックが必要な場合はJPEGを併用) |
| 元画像サイズ(Retina考慮) | 表示幅の2倍を目安に書き出す。例: 表示幅600pxなら1200px幅で書き出す |
| IMAGE01表示サイズ目安 | PC: 幅 約520px(FV右カラム) / SP: 幅100%、高さを抑えたトリミング |
| IMAGE02表示サイズ目安 | PC: 幅 約480px(SECTION06左カラム) / SP: 幅100% |
| IMAGE03表示サイズ目安 | PC: 幅 約560px(SECTION07右カラム) / SP: 幅100% |
| object-fit | `cover`(すべての画像) |
| object-position | IMAGE01は`right center`(主題が右寄りのため)、IMAGE02・03は`center` |
| lazy-loading | IMAGE02・IMAGE03は`loading="lazy"`を適用 |
| FV画像(IMAGE01)のみ | ファーストビュー内で即時表示させるため`loading="eager"`(または`fetchpriority="high"`)を検討する |

## 画像とHTMLコピーの役割分担

3点の画像はいずれも、ブランド名・キャッチコピー・CTA・特徴・数字・見出しといった情報を担わない。これらはすべてHTML/CSS側でテキストとして表示する。画像はあくまで「雰囲気・ブランド価値・状態理解」を補助する視覚要素として設計している。

## STEP07自己チェック

- 画像数: 3点のみ(IMAGE01〜03)、追加していない
- STEP06のデザイン仕様(カラー・コンセプト・セクション対応)と一致
- 各画像の用途(使用セクション・目的)を明記
- 日本語プロンプト・英語プロンプトともに、subject/composition/lighting/background/mood/color/styleを含む文章形式で記載
- Negative/Avoidをすべての画像に明記(人物関連negativeは各画像の文脈に合わせて調整)
- 推奨ファイル名をすべて設定(`flexia-hero.webp` / `flexia-benefit.webp` / `flexia-session.webp`)
- alt方針をすべて設定(STEP08 QAでの再検討により、隣接するHTMLコピーと内容が重複する装飾画像として`alt=""`+`aria-hidden="true"`に統一)
- 画像内文字(ロゴ・コピー・数字等)は要求していない
- 実在ブランド・実在人物・実在店舗を要求していない
- 架空の店舗設備・具体的なトレーニング手順を事実として作り込んでいない
- 過度な筋肉表現・ビフォーアフター・医学的効果表現は明示的にAvoidに含め、プロンプト本文にも記載していない
- STEP08(実装)には進んでいない
- `site/`は編集していない
