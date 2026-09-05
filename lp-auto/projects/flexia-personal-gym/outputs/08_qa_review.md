# FLEXIA Final QA Review

**実施方法について**: 本レビューは、`client-brief.md`・`outputs/01〜07`・`site/index.html`・`site/css/style.css`・`site/js/main.js`・`site/images/`のコード/テキストを静的に読み込み、内容照合・CSSカスケード計算・WCAGコントラスト計算(相対輝度式)・HTML構造解析によって行った。加えて、375px/390px/430pxを想定したMobile微調整(セクション間余白・APPROACH本文の折返し・PROBLEM見出しの改行・最終CTAの横padding二重加算解消等)を実施したうえで、**実ブラウザ(Chrome DevTools, 390px前後)での目視確認が完了**しており、その結果を本レポートに反映している。ファイルの修正は行っておらず、本ファイル(`outputs/08_qa_review.md`)のみを最新状態へ上書きした。

本レポートは、前回QA(HIGH0件・MEDIUM1件)で指摘した「`.section-light-alt`背景上のeyebrowコントラスト」への対応、およびその後のMobile実機確認に基づく複数の微調整を反映した**最終版**である。

---

## Summary

- CRITICAL: 0件
- HIGH: 0件
- MEDIUM: 0件
- LOW: 1件
- INFO: 4件

前回MEDIUM(M-1: `.section-light-alt`背景上のeyebrowコントラスト)は、該当箇所のみ`#2860EA`への個別調整により解消(`#2860EA` vs `#F4F6F8` = 4.906:1、WCAG AA適合)。CTAボタン(`#2B67F6`、白背景と4.802:1)・hover(`#1949CA`、7.376:1)は変更なく適合を維持。

Mobile実機確認(390px前後)で新たに判明していたセクション間余白・見出し改行・checklist折返し・最終CTAの横padding二重加算・CTA文言の2行化については、いずれもMobile専用CSS(および必要最小限のHTML調整)で解消済みであることを確認した。

CRITICAL・HIGH・MEDIUMともに0件で、公開前に必ず対応すべき問題は残っていない。

---

## CRITICAL

該当なし。架空の料金・実績・レビュー・資格・所在地・営業時間・支払方法・キャンセル規定・ビフォーアフター・医学的効果・結果保証・No.1表現・手ぶら保証・個別メニュー作成保証・申込み後の未確定フロー、いずれも`site/index.html`上に確認されなかった。

## HIGH

該当なし。

## MEDIUM

該当なし。

**前回MEDIUM(M-1: eyebrowコントラスト)の対応状況**: `.section-light-alt`(背景`#F4F6F8`)配下の`.eyebrow`のみ、`--color-accent`とは独立して`#2860EA`を指定。`#2860EA` vs `#F4F6F8` = **4.906:1**でWCAG AA(4.5:1)に適合することを再計算で確認。CTAボタン(`--color-accent: #2B67F6`、白背景と4.802:1)・hover(`--color-accent-hover: #1949CA`、7.376:1)は変更されておらず、引き続き適合。→ **解消**。

## LOW

### L-1. `outputs/05_lp_copy.md`冒頭のSTEP番号表記が工程定義と不一致(既知・未対応)

【対象箇所】`outputs/05_lp_copy.md` 3行目「HTML/CSS/JSの実装はSTEP06以降で行う。」

【現在の状態】正式な工程は「STEP07完了後にHTML/CSS/JS実装を行う」。`06_design_guide.md`は既に同種の誤りを修正済みだが、`05_lp_copy.md`の同種の記述は今回のタスク範囲外(`outputs/01〜07`変更禁止)のため引き続き未対応。site自体には影響しない。

【推奨修正】「HTML/CSS/JSの実装は、STEP07完了後の実装工程で行う。」等へ修正することを推奨(次回以降の対応候補)。

## INFO

### I-1. `outputs/07_image_prompts.md`内の`#2F6FFF`について

画像生成プロンプト文中(IMAGE01〜03の「光の色」指定)に旧色`#2F6FFF`が残っているが、CSSのUIカラートークンではなく生成済み画像の色指定という記述のため、UI上の問題ではない。今回のタスク範囲外のため未対応。

### I-2. Mobile微調整の内容(記録)

実ブラウザ確認(390px前後)を踏まえ、以下をMobile専用(`@media (max-width:767px)`)で調整済み。
- セクション間余白: `#problem`上下52px、`#why`下52px、`#service`上52px、`#approach`(ダーク)上下73px、`#counseling`下40px、`#faq`上40px(COUNSELING→FAQは128px相当→80px相当に改善)
- PROBLEM見出し: `<br class="sp-only">`により「こんな悩みは／ありませんか？」の自然な2行に固定(Desktop/Tabletは無効)
- PROBLEMチェックリスト: card左右padding・アイコンgapの縮小、および「作れない」を`nowrap-sp`で保護し不自然な分断を解消
- APPROACH本文: Mobileのみ`text-align:left`(見出し・eyebrowは中央揃えを維持)
- 最終CTA: `.section-final-cta`の横paddingが`.container`と二重加算されていた問題を解消し、`.final-cta`左右paddingを18pxへ調整。見出し・本文中の「無料カウンセリング」を`nowrap-sp`で保護。CTAボタンをMobile専用でwidth:100%・font-size 14px等に調整し1行表示を実現(実効コンテンツ幅: 375px≈299px/390px≈314px/430px≈354px)

いずれもDesktop(≥1024px)・Tablet(768〜1023px)のスタイルには影響しないことをセレクタのスコープ(`#approach.section-dark`のベース値・`@media (min-width:1024px)`ブロック等)から確認済み。

### I-3. コード上・実機で確認済みのPASS項目

- CSS brace balance 154/154、JS brace balance 8/8・括弧balance 31/31、HTMLタグバランス不整合なし。
- 画像3点(`flexia-hero.webp`・`flexia-benefit.webp`・`flexia-session.webp`)はいずれも`file`コマンドで実体がWebP(VP8 encoding)であることを確認。合計約280.8KB(旧PNG比約94.8%削減)。旧PNGファイル・旧PNG参照ともに0件、画像参照切れなし。
- `site/index.html`全文検索で「週2回から」「手ぶら」「No.1」「必ず痩せる」「絶対」「100%」「日程調整」「来店」「成功率」「継続率」「満足度」いずれも0件。
- Footerに「本サイトはポートフォリオ掲載を目的として制作した架空のサービスサイトです。実在する店舗・企業ではありません。」を確認。
- `outputs/05_lp_copy.md`(正本)と`site/index.html`の公開文言は、HERO・SECTION04・SECTION05・SECTION07・SECTION08・FAQ・最終CTAのすべてで差分0件(構造差分を除く)。
- **実ブラウザ(390px前後)での目視確認結果**: Hero・PROBLEM・APPROACH・WHY・SERVICE・COUNSELING・FAQ・最終CTA・Footer・CTA折返し・架空LP表記・横スクロールなし、いずれもPASS。

### I-4. 要目視確認事項(未確認のまま残る項目)

以下は今回の実機確認範囲に明示的に含まれていなかったため、根拠のないPASS扱いはしていない。

- 画像3点(WebP変換後)のテイスト・トーンがLP全体のデザインと視覚的に馴染んでいるか

---

## Copy Check

`outputs/05_lp_copy.md`を正本として`site/index.html`と比較した公開文言差分は、HERO・SECTION04・SECTION05・SECTION07・SECTION08・FAQ・最終CTAのすべてで**0件**(HTMLタグ・改行・アイコン等の構造差分、および今回のMobile専用`nowrap-sp`/`sp-only`スパン・br追加を除く)。内部制作メモの混入は確認されなかった。

## HTML Check

semantic HTML・見出し階層・id重複なし・href(内部アンカーのみ)・img src(3点とも実在)・タグバランス、いずれも問題なし。

## CSS Check

brace balance 154/154。Accent Blue関連はすべてWCAG AA適合(本文参照)。`--space-side`/`--space-section`のMobile/Tablet/Desktopカスケードは正常。Mobile専用の個別セクション調整(#problem/#why/#service/#approach/#counseling/#faq/.section-final-cta/.final-cta)はいずれも`max-width:767px`にスコープされ、Desktop/Tabletの表示に影響しない。横スクロール要因なし。

## JavaScript Check

brace balance 8/8、括弧balance 31/31。FAQ処理・reveal処理・`prefers-reduced-motion`対応、いずれも正常。外部ライブラリなし。

## Responsive Check

FV/SERVICE/BENEFIT/利用イメージ/FAQのカラム数分岐は仕様通り。Mobile専用の余白・改行・折返し調整により、390px前後での実機表示も良好であることを確認済み。画像参照エラーなし。

## Accessibility Check

コントラストはCTA・eyebrowともにWCAG AA適合。focus-visible・aria属性・keyboard操作・alt方針(装飾画像として統一)いずれも良好。

## Image Check

主要画像はhero/benefit/sessionの3点(WebP)のみ。実在ブランドロゴ・文字入り・ビフォーアフター・実績を示す画像なし。参照エラーなし。

## Performance Check

画像合計約280.8KB。loading/decoding属性を適切に設定。外部JSライブラリなし、自動再生・重いアニメーションなし。

## Final Verdict

CRITICAL・HIGH・MEDIUMすべて0件。残るLOW1件(`05_lp_copy.md`冒頭のSTEP番号表記、site非影響)とINFO4件(画像生成プロンプト内の旧色参照、Mobile微調整の記録、実機確認済みPASS項目一覧、画像トーンの視覚的馴染みのみ未確認)は、いずれも公開のブロッカーではない。実ブラウザ(390px前後)でのレイアウト・折返し・横スクロール・架空LP表記の確認も完了しており、**公開・commit可能な状態**と判断する。
