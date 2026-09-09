# NEXORA AI Design Guide

本文書は、STEP07完了後のHTML/CSS/JS実装工程でそのまま参照できるデザイン仕様書である。画像生成・実装はまだ行わない。使用コピーは`05_lp_copy.md`の採用コピーに準拠する。

今回の目標は、FLEXIA(黒一色・スポーツ系・高級感)・LUMIEL(白基調・明るい教育系)のいずれとも異なる、**「実案件でAI SaaS企業・BtoBスタートアップに提案しても違和感がない」**BtoB SaaS/AIサービスLPの完成度を目指すことである。単純なテンプレートLP、同じカードの繰り返し、SF映画的な過剰な未来感は避ける。

---

## 1. Design Concept(デザインコンセプト)

**「業務を理解したうえでAIを設計する、信頼できるBtoB AIパートナーのプロダクトサイト」**

- **どんな印象を与えるか**: Modern / Sophisticated / Premium Tech / Trust / Innovation / Clean / Intelligent。Dark Navyを基調に、Blue〜Cyanのglow・グラデーション・floating UIで「今この瞬間も動いているプロダクト」感を出しつつ、情報設計は簡潔で読みやすく、意思決定者が安心して検討できる落ち着きを保つ
- **何を避けるか**: FLEXIAのような黒一色+ストイックな高級感、LUMIELのような明るい教育系トーン、SF映画的な過剰な未来感(ネオン過多、意味のない3D回転、派手なパーティクル)、テンプレート感(全セクション同一カードの繰り返し、3カード×連発、不要な角丸カードの大量使用、glow/英語ラベルの乱用)
- **デザインの軸**: 「作り込まれているが、読みやすい」。装飾はHERO・FEATURES・FINAL CTA等の見せ場に集中させ、情報量の多いセクション(PROBLEM・HOW IT WORKS本文・FAQ)は可読性を最優先する

## 2. Color Palette(カラーパレット)

| トークン | 用途 | HEX / 値 |
|---|---|---|
| Background Deep | ページ最背面(HERO・FINAL CTA等) | `#07111F` |
| Background Navy | セクション背景(Deepとの濃淡でリズムを作る) | `#0B172A` |
| Surface | カード・パネル背景 | `#111F35` |
| Surface Glass | ガラス調パネル背景(半透明) | `rgba(17, 31, 53, 0.6)` |
| Background Light(PROBLEM用) | 明るいセクション背景の候補 | `#F5F7FB` |
| Primary Blue | アイコン・リンク・テキストアクセント・glow・border | `#3B82F6` |
| Primary CTA | CTAボタン塗り(通常時) | `#2563EB` |
| Primary CTA Hover | CTAボタン塗り(hover時) | `#1D4ED8` |
| Cyan | セカンダリアクセント・glow・グラデーション終点 | `#22D3EE` |
| Light Blue | グラデーション中間色・floating card装飾 | `#60A5FA` |
| Text Primary(Inverse) | 暗背景上のメインテキスト | `#F8FAFC` |
| Text Secondary(Inverse) | 暗背景上の補足テキスト | `#A9B8CC` |
| Text Primary(明背景用) | 明背景セクション(PROBLEM候補)のメインテキスト | `#0B172A` |
| Text Secondary(明背景用) | 明背景セクションの補足テキスト | `#4B5A70` |
| Border(Inverse) | 暗背景上のボーダー | `rgba(148, 163, 184, 0.16)` |
| Border Strong(Inverse) | ガラス調パネルのボーダー | `rgba(148, 163, 184, 0.24)` |

### アクセシビリティ調整の経緯(必須事項)

依頼時のPrimary Blue候補`#3B82F6`は、白文字とのコントラスト比が**約3.678:1**で、WCAG AA(通常テキスト4.5:1)を明確に下回る。FLEXIA案件で経験した「アクセントカラーのコントラスト不足」と同種の問題が、より大きな差で再発する値だったため、**CTAボタンの塗り色にはより濃い`#2563EB`(白文字と5.169:1、適合)を専用トークンとして分離した**。`#3B82F6`自体は、暗背景上のテキスト・アイコン・リンクとして使う場合は4.879〜5.149:1でAAに適合するため、その用途に限定して使用する。

| 組み合わせ | 比率 | 判定 |
|---|---|---|
| Text Primary(`#F8FAFC`) vs Background Deep/Navy/Surface | 15.8〜18.1:1 | 適合 |
| Text Secondary(`#A9B8CC`) vs Background Deep/Navy/Surface | 8.2〜9.4:1 | 適合 |
| Primary Blue(`#3B82F6`)をテキスト/アイコンとして使用時 vs Deep/Navy | 4.88〜5.15:1 | 適合 |
| Cyan(`#22D3EE`)をテキスト/アイコンとして使用時 vs Deep/Navy | 9.9〜10.5:1 | 適合 |
| 白文字 on Primary CTA(`#2563EB`) | 5.169:1 | 適合 |
| 白文字 on Primary CTA Hover(`#1D4ED8`) | 6.702:1 | 適合(通常時より視認性低下なし) |
| 白文字 on Primary Blue(`#3B82F6`、CTA背景としては不使用) | 3.678:1 | **不適合のため、CTA背景には使用しない** |

**運用ルール**: `#3B82F6`はCTAボタンの塗り色として使用しない。ボタン塗りは必ず`--color-primary-cta`(`#2563EB`)を使用する。アイコン・リンク・見出しアクセント・glow装飾には`#3B82F6`をそのまま使用してよい。

## 3. Typography(タイポグラフィ)

**第一候補(Webフォント)**: 日本語 = Noto Sans JP(Google Fonts、Zen Kaku Gothic Newを代替候補として保持) / 英数字 = Inter(Google Fonts、Manropeを代替候補として保持)
**CSSフォールバック**: `-apple-system, BlinkMacSystemFont, "Hiragino Kaku Gothic ProN", "Yu Gothic", "Segoe UI", sans-serif`

| 要素 | Desktop | Mobile | weight | line-height | letter-spacing |
|---|---|---|---|---|---|
| Hero H1 | `clamp(40px, 4.2vw, 64px)` | 34px | 800 | 1.35 | -0.01em |
| H2(セクション見出し) | 40px | 28px | 800 | 1.4 | -0.005em |
| H2-emphasis(INSIGHT等) | 48px | 30px | 800 | 1.3 | -0.01em |
| H3 | 20px | 18px | 700 | 1.5 | 0 |
| Body | 16px | 15px | 400 | 1.75 | 0 |
| Small / UIラベル | 13px | 12px | 600 | 1.4 | 0.06em(uppercase) |
| Button | 16px | 15px | 700 | 1.2 | 0.01em |
| Eyebrow | 12px | 11px | 700 | 1.2 | 0.18em(uppercase) |

**HERO H1の改行について**: 「AIを、現場で使える仕組みに。」(12文字)は、Desktopでは`clamp()`により1行または意味の切れ目(「AIを、」/「現場で使える仕組みに。」)での自然な2行を想定する。Mobile(34px)では、375px幅でコンテナ幅(側余白20px×2を除く)を計算したうえで、「AIを、」/「現場で使える仕組みに。」の自然な2行になるよう、実装時に`<br>`または`clamp()`で調整する。不自然な1〜2文字だけの孤立行が発生しないよう、実装時に文字数×フォントサイズでの事前検証を必須とする(FLEXIA・LUMIEL両案件で発生した見出し折返し問題を教訓とする)。

## 4. Grid / Container(グリッド・コンテナ)

- **最大コンテンツ幅**: 1240px
- **Desktop左右余白**: 48px(1024px前後の狭いDesktopでは40px)
- **Tablet左右余白**: 32px
- **Mobile左右余白**: 20px
- **container設計**: `.container { max-width: 1240px; margin: 0 auto; padding: 0 var(--space-side); }`
- **grid基本ルール**: CSS Gridベース。Bento Grid(FEATURES)は明示的な`grid-template-areas`または列/行スパン指定で管理し、意図しない折り返しを防ぐ

## 5. Spacing(余白・セクションリズム)

- **Section padding(基本)**: Desktop 120px / Tablet 96px / Mobile 80px
- **重要**: 全セクションを同一paddingにせず、以下のように視覚的リズムを作る
  - HERO: Desktop 0(`min-height`で制御) / Mobile 64px上+80px下
  - INSIGHT: Desktop 140px(前後セクションより広く、余白を大胆に取るブランドセクション) / Mobile 88px
  - 中間CTA: Desktop 96px(前後より控えめ、パネル自体の内側paddingで存在感を出す) / Mobile 72px
  - FINAL CTA: Desktop 130px / Mobile 88px
  - その他(PROBLEM/INSIGHT以外/HOW IT WORKS/FEATURES/USE CASE/SUPPORT/FAQ): Desktop 120px / Mobile 80px
- **カード間gap**: Bento Grid 20〜24px、その他カードグリッド 24〜28px
- **`:root`のデフォルトはMobile(SP)値とし、768px以上でTablet値、1024px以上でDesktop値に切り替える。**(FLEXIA案件STEP08で発覚した「Mobileに意図せずPC値が適用される」カスケード不具合を、本案件では設計段階から回避する)

## 6. Header(ヘッダー)

- 固定(sticky)、高さ64〜72px
- 背景: `rgba(7, 17, 31, 0.72)` + `backdrop-filter: blur(10px)`(半透明グラス調、スクロール時も下のHEROが透けて見える演出)
- ロゴ: 「NEXORA」+ 下段に小さく「AI」(FLEXIA/LUMIELと同じ2行ブランドマーク構造を踏襲、フォントはInter)
- ナビゲーションリンクは最小限(本LPは単一ページのためナビ自体を持たない、またはCTAへのアンカーのみとする方針をSTEP07以降で確定)
- ボーダー: 下端に`Border(Inverse)`の1pxライン

## 7. HERO(SECTION 01)

**使用コピー**: `05_lp_copy.md`のSECTION01(見出し・本文・補足コピー・CTA・サブCTA・UIラベル)をそのまま使用する。

- **PCレイアウト**: 2カラム(左=eyebrow+H1+本文+CTA+サブCTA+補足コピー、右=Dashboard mockup)。カラム比率は`1.08fr 0.92fr`程度とする
- **SPレイアウト**: 1カラム縦積み。eyebrow → H1 → 本文 → CTA → サブCTA → 補足コピー → Dashboard mockupの順(Dashboardは最後、幅100%以内)
- **背景**: Background Deep(`#07111F`)を基調に、以下を重ねる
  - radial gradient glow(Blue→Cyan、右上または右側に配置し、Dashboard mockupの位置と呼応させる)
  - subtle grid線(1px、`Border(Inverse)`と同系色、opacity低め)
  - blurred light orb(大きくぼかした円形のglow、1〜2個)
  - 抽象的なテクノロジーパターン(細い接続線・ドット、装飾密度は控えめ)
- **奥行き・レイヤー感**: 背景グロー(最背面) → grid線(中間) → Dashboard mockup(floating card含む、最前面)という3層構造でレイヤー感を出す
- **画面高さ**: Desktopで`min-height: 92vh`程度を目安とし、100vh固定にはしない

## 8. HERO Dashboard Mockup(HTML/CSSベースのUI構築)

**方針**: 画像ではなく、HTML/CSSで構築するUIパネルを優先する(STEP07での画像生成は最小限に抑える)。

**構成(Main Dashboard Panel)**:
```
Dashboard Panel(glassmorphism, rounded 20px)
├── Top bar(3つのドット風装飾 + タイトルラベル「NEXORA AI」)
├── Workflow card(接続されたノード風のミニ図。ラベルのみ、数値なし)
├── Process visualization(進捗"らしさ"を出す装飾バー。%表示・実数値は使用しない。単なる装飾グラデーションバーとする)
├── Integration nodes(2〜3個の小さな円形ノードを線でつなぐ)
└── Floating status cards(Panel外に2〜3枚を浮かせて重ねる)
```

**表示するUIラベル(`05_lp_copy.md`準拠、数値・成果は一切表示しない)**:
- WORKFLOW / ACTIVE
- AI ASSIST / CONNECTED
- PROCESS / READY
- SUPPORT / ACTIVE

**明示的に禁止する表現**: 売上・%・ROI・成果数値・件数・時間削減・顧客数・実績グラフ。円グラフ・棒グラフは架空の成果に見えるため原則使用しない。進捗バー風の装飾を使う場合も、数値・パーセンテージのラベルは付けず、視覚的な"動いている感"のみを表現する。

**代替のテック感演出**: node connection(線でつながる円)、progress風の装飾ライン(数値なし)、workflow path(点線または矢印)、status dot(小さな発光ドット、色でON/OFF状態を示す程度)、integration chip(角丸の小さなラベルタグ)。

## 9. Floating UI(HERO周辺の浮遊カード)

- Dashboard周辺に2〜3枚のfloating cardを配置(例: 「AI ASSIST / CONNECTED」「WORKFLOW / ACTIVE」「SUPPORT / READY」)
- PC: `position: absolute`でDashboard Panelの外側にわずかにはみ出す形で浮かせ、subtle glassmorphism(`background: rgba(17,31,53,0.6); backdrop-filter: blur(12px); border: 1px solid rgba(148,163,184,0.24);`)+soft glow(box-shadow)を適用
- Mobile: floating配置を解除し、Dashboard Panel内部の通常フロー要素として統合する(`position: static`に切り替え、横スクロールを絶対に発生させない)

## 10. Glassmorphism運用ルール

使用箇所を**Dashboard mockup・Floating card・中間CTAパネル・FEATURESの一部カード**に限定する。全カードに適用しない。

```css
.glass-panel {
  background: rgba(17, 31, 53, 0.6);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid rgba(148, 163, 184, 0.24);
  box-shadow: 0 8px 32px rgba(7, 17, 31, 0.4);
}
```

## 11. PROBLEM(SECTION 02)

**使用コピー**: `05_lp_copy.md`のSECTION02(見出し・本文・箇条書き5項目)。

- **背景**: HEROとの差別化のため、Background Light(`#F5F7FB`程度の明るいNavy寄りグレー)を検討候補とする。暗背景を継続する場合はBackground Navy(`#0B172A`、HEROのDeepより一段階明るい)とし、いずれにせよHEROと同一トーンの繰り返しを避ける
- **レイアウト**: 単純な5枚均等カードにしない。以下のいずれかを採用する
  - 見出しを大きく配置し、5つの悩みを**issue chip**(角丸の短いタグ)として横並び〜折り返し配置し、下に短い補足を添える
  - または、5項目を**staggered list**(左右に少しずつオフセットさせた縦list)として配置し、単調な均等グリッドを避ける
- **強調**: 悩みの中でも中心的な2つ(「AIを導入したいが活用方法が分からない」「どの業務をAI化できるか分からない」)は、フォントサイズまたは色(Primary Blue)でわずかに強調してよい
- **警告色(赤)は使用しない**

## 12. INSIGHT(SECTION 03)

**使用コピー**: `05_lp_copy.md`のSECTION03(見出し・本文)。

- **方針**: ブランドセクションとしてミニマルに構成する。カード・リストは使わない
- **レイアウト**: H2-emphasis(48px)で見出しを主役にし、本文は1〜2文に絞る。余白を大胆に取り(Desktop 140px)、LP全体の中で最も"静かな"セクションとする
- **背景**: Background Deepを基調に、薄いgrid線または1本の細いglowラインのみを装飾として置く。HERO・PROBLEMより装飾密度を大きく落とすことで、直前のセクションとのコントラストを作る

## 13. HOW IT WORKS(SECTION 04)

**使用コピー**: `05_lp_copy.md`のSECTION04(5ステップのタイトル・本文)。

- **Desktop**: 5ステップを横方向、またはジグザグ(交互に上下にずらす)のconnected flowとして配置する。各ステップは「STEP番号+アイコン+タイトル+短い本文」の組み合わせで、接続線(Blue→Cyanのgradient)でつなぐ
- **Mobile**: 縦方向のタイムライン(左端に縦の接続線、右側にステップ内容)に再構成する
- **アイコン**: 業務ヒアリング=虫眼鏡/リスト系、AI活用設計=ノード/回路系、導入支援=歯車/接続系、AIツール活用支援=チェック/操作系、運用サポート=シールド/循環系、のようなシンプルな線画アイコンを割り当てる(具体的なSVGパスはSTEP07以降で作成)
- **アニメーション**: 接続線に沿った軽いflow animation(グラデーションが流れるような表現)を使用可。`prefers-reduced-motion`が有効な場合は静止させる
- **重要**: 期間・日数・回数の表示は行わない。STEP番号(01〜05)のみ使用する

## 14. FEATURES(SECTION 05・Bento Grid)

**使用コピー**: `05_lp_copy.md`のSECTION05(6項目のタイトル・UIラベル・本文)。

**Desktop Bento Grid構成案**(単純な6等分は禁止):

```
grid-template-columns: repeat(4, 1fr);
grid-template-rows: repeat(2, auto);

[業務ヒアリング]        [業務ヒアリング]        [AI活用方法の提案]  [AIツール活用支援]
(Large, 2×1)            (Large続き)              (Medium, 1×1)       (Medium, 1×1)

[業務フローに合わせた導入支援]  [業務フローに合わせた導入支援]  [導入後の運用サポート]  [オンライン相談]
(Large, 2×1)                    (Large続き)                      (Medium, 1×1)          (Small/横長, 1×1)
```

- **Large card(業務ヒアリング/業務フローに合わせた導入支援)**: 2列分の幅を持ち、簡単な説明文に加えて小さなミニビジュアル(node風装飾、またはmini flow図)を添える
- **Medium card(AI活用方法の提案/AIツール活用支援/導入後の運用サポート)**: 1列幅、アイコン+タイトル+本文の標準構成
- **Small/horizontal card(オンライン相談)**: 最も小さく軽い扱いとし、chat bubble風のミニアイコンを添える

**各カードに異なるUI要素を割り当て、同じ見た目のカードを繰り返さない**:
- 業務ヒアリング: node/リスト風の小さな図
- AI活用方法の提案: mini flow(矢印でつながる2〜3個の小円)
- 業務フローに合わせた導入支援: connection line(業務フローを線でつなぐイメージ)
- AIツール活用支援: チェックマーク付きの小さなステータスドット
- 導入後の運用サポート: 循環矢印風の小さなアイコン
- オンライン相談: chat bubbleアイコン

**Mobile**: 1カラムに再構成。大小の差はカードの縦paddingとフォントサイズで表現し、Desktopの複雑なグリッド構造は維持しない。

## 15. Middle CTA(SECTION 06・中間CTA)

**使用コピー**: `05_lp_copy.md`のSECTION06(本文・CTA)。

- 単なるボタン単体ではなく、視覚的に独立した**CTAパネル**として構成する
- 背景: Dark〜Blueのgradient panel、またはSurface Glass(半透明グラスパネル)のいずれかを候補とし、STEP07で確定する
- FINAL CTAより装飾・サイズともに控えめにし、LP終盤のFINAL CTAが最も強い見せ場になるよう役割を分ける

## 16. USE CASE(SECTION 07)

**使用コピー**: `05_lp_copy.md`のSECTION07(見出し・本文・3項目、いずれも「活用イメージの例」である旨を含む)。

- **UI上の明示**: 各カードに「EXAMPLE」または「活用イメージ」という小さなラベルを、コピー本文の「(活用イメージの例)」表記に加えて視覚的にも表示する(バッジ風の小さなタグ)
- **見た目**: browser-style card(ブラウザウィンドウ風の枠、上部に3つのドット装飾)、またはworkflow card(付箋・簡易フローチャート風の図)のいずれかで3項目(情報整理/文書作成/問い合わせ対応)を表示する
- **禁止**: 企業ロゴ、担当者写真、成果値、星評価、実在アプリのUI模倣は一切使用しない

## 17. SUPPORT(SECTION 08)

**使用コピー**: `05_lp_copy.md`のSECTION08(見出し・本文)。

- **ビジュアル**: 中心に「NEXORA AI」ノード、周囲に確定特徴に基づくノード(例: 「AI ASSIST」「OPERATION」)を配置した放射状の関係図とする。**サービス内容を超える新しい支援工程を作らない**(周囲ノードはclient-brief.mdの確定特徴の言い換えにとどめる)
- HERO Dashboardとは見た目を変える(放射状レイアウト、HERO Dashboardのパネル形式とは異なる構成)
- 背景: Background Navyを基調とし、HOW IT WORKSの横方向フローとも視覚的に区別する

## 18. FAQ(SECTION 09)

**使用コピー**: `05_lp_copy.md`のSECTION09(6問)。

- Accordion形式。`<button>`要素、`aria-expanded`、`aria-controls`、`role="region"`、keyboard操作対応をFLEXIA/LUMIEL案件と同じパターンで実装する
- デザイン: シンプルでクリーンな`border-bottom`区切り、またはglass accordion(パネル全体にSurface Glassを適用)のいずれかを候補とし、可読性を最優先する
- 背景: Background DeepまたはNavy(明るい背景にする場合はPROBLEMと呼応させて検討)

## 19. FINAL CTA(SECTION 10)

**使用コピー**: `05_lp_copy.md`のSECTION10(見出し・本文・CTA)。

- LP最後の最大の見せ場。大きなGradient/Glow Panel(Background Deep基調+Blue→Cyanのradial glow+subtle grid)
- HEROよりもシンプルな構成とし、装飾よりもCTAボタンの視認性を最優先する
- CTAボタンは白背景+Primary CTA文字、またはPrimary CTA背景+白文字のいずれかで、7章のコントラスト計算に基づき配色を確定する

## 20. Footer(SECTION 11)

**使用コピー**: `05_lp_copy.md`のSECTION11(架空制作表記)。

- 背景: Background Deep(Dark Navy)
- ブランド名「NEXORA AI」+ 架空案件表記を、Small textサイズだが**十分に読めるサイズ**(12px以上)で表示する。極端な縮小・非表示は行わない

## 21. Motion(モーション)

**使用可能**: scroll reveal、stagger reveal(FEATURESのBento Gridで各カードを少しずつ遅延させて表示)、hover lift、subtle glow、floating animation(HERO floating cardの微細な上下運動)、moving gradient(HOW IT WORKS接続線)、connection-line animation。

**禁止**: 派手な3D回転、強いparallax、大量のparticles、読みにくくなるアニメーション。

**必須**: `prefers-reduced-motion: reduce`が有効な場合、上記すべてのアニメーションを無効化し、要素を最初から表示状態にする。floating animationも停止する。

## 22. インタラクション

- FAQ accordion、hover state(カード・ボタン)、`:focus-visible`、CTA hover(色変化+わずかな`translateY`)、card hover(glow強調)
- Dashboard内のstatus dot等に微細なアニメーションを加えてよいが、**クリックしないと重要情報が読めない設計は避ける**(Dashboard・floating cardの情報はホバー/クリック操作なしで常時視認できる状態にする)

## 23. Responsive(レスポンシブ)

| 項目 | Desktop(1440/1280/1024) | Tablet(768) | Mobile(430/390/375) |
|---|---|---|---|
| HERO | 2カラム、Dashboard右配置 | 2カラム(縮小)または1カラム | 1カラム縦積み、Dashboardは最後 |
| Dashboard mockup | フル装飾、floating card浮遊 | floating簡略化 | floating解除、Panel内へ統合 |
| HOW IT WORKS | 横方向/ジグザグflow | 横方向(縮小)または縦 | 縦方向タイムライン |
| FEATURES(Bento Grid) | 4列、大小混在 | 2列 | 1列 |
| USE CASE | 3カラム | 2カラムまたは1カラム | 1カラム |
| FINAL CTA | 大型パネル | 同左(縮小) | 縦積み、CTA幅は内容に応じた可変幅 |

**Mobile HERO推奨構成**: コピー → CTA → サブCTA → Dashboard(幅100%以内)。floating cardはabsoluteのまま画面外にはみ出させず、必要なら通常フローへ変更する。**Mobileでは全セクションを通じて横スクロールを絶対に発生させない**(`overflow-x: hidden`、固定px幅の排除、Bento Grid/Workflow/USE CASEカードの1カラム化を徹底する)。

## 24. Accessibility(アクセシビリティ)

- **コントラスト**: 本文・見出しとも背景とのコントラスト比4.5:1(大きな見出しは3:1)以上を実装時に確認する。特にPrimary Blue(`#3B82F6`)はCTA背景として使用せず、CTA背景は必ずPrimary CTA(`#2563EB`)を使用する(2章参照)
- **glowエフェクトへの配慮**: Blue/Cyanのglow装飾が本文テキストに重なる場合、テキスト背後に半透明のスクリムまたは十分な余白を確保し、本文コントラストを損なわないようにする
- **focus-visible**: すべてのボタン・リンク・アコーディオントリガーに明確なフォーカスリング(Primary BlueまたはCyan、offset 2px)を設定する
- **操作領域**: ボタン・タップ対象は44px前後以上を確保する
- **semantic heading**: h1→h2→h3の順を守り、階層を飛ばさない
- **FAQのaria属性**: `aria-expanded`、`id`と`aria-controls`、`role="region"`と`aria-labelledby`を設定する
- **keyboard操作**: すべての操作要素をTabキーで到達可能にし、アコーディオンはネイティブ`<button>`でEnter/Space対応する
- **色だけに依存しない情報表現**: Dashboard内のstatus dot等は、色に加えてテキストラベル(ACTIVE/READY/CONNECTED等)を必ず併記する
- **`prefers-reduced-motion`**: 21章の通り、アニメーションを無効化するフォールバックを用意する

## 25. Image Strategy(画像戦略、STEP07への引き継ぎ)

**方針**: NEXORA AIはFLEXIA・LUMIELほど人物写真に依存しない。メインビジュアルはHTML/CSS製のDashboard UIを優先し、STEP07で生成する画像は**最大2点**に抑える。

- **IMAGE候補01(任意)**: Abstract AI workflow visual — HERO背景の補強、またはINSIGHT/SUPPORT背景装飾として使う抽象的なテクノロジービジュアル(具体的な使用要否・使用箇所はSTEP07で判断する)
- **IMAGE候補02(任意)**: Premium technology workspace — USE CASE等での補助的な雰囲気画像(具体的な使用要否はSTEP07で判断する)

Dashboard mockup自体はCSS/UIで制作することを優先し、画像化しない。画像を使用する場合もWebP形式とし、架空の数値・グラフ・UIを画像内に描写しない(07_image_promptsで詳細を設計する)。

## 26. Performance(パフォーマンス)

- 大量画像・動画背景・WebGL・Three.js・大量canvas・外部JSライブラリの乱用は避ける
- HTML/CSS/Vanilla JS中心で実装する(FLEXIA/LUMIELと同じ方針)
- アイコンは絵文字を使用せず、inline SVGまたはCSSで実装する(外部アイコンライブラリの導入は必要性を精査し、可能な限り避ける)
- 画像を使用する場合はWebP形式とする
- Dashboard mockup・floating card・glow等の装飾はCSSのみで実装し、追加の画像・JSライブラリを必要としない設計にする

## 27. CSS Architecture Guidance(CSS設計方針)

- FLEXIA/LUMIEL案件と同様、CSS変数(custom properties)によるデザイントークン管理を踏襲する(28章のトークン一覧を参照)
- レイヤー構成: `:root`(トークン定義) → リセット → 基本要素 → レイアウト(`.container`/`.section`) → コンポーネント(`.card`/`.button`/`.dashboard-*`/`.bento-*`) → セクション固有スタイル → レスポンシブ(モバイルファースト、`min-width`メディアクエリで拡張)
- Bento Grid・Dashboard・Workflowなど本案件特有のコンポーネントは、専用のクラス命名(`.dashboard-panel`, `.bento-grid`, `.workflow-node`等)で管理し、既存コンポーネント(`.card`等)と混在させすぎない
- `--space-side`/`--space-section`は`:root`のデフォルトをSP値にし、768px以上でTablet値、1024px以上でDesktop値に切り替える(5章参照。FLEXIA STEP08の教訓を実装当初から反映する)

## 28. 実装時に守るデザイントークン

```css
:root {
  /* Color */
  --color-bg-deep: #07111F;
  --color-bg-navy: #0B172A;
  --color-bg-light: #F5F7FB;
  --color-surface: #111F35;
  --color-surface-glass: rgba(17, 31, 53, 0.6);
  --color-primary: #3B82F6;
  --color-primary-cta: #2563EB;
  --color-primary-cta-hover: #1D4ED8;
  --color-cyan: #22D3EE;
  --color-light-blue: #60A5FA;
  --color-text-inverse: #F8FAFC;
  --color-text-inverse-sub: #A9B8CC;
  --color-text: #0B172A;
  --color-text-sub: #4B5A70;
  --color-border-inverse: rgba(148, 163, 184, 0.16);
  --color-border-strong: rgba(148, 163, 184, 0.24);

  /* Spacing(モバイルファースト: デフォルトはSP値) */
  --max-width: 1240px;
  --space-side-pc: 48px;
  --space-side-tablet: 32px;
  --space-side-sp: 20px;
  --space-section-pc: 120px;
  --space-section-tablet: 96px;
  --space-section-sp: 80px;
  --space-side: var(--space-side-sp);
  --space-section: var(--space-section-sp);
  --space-card-gap: 24px;
  --space-card-gap-bento: 20px;

  /* Typography */
  --font-jp: "Noto Sans JP", -apple-system, BlinkMacSystemFont, "Hiragino Kaku Gothic ProN", "Yu Gothic", "Segoe UI", sans-serif;
  --font-en: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-size-h1-sp: 34px;
  --font-size-h1: clamp(40px, 4.2vw, 64px);
  --font-size-h2-sp: 28px;
  --font-size-h2: 40px;
  --font-size-h2-emphasis-sp: 30px;
  --font-size-h2-emphasis: 48px;
  --font-size-h3-sp: 18px;
  --font-size-h3: 20px;
  --font-size-body-sp: 15px;
  --font-size-body: 16px;
  --font-size-small-sp: 12px;
  --font-size-small: 13px;
  --font-size-button-sp: 15px;
  --font-size-button: 16px;
  --font-size-eyebrow-sp: 11px;
  --font-size-eyebrow: 12px;

  /* Radius */
  --radius-card: 18px;
  --radius-panel: 24px;
  --radius-button: 999px;
  --radius-chip: 999px;
  --radius-small: 8px;

  /* Shadow / Glow */
  --shadow-card: 0 8px 24px rgba(7, 17, 31, 0.3);
  --shadow-card-hover: 0 16px 40px rgba(7, 17, 31, 0.45);
  --glow-primary: 0 0 60px rgba(59, 130, 246, 0.28);
  --glow-cyan: 0 0 60px rgba(34, 211, 238, 0.22);

  /* Breakpoint(参考値。メディアクエリ内に直接記述) */
  /* Desktop: min-width 1024px / Tablet: 768px-1023px / Mobile: max-width 767px */

  /* Transition */
  --transition-base: 0.2s ease;
  --transition-glow: 0.35s ease;
}
```

## 29. Design QA Checklist(自己レビュー・テンプレート感チェック)

STEP06内で以下を自己レビューした結果を記録する。

| チェック項目 | 結果 |
|---|---|
| 全セクションが同じカードレイアウトになっていないか | 該当なし。PROBLEM(issue chip/staggered list)、HOW IT WORKS(connected flow)、FEATURES(Bento Grid)、USE CASE(browser-style card)、SUPPORT(放射状ノード図)と、セクションごとに異なるUIパターンを採用している |
| 全背景が同じトーンになっていないか | 該当なし。Background Deep(HERO/INSIGHT/FINAL CTA)、Navy(SUPPORT/FAQ候補)、Light(PROBLEM候補)を使い分け、暗→明→暗のリズムを作っている |
| 3カード×繰り返しになっていないか | 該当なし。FEATURESはBento Grid(大小混在6項目)、HOW IT WORKSは5ステップのフロー、USE CASEは3項目だが「例」であることを明示したbrowser-style cardで構成 |
| 不要な角丸カードの大量使用がないか | INSIGHTはカードを使わずタイポグラフィのみ、SUPPORTはカードではなく関係図で構成し、カード多用を避けている |
| glowの乱用がないか | glowはHERO・中間CTA・FINAL CTAの見せ場に限定し、PROBLEM・FAQ等の情報密度が高いセクションでは装飾を控えている |
| 英語ラベルの乱用がないか | UIラベルはHERO DashboardとFEATURESのUIラベルのみに限定し、それ以外のセクションでは日本語コピーを主体としている |
| SaaSっぽいだけの装飾になっていないか | Dashboard・Workflow・Bento Gridはいずれも確定情報(業務ヒアリング/AI活用方法の提案/導入支援/活用支援/運用サポート/オンライン相談)と直接対応させており、装飾のための装飾になっていない |

**総合判定**: 上記チェックの結果、テンプレート感・カードの単調な繰り返しは確認されなかった。STEP07(画像プロンプト設計)・実装工程では、本文書のBento Grid構成・Dashboard UI構成・カラートークン(特にCTA背景色`#2563EB`の運用ルール)を厳守すること。

CSS自体の実装は、STEP07完了後のHTML/CSS/JS実装工程で行う。本文書はあくまで仕様書である。
