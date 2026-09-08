# LUMIEL ENGLISH Final QA Review

**実施方法について**: 本レビューは、`client-brief.md`・`outputs/01〜07`・`site/index.html`・`site/css/style.css`・`site/js/main.js`・`site/images/`のコード/テキストを静的に読み込み、内容照合・CSSカスケード計算・WCAGコントラスト計算(相対輝度式)・HTML構造解析によって行った。PC版および390px前後のMobileは、ユーザー自身による実ブラウザ目視確認でPASSが報告されている。1440/1024/768/430/375pxについては、本レビューではCSSのボックスモデル・文字数×フォントサイズの計算により確認しており、実ブラウザでのスクリーンショット確認ではない。ファイルの修正は行っておらず、`outputs/08_qa_review.md`のみを最新状態へ上書きした。

本レポートは、前回QA(CRITICAL0/HIGH0/MEDIUM0/LOW2)で指摘した`05_lp_copy.md`とsiteの同期漏れ2件(SECTION03視覚要素・SECTION06箇条書き)への対応を反映した**最終版**である。

---

## Summary

- CRITICAL: 0件
- HIGH: 0件
- MEDIUM: 0件
- LOW: 0件
- INFO: 4件

client-brief.mdに存在しない事実(料金・講師人数・講師国籍・利用者数・満足度・継続率・実績数・口コミ・資格・受賞歴・No.1・成功率・TOEICスコア・Before/After・24時間・いつでも予約・好きな時間に受講・自分の都合に合わせて・勧誘なし・効果保証・必ず話せる・必ず上達する・絶対・100%・最短○日)は、`site/index.html`にも`outputs/05_lp_copy.md`の公開コピー本文にも**一切確認されなかった**(いずれも「実案件では追加確認が必要な情報」等の明示的な除外セクション内の記載のみ)。前回LOWだった2件の同期漏れは解消済み。

---

## CRITICAL

該当なし。

## HIGH

該当なし。

## MEDIUM

該当なし。

## LOW

該当なし。

**前回LOW(L-1・L-2)の対応状況**:
- L-1(SECTION03「25 MINUTES」視覚要素の未記載): `outputs/05_lp_copy.md`のSECTION03に【視覚要素】として「25 MINUTES(確定情報「1回25分」の視覚的再掲。新しい事実ではない)」を追記し、siteとの表記を完全一致させた。→ **解消**
- L-2(SECTION06の4項目リスト未記載): `outputs/05_lp_copy.md`のSECTION06に【箇条書き】として、site/index.htmlの`.support-list`4項目(初心者向けのサービス設計/マンツーマンで自分のペースに合わせやすい/日本語での学習サポート/レッスン後の簡単なフィードバック)をそのまま追記し、文言を完全一致させた。→ **解消**

## INFO

### I-1. コード上で確認済みのPASS項目

- CTA文言「無料体験レッスンを予約する」がHERO・BENEFITS直後・FINAL CTAの3箇所で完全一致し、すべて`href="#free-trial"`。FREE TRIAL・SERVICE・BEGINNER SUPPORT・FAQに追加CTAはない。
- FAQ6問すべてが`aria-expanded="false"`で初期化され、クリックで開閉・再クリックで閉じる・`aria-expanded`更新の実装を確認。`aria-controls`・`aria-labelledby`・`role="region"`・`<button type="button">`もすべて6件ずつ設定済み。
- HTML要素のid重複なし(27個すべて一意)、見出し階層はh1→h2→h3の順で崩れなし。`site/css/style.css`のbrace balance 132/132、`site/js/main.js`のbrace balance 8/8・括弧balance 31/31、HTMLタグバランスも不整合なし。
- `--space-side`/`--space-section`は`:root`のデフォルトがSP値になっており、768px以上でtablet値、1024px以上でpc値に正しく切り替わる。`.section-final-cta`も横paddingを持たず`.container`に委ねる設計で、FLEXIA案件で発生した不具合はいずれも再発していない。
- 画像2点(`lumiel-hero.webp`1122×1402、`lumiel-service.webp`1672×941)は実体WebPを確認、デザイン仕様のアスペクト比(4:5・16:9)と一致。`alt=""`+`aria-hidden="true"`、loading/decoding属性も仕様通り。
- アクセシビリティ: Primary(`#245DEB`)・Hover(`#1D4ABC`)・Text(`#1E293B`)・Sub Text(`#5F6F86`)は、白背景・Sub Background(`#F5F9FF`)・Navy背景いずれの組み合わせでもWCAG AA(4.5:1)に適合(5.1〜16.0:1の範囲)。focus-visible、44px以上のタップ領域、`prefers-reduced-motion`対応も実装済み。
- Footerに「本サイトはポートフォリオ掲載を目的とした自主制作・架空のオンライン英会話サービスです。実在する企業・サービスではありません。」を確認(十分なサイズで表示、非表示・極端な縮小なし)。

### I-2. コピー整合性チェック結果(最終)

`outputs/05_lp_copy.md`を正本として`site/index.html`と比較した結果、HERO・PROBLEM・APPROACH・BENEFITS・SERVICE・BEGINNER SUPPORT・FREE TRIAL・FAQ・FINAL CTA・Footerのすべてで、HTML構造上の改行(`<br>`・`sp-only`・`nowrap-sp`)を除く**公開文言の差分は0件**。SECTION03の視覚要素、SECTION06の4項目リストも含め、site側にのみ存在していた要素はすべて05側に反映され、完全に同期した。

### I-3. 表現リスクチェック結果

「続けやすい」「取り入れやすい」「自分のペース」「少しずつ会話に慣れていける環境です」について、client-brief.mdの確定特徴(1回25分・マンツーマン・オンライン完結・日本語サポート・レッスン後フィードバック・予約制)から合理的に説明できる範囲であることを再確認した。いずれも「〜しやすい」「〜な環境です」というサービス設計の記述にとどまり、結果保証には拡張されていない。

### I-4. 実ブラウザ確認範囲についての申し送り(非ブロッキング)

1440px・1024px・768px・430px・375pxは、本レビューではCSSのボックスモデルおよび文字数×フォントサイズによる計算確認にとどまる(実ブラウザでのスクリーンショット未確認)。PC版・390px前後は実ブラウザでPASS報告済み。可能であれば残りの幅も実機で確認することを推奨するが、計算上は横スクロール・見出し破綻・CTA切れのいずれも発生しない見込みであり、公開のブロッカーではない。

---

## Copy Check

`outputs/05_lp_copy.md`と`site/index.html`の比較(公開される文字列のみを基準)。

| セクション | 判定 |
|---|---|
| HERO | 差分0件 |
| PROBLEM | 差分0件 |
| APPROACH | 差分0件(視覚要素「25 MINUTES」を05に追記済み) |
| BENEFITS | 差分0件 |
| SERVICE | 差分0件 |
| BEGINNER SUPPORT | 差分0件(4項目リストを05に追記済み) |
| FREE TRIAL | 差分0件 |
| FAQ | 差分0件 |
| FINAL CTA | 差分0件 |
| Footer | 差分0件 |

内部制作メモの混入は確認されなかった。

## 事実・捏造チェック

`site/index.html`・`outputs/05_lp_copy.md`の公開コピー部分を全文検索した結果、料金・講師人数・講師国籍・利用者数・満足度・継続率・実績数・口コミ・資格・受賞歴・No.1・成功率・TOEICスコア・Before/After・24時間・いつでも予約・好きな時間に受講・自分の都合に合わせて・勧誘なし・効果保証・必ず話せる・必ず上達する・絶対・100%・最短○日は**いずれも0件**。

## HTML / CSS / JavaScript

前回レビューから変更なし(site/は今回未修正)。HTMLタグバランス・id重複・見出し階層・CSS brace balance(132/132)・JS brace/括弧balance(8/8・31/31)、いずれも問題なし。

## CTA / FAQ / 画像 / アクセシビリティ / レスポンシブ

前回レビューの内容から変化なし。CTA3箇所(HERO/BENEFITS直後/FINAL CTA)、FAQ6問、画像2点(WebP・寸法・alt/aria-hidden/loading属性)、コントラスト(WCAG AA適合)、レスポンシブ(1440/1024/768/430/390/375pxの計算確認+PC/390pxの実機確認)、いずれも問題なし。

## Final Verdict

CRITICAL・HIGH・MEDIUM・LOWすべて0件。`outputs/05_lp_copy.md`と`site/index.html`の公開コピーは完全に同期し、client-brief.mdにない事実の混入も確認されなかった。残るINFOは実ブラウザ未確認幅(1440/1024/768/430/375px、非ブロッキング)のみであり、**公開・commit可能な状態**と判断する。
