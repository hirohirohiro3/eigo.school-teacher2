# 制作の記録

> **2026-10-10（昼）にこのファイルを分割しました。** 新しい記録は上に足しています。10-09（夜）の順21：中2の総合テスト 第2部、10-09（昼）の順20：第1部、10-09（夜・10-08 16:13 UTC 開始）の順19：中2の総合テストの道具の記録は `STATUS-archive-2026-10-10.md` にそのまま入っています。それより前は `STATUS-archive-2026-10-08.md`、`STATUS-archive-2026-10-07.md`、`STATUS-archive-2026-10-06.md`、`STATUS-archive-2026-10-05.md`、`STATUS-archive-2026-10-03.md`、`STATUS-archive-2026-10-02.md`、`STATUS-archive-2026-10-01.md`、`STATUS-archive-2026-09-30.md`、`STATUS-archive-2026-09-28.md`、`STATUS-archive-2026-09-26.md`、`STATUS-archive-2026-09-24.md`、`STATUS-archive-2026-09-23-night.md`、`STATUS-archive-2026-09-23.md`、`STATUS-archive-2026-09-22.md`、`STATUS-archive-2026-09.md` です。
>
> 手順は前回と同じで、**古い `STATUS.md` を `update_file` で `STATUS-archive-2026-10-10.md` に改名し、この新しい `STATUS.md` を置いています。** アーカイブ側の中身は1バイトも触っていません。リポジトリに反映するときは、改名されたアーカイブとこの新しい `STATUS.md` の両方を置いてください。「Drive からの復元」「Drive へのアップロード」の要点は下に書き写してあります。

---

## 2026-10-11（昼の枠／JST。開始 2026-10-11 06:08 UTC ＝ 15:08 JST）　順24：中2の総まとめテスト

手順5の判定：1番目は通過（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-N"` のキーで積む作り）。2番目は `g2/` に Unit 1〜16 の2本ずつが Drive にそろい、復元した Unit 15・16 は `check.py 15`・`16 --grade 2` が NG 0件。3番目は `word-test.html` に `data-g="2"` があり `--word-test` が NG 0件。4番目は `GRADE_REVIEW_SPEC[2]` あり。5番目は `g2/review01`〜`04` がそろい4本とも `--review N --grade 2` が NG 0件。6番目で `g2/review-final.html` が無いので、**順24＝中2の総まとめテスト（Unit 1〜16）**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/review-final.html` | **新規**（67,080バイト）中2の総まとめテスト | g2 |
| `g2/index.html` | 変更（17,270 → 17,277バイト）「中2のまとめ」の「総まとめテスト　準備中」をリンクに | g2 |
| `STATUS.md` | 変更（この記録を上に追記） | ルート |

ほかのファイル（`index.html`・`word-test.html`・`tools/` の4本・`units/` の22本・`g2/` のほかの26本・計画書類）は**1バイトも変えていません**（復元直後と作業後の md5 を機械で突き合わせ、差分は `g2/index.html` だけ）。**`check.py`・`build.py`・`master-vocab.json` は今回いっさい触っていません。**

### 中身（`g2/review-final.html`）

`python tools/build.py --grade 2 review final "中2の総まとめ" "Unit 1〜16" body.html` で組みました。大問の構成・配点は `UPDATE-PLAN.md`「2. 総合テスト」と中2 review01〜04 と同じ（全31問・100点）。

| 大問 | 配点 | 中身 | 出題の Unit |
|---|---|---|---|
| 1 文法 | 25（2×5＋3×5） | **10問すべて別の Unit**（中1の総まとめと同じ作り）。4択5問（was taking＝1／going to＝3／must not＝6／finished cleaning＝12／covered with＝16）、語形変化（There were ＝5）、並べかえ2問（My uncle gave me a nice watch.＝8／Please tell me how to use this computer.＝11）、誤文訂正2問（will goes → go＝2／If it will be sunny → is＝4） | 1〜6・8・11・12・16 |
| 2 資料つきの読解 | 18（3×6） | 町の「Clean River Day」の予定表と、ユナが留学生マイクに送るメール **133語** | 2・6・7・9・10・15 |
| 3 対話文の読解 | 21（3・4・4・3・4・3） | カナダから来るいとこをどこへ連れて行くか、タクと ALT のグリーン先生の対話 **154語** | 1・4・11〜14 |
| 4 条件英作文 | 10 | 週末のボランティア、図書館で子どもに英語の本を読む（Plan A）か公園で花を植える（Plan B）か。**30語以上・because を使う・書き出しの want to のほかに不定詞・動名詞・比較・受動態のどれかを1回以上** | 4・9・12・13 |
| 5 長文の読解 | 26（2×3・3×2・4・4・6） | 祖父が作ってくれた木の箱についてのハルカのスピーチ **149語** | 1・8・10・12〜16 |

- 判断が要る問題は8問（英問英答5・日本語の記述2・条件英作文1）。すべてに模範解答と採点の目安があります。
- **単元の要注意事項を出題に入れました**：Unit 1 の過去進行形（大問1 問1 で were taking を誤りの選択肢に・大問3 の英問英答）、Unit 4 の「when / if の中は未来でも現在形」（誤文訂正）、Unit 6 の must not と don't have to（大問1 問3・大問2 の Why doesn't Mike have to 〜?）、Unit 7 の Shall we 〜?（大問2 問1）、Unit 8 の SVOO（並べかえ・大問5 の英問英答で代名詞の格 gave she を誤りの形に）と SVOC（大問5 本文の call it 〜／make my work easy）、Unit 10 の目的の to（大問2 問2・大問5 の ( 3 )）、Unit 11 の疑問詞 + to（並べかえ how to use・大問3 の ( A ) where to take）、Unit 12 の enjoy / finish ＋動名詞（大問1 問4）と動名詞の主語は単数（大問3 の英問英答で Cooking together are fun を誤りの形に・大問5 の ( 2 ) Looking）、Unit 13 の比較級（大問3 の下線部 fresher than）、Unit 14 の not as 〜 as（大問5 の英問英答）、Unit 15 の受動態（大問2 の are given・大問5 の下線部 were used by）、Unit 16 の be covered with と be made of（大問1 問5・大問5 の ( 1 )）。
- **語彙**：中1の479語＋中2 Unit 1〜16 の567語と `check.py` の `BASIC` の範囲で書きました。`master-vocab.json` と機械で突き合わせ、範囲外だった `fish`・`video`・`year`（単数形）・`hi` を書きかえています（`birds`・`morning market` と `vegetables`・`reading a book`・`Last summer`・`Hello`）。残った範囲外は固有名詞（Yuna・Mike・Taku・Mr. Green・Haruka・Minato・Kyoto・Canada・Japan）と月・曜日（August・November・Saturday・Wednesday）だけです。

### 検証結果

- `check.py --review final --grade 2`：**24項目 NG 0件**（375px で横スクロールなし・印刷 A4 11ページを含む）。最初の版は読解本文2（対話）が171語で NG 1件だったので、語を書きかえるついでに最後の2行を削って154語にしました。
- **中1の既存の検査はすべて NG 0件**：`--index`・`--word-test`・`--review 1`〜`4`・`--review final`、`check.py 16`。中2：`--index --grade 2`・`--review 1`〜`4 --grade 2`・`--review final --grade 2`・`check.py 15`・`16 --grade 2`。**作業前にも同じ検査で NG 0件のベースラインを取ってあります。**
- **playwright（Chromium・375px、Google Fonts は空の CSS に差し替え）**：`g2/review-final.html`・`review01`〜`04`・`g2/index.html`・`index.html`・`units/review-final.html`・`units/review04.html`・`word-test.html`（`?grade=2`・`?unit=5`・`?part=2-4`）の**12通り**で scrollWidth 375px・JS の例外0件。
- **満点の確認**：`g2/review-final.html` に全31問の正解（記述は模範解答）を機械で入れて「採点する」を押し、**100点／大問ごとに 25・18・21・10・26 の満点**、「Unit ごとの正答率」が **Unit 1〜16 の16単元とも100%**（リンク16本・「見直し」の印0件）。結果画面も 375px で横スクロールなし。「先生に送る（画像）」で **1080×5044 の画像**がモーダルに出て、JS の例外0件。**回帰として `g2/review01`〜`04` でも同じ満点テストを通しました**（4本とも100点）。

### 自分で判断したこと

1. **大問1を「10問すべて別の Unit」にしました。** 中1の総まとめ（`units/review-final.html`）が「16単元から1問ずつ」の作りなので合わせています。大問1で拾えない6単元（7・9・10・13・14・15）は大問2・3・5 で必ず1問以上、`data-unit` に入れています。
2. **大問4の条件を「書き出しの want to のほかに、不定詞・動名詞・比較・受動態のどれかを1回以上」にしました。** 第3部・第4部の条件を合わせた形で、中2の後半の文法を使わせるためです。`data-unit` は `4 9 12 13`（because・不定詞・動名詞・比較）。`data-avoid` には like read／enjoy to read／more better／will goes／must to など中2全体でよく出る誤りの形を入れました。
3. **大問2の英問英答 What is given to everyone at lunch? と、大問2 問5 の Why doesn't Mike have to bring his lunch? を、同じ本文の別の Unit（15 と 6）として出しました。** 問5 は `data-unit="6 15"` です。
4. **大問2 問1 の選択肢を日本語にしました**（Shall we 〜? の働きを問うため）。採点は `input` の value で行うので、選択肢が日本語でも採点に影響しないことを満点テストで確かめました。
5. **大問2 の日付を「Saturday, November 14」にしました。** 2026年11月14日は土曜日です。
6. 中3の形（現在完了・`too 〜 to`・`want 人 to`・間接疑問・関係代名詞・仮定法・付加疑問）は使っていません（検査でも NG 0件）。`tell me how to use` は「疑問詞 + to」で、間接疑問ではありません。

### 気になった点（次の回への申し送り）

- **次は順25＝中3の道具の準備です**（`PLAN-g2g3.md` 5.2 の中3の `LATER_GRAMMAR`、`g3/index.html`（全部準備中）。`index.html`・`g2/index.html` のヘッダーの「中3」は準備中のまま）。教材は作らない回です。
- **`fish`・`video`・`year`（単数形）・`hi` が `master-vocab.json` にも `BASIC` にもありません。** `fish` は中学の基本語なので、中3 Unit 1 以降の新出語に入れるかどうかは人の判断だと思います（今回は避けて書きました）。
- `g2/vocab12_gerund.html` の `take part in 〜` の重複、`IRREGULAR` に無い `worse`／`worst`／`could`、過去分詞一覧に無い `thought`・`began`・`kept`・`became`、中3 Unit 9 の whose・関係副詞の保留、使われていない `tools/gen-word-test.tpl.html` は前の回からの申し送りのままです（人の判断）。

### 飛ばした操作

- **なし。** 5フォルダを一覧し、**同名ファイルの重複が無いことを確認しました**（ルート26本＋フォルダ4つ、`units/` 37本、`tools/` 11本、`g2/` 37本、`g3/` は空）。復元は計画書類5本・`STATUS.md`・`index.html`・`word-test.html`・`tools/` の4本・`units/` の22本（`review01`〜`04`・`review-final`・`unit16`・単語帳16本）・`g2/` の23本（`index`・`review01`〜`04`・`unit15`・`unit16`・単語帳16本）の **57本**で、すべて Drive の `fileSize` とバイト数が一致しました（1回目で全部取れました）。

---

## 2026-10-11（夜の枠／JST。開始 2026-10-10 16:13 UTC ＝ 2026-10-11 01:13 JST）　順23：中2の総合テスト 第4部

手順5の判定：1番目は通過（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-N"` のキーで積む作り。中1 479語／中2 567語）。2番目は `g2/` に Unit 1〜16 の2本ずつが Drive にそろい、復元した Unit 13〜16 は `check.py 13`〜`16 --grade 2` が NG 0件。3番目は `word-test.html` に `data-g="2"` が567語あり `--word-test` が NG 0件。4番目は `--review` が `--grade 2` を受けつける（`GRADE_REVIEW_SPEC[2]` あり）。5番目で `g2/review01.html`〜`review03.html` はあり（3本とも `--review N --grade 2` が NG 0件）、`g2/review04.html` が無いので、**順23＝中2の総合テスト 第4部（Unit 13〜16）**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/review04.html` | **新規**（66,747バイト）中2 第4部の総合テスト | g2 |
| `g2/index.html` | 変更（17,267 → 17,270バイト）第4部のまとめの「総合テスト　準備中」をリンクに | g2 |
| `STATUS.md` | 変更（この記録を上に追記） | ルート |

ほかのファイル（`index.html`・`word-test.html`・`tools/check.py`・`tools/build.py`・`tools/tpl-review.html`・`tools/master-vocab.json`・`units/` の復元した18本・`g2/` の単元ファイル32本・`g2/review01`〜`review03`・計画書類）は**1バイトも変えていません**（復元直後と作業後のファイル一覧とバイト数を機械で突き合わせ、差分は上の2本だけ）。**`check.py`・`build.py`・`master-vocab.json` は今回いっさい触っていません。**

### 中身（`g2/review04.html`）

`python tools/build.py --grade 2 review 4 "第4部　比較・受動態" "Unit 13〜16" body.html` で組みました。部の名前は `UPDATE-PLAN-g2g3.md`「部の名前」のとおり。大問の構成・配点は `UPDATE-PLAN.md`「2. 総合テスト」と中2 review01〜03 と同じ（全31問・100点）。

| 大問 | 配点 | 中身 | 出題の Unit |
|---|---|---|---|
| 1 文法 | 25（2×5＋3×5） | 4択5問（higher／more useful／produced／be made of／not as heavy as）、語形変化（like the best ← good）、並べかえ2問（This book is the most helpful of the three. ／ This package was delivered by my brother yesterday.）、誤文訂正2問（not as taller as → tall／is made from stone → of） | 13〜16 |
| 2 資料つきの読解 | 18（3×6） | 3つの町（Midori・Hikari・Sakura）の人口・面積・名物の表と、アヤが留学生ルーシーに送るメッセージ **148語** | 13・14・15・16 |
| 3 対話文の読解 | 21（3・4・4・3・4・3） | 昔の道具のポスターを作るケンタと ALT のブラウン先生の対話 **157語** | 13〜16 |
| 4 条件英作文 | 10 | 社会科の校外学習、竹の工場（Plan A）か博物館の古い道具（Plan B）か。**30語以上・because を使う・比較か受動態を1回以上** | 13〜16 |
| 5 長文の読解 | 26（2×3・3×2・4・4・6） | 竹の工場を訪ねたサキのスピーチ **143語** | 13〜16 |

- 判断が要る問題は8問（英問英答5・日本語の記述2・条件英作文1）。すべてに模範解答と採点の目安があります。
- **単元の要注意事項を出題に入れました**：Unit 13 の「-er / -est と不規則（good-better-best）」（大問1 問1・問6・並べかえ the most helpful・大問2 問1・問2）と「much ＋ 比較級」（大問5 の下線部① much smaller than before）と「one of the ＋ 最上級 ＋ 複数形」（大問5 の ( 3 )）と「like 〜 the best」（大問3 の英問英答）、Unit 14 の「more / most をつける長い語」（大問1 問2・大問5 の ( 3 )）と「not as 〜 as が比較級の書き換えになる・中は原級」（大問1 問5・**誤文訂正で主語が入れ替わる書き換えを1問**・大問2 問3・大問3 問6・大問5 の ( 1 ) と英問英答）、Unit 15 の「be動詞 ＋ 過去分詞」（大問1 問3・並べかえ was delivered・大問2 の英問英答 are sold・大問5 の ( 2 ) と英問英答 are produced）と「否定の受動態」（大問3 の下線部① were not made の記述）、Unit 16 の「be made of と be made from の違い」（大問1 問4・誤文訂正）と「by 以外の前置詞」（大問2 の be known for、大問3 の be filled with、大問5 の be surprised at）。
- **語彙**：中1の479語＋中2 Unit 1〜16 の567語（計1,046語、重複を除いた見出し1,006語）の範囲で書きました。`master-vocab.json` と機械で突き合わせ、範囲外だった `year`（単数形。`"~ years old"` の形でしか入っていない）・`basket`・`social`・`wow`・`hi`・`kept`・`thought`・`began`・`became` を書きかえています（`in spring`・`cups, boxes and other things`・`history homework`・`Really?`・`Hello,`・`are not found in books`・`Then it is the oldest tool on your poster.`／`said`・`started`・`it made the room bright`）。残った範囲外は固有名詞（Midori・Hikari・Sakura・Lucy・Aya・Saki・Kenta・Ms. Brown・Japan）、表組みの実体参照（`km&sup2;` の `km`・`sup`）、日本語の解説文に出る `ALT`・`-er`・`-est`、`isn't`／`aren't`／`doesn't` の短縮形、そして **`g2/unit15_passive.html` の過去分詞一覧（33語）に載っている `sold`・`built`・`told`・`broken`** と、`check.py` の `IRREGULAR` にある `said` だけです。

### 検証結果

- `check.py --review 4 --grade 2`：**24項目 NG 0件**（375px で横スクロールなし・印刷 A4 11ページを含む）。**最初の版で NG 0件**でした。
- **中1の既存の検査はすべて NG 0件**：`--index`・`--word-test`・`--review 1`〜`4`・`--review final`、`check.py 16`。中2：`--index --grade 2`・`--review 1`〜`4 --grade 2`・`check.py 13`〜`16 --grade 2`。**作業前にも同じ検査で NG 0件のベースラインを取ってあります。**
- **playwright（Chromium・375px）**：`g2/review04.html`・`review03.html`・`review02.html`・`review01.html`・`g2/index.html`・`index.html`・`units/review04.html`・`units/review-final.html`・`word-test.html`（`?part=2-4`・`?unit=5`・`?grade=2`・`?unit=2-13`）の**12通り**で scrollWidth 375px・JS の例外0件。
- **満点の確認**：`g2/review04.html` に全31問の正解（記述は模範解答）を機械で入れて「採点する」を押し、**100点／大問ごとに 25・18・21・10・26 の満点**、結果画面の「Unit ごとの正答率」が Unit 13〜16 の4単元とも **100%**、リンク先が `unit13_comparative-er.html`〜`unit16_passive-advanced.html` になり、「見直し」の印が0件であることを確かめました。結果画面も 375px で横スクロールなし。「先生に送る（画像）」を押すと **幅1080px（1080×4369）の画像**がモーダルに出て、JS の例外0件。**回帰として `g2/review01.html`〜`review03.html` でも同じ満点テストを通しました**（3本とも100点）。

### 自分で判断したこと

1. **大問4の条件を「比較（比較級・最上級・as 〜 as）か受動態（be動詞 ＋ 過去分詞）を1回以上使う」にしました。** 中2 review01 は「because を使う」、review02 は「There is / There are か助動詞」、review03 は「不定詞か動名詞」でした。第4部の中心の形を使わせるため同じ作りにしています。書き出しは「I want to join Plan A（または Plan B）」で、`data-avoid` には more better／most oldest／as cheaper as／is made by wood など、第4部でよく出る誤りの形を入れています。模範解答は Plan A（40語）・Plan B の両方を載せました。
2. **誤文訂正の1問を「比較級 ↔ not as 〜 as の書き換え」にしました**（`Kenta is taller than Aya.` ＝ `Aya is not as taller as Kenta.` → `tall`）。`PLAN-g2g3.md` 3節 Unit 14 の「書き換え問題は主語が入れ替わるので誤文訂正で必ず1問出す」に合わせたものです。
3. **過去分詞・過去形は `g2/unit15_passive.html` の一覧（33語）と `units/unit16_general-past.html` の不規則変化（22語）に載っているものだけを使いました。** `thought`（think）・`began`（begin）・`kept`（keep）はどちらの表にも無いので、`said`・`started`・`are not found` に書きかえています。`became` も表に無いため `it made the room bright` にしました（`check.py` の `IRREGULAR` には `became` がありますが、生徒が表で見ていない形は避けました）。
4. **大問3の下線部①を「Metal tools were not made at that time.」にしました。** 受動態の否定を日本語で説明させる問題で、`PLAN-g2g3.md` Unit 15 の「be動詞 ＋ 過去分詞」が否定でも読めるかを見ます。要点は「金属（の道具）」と「作られていなかった」の2つです。
5. **大問2の表の面積に `km&sup2;` を使いました。** 外部読み込みを増やさずに上付きの2を出すためで、実体参照なので検査の「外部読み込みは Google Fonts だけ」に影響しません。
6. 中3の形（現在完了・`too 〜 to`・`want 人 to`・間接疑問・関係代名詞・仮定法・付加疑問）は使っていません。`has been`・`the 名詞 which`・`told us to` が無いことは検査でも確認しました。

### 気になった点（次の回への申し送り）

- **次は順24＝中2の総まとめテスト（`g2/review-final.html`、Unit 1〜16 の全範囲）です。** 要るもの：`tools/tpl-review.html`、`units/review-final.html`（見本）、`g2/review04.html`（直前の見本）、`g2/index.html`、そして**中2 Unit 1〜16 の単語帳16本**（語彙の範囲を機械で突き合わせるため）。読解は120〜160語、条件英作文は30語以上（`GRADE_REVIEW_SPEC[2]["final"]` は `((1,16),(120,160),30)`）。`build.py` の呼び方は `python tools/build.py --grade 2 review final "中2の総まとめ" "Unit 1〜16" body.html`、単語テストへのリンクは `?grade=2` になります。
- **総まとめは Unit 1〜16 の全部を `data-unit` に入れる必要があります**（検査の「範囲の Unit がすべて出題に入っている」が16単元ぶんを見ます）。31問で16単元を覆うので、読解問題の `data-unit` に複数の Unit を並べる形（`data-unit="13 15"` など）を多めに使うことになります。
- **語彙の範囲外でつまずきやすい語**（今回新しく分かったもの）：`year`（単数形は入っていない。`years` は `"~ years old"` の形で入っている）・`basket`・`social`・`wow`・`hi`（`hello` は Unit 1 にあります）。前の回からの申し送りは `alone`・`already`・`also`・`well`（副詞）・`meaning`・`cap`・`hall`・`center`・`top`・`back`・`course` です。
- **過去分詞・過去形で表に無い語**：`thought`（think）・`began`（begin）・`kept`（keep）・`became`（become）。`g2/unit15_passive.html` の一覧にも `units/unit16_general-past.html` の不規則変化にも載っていないので、総合テストの本文では避けてください（`said`・`started` は使えます）。**`g2/unit15_passive.html` の過去分詞一覧に `keep`・`think`・`begin`・`become` を足すかどうかは人の判断**だと思い、今回は触っていません。
- 総合テストの本文は、`master-vocab.json` の `"1"`〜`"16"` ＋ `"g2-1"`〜その部の最後のキーから語を集め、語形（-s・-ed・-ing・-er・-est・子音重ね・y→ier）を戻して照合すると速いです。代名詞・be動詞・冠詞・数詞・前置詞はキーに入っていないので、出てきても範囲外ではありません。
- **playwright で `file://` のページを開くと、Google Fonts が読めずに `net::ERR_TUNNEL_CONNECTION_FAILED` のコンソールエラーが1件出ます。** これはこの実行環境の外向き通信の制限で、ページの不具合ではありません（中1の触っていないページでも同じように出ます）。`page.route` で `fonts.googleapis.com` を空の CSS に差し替えてから測ると0件になります。JS の例外（`pageerror`）は差し替えの前後どちらも0件でした。
- `g2/vocab12_gerund.html` の `take part in 〜` の重複、`IRREGULAR` に無い `worse`／`worst`／`could`、中3 Unit 9 の whose・関係副詞の保留、使われていない `tools/gen-word-test.tpl.html` は前の回からの申し送りのままです（人の判断）。

### 飛ばした操作

- **なし。** 5フォルダを一覧し、**同名ファイルの重複が無いことを確認しました**（ルート27本、`units/` 37本、`tools/` 11本、`g2/` 33本、`g3/` は空）。復元は計画書類5本・`STATUS.md`・`index.html`・`word-test.html`・`tools/` の4本（`build.py`・`check.py`・`master-vocab.json`・`tpl-review.html`）・`units/` の18本（`review01`〜`04`・`review-final`・単語帳16本のうち16本・`unit16`）・`g2/` の28本（`index`・`review01`〜`03`・Unit 13〜16 のワークブック4本・単語帳16本）の **56本**で、すべて Drive の `fileSize` とバイト数が一致しました（1回目で全部取れました）。
- **`units/` の単語帳16本と `units/unit16_general-past.html` は、最初は落としていませんでした。** そのため `--word-test` が6件 NG、`--index --grade 2` が1件 NG になりました（どちらも「単語帳が無い」「中1に単元が1本も無い」と判定されるため）。**復元していないだけの見かけの NG で、ファイルの中身の問題ではありません。** 中1の既存の検査を毎回確かめるには、`--word-test` に**全学年の単語帳**、`--index --grade 2` の学年切り替えの判定に**`units/unit??_*.html` が1本以上**要ります。次の回も同じところで止まらないよう、最初からこの2つを復元してください。

---

## 2026-10-10（昼の枠／JST。開始 2026-10-10 06:08 UTC ＝ 15:08 JST）　順22：中2の総合テスト 第3部

手順5の判定：1番目は通過（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-N"` のキーで積む作り。中1 479語／中2 567語）。2番目は `g2/` に Unit 1〜16 の2本ずつが Drive にそろい、復元した Unit 9〜16 は `check.py 9`〜`16 --grade 2` が NG 0件。3番目は `word-test.html` に `data-g="2"` があり `--word-test` が NG 0件。4番目は `--review` が `--grade 2` を受けつける（`GRADE_REVIEW_SPEC[2]` あり）。5番目で `g2/review01.html`・`review02.html` はあり（どちらも `--review N --grade 2` が NG 0件）、`g2/review03.html` が無いので、**順22＝中2の総合テスト 第3部（Unit 9〜12）**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/review03.html` | **新規**（65,676バイト）中2 第3部の総合テスト | g2 |
| `g2/index.html` | 変更（17,264 → 17,267バイト）第3部のまとめの「総合テスト　準備中」をリンクに | g2 |
| `STATUS.md` | 変更（この記録。ファイルを分割） | ルート |
| `STATUS-archive-2026-10-10.md` | 改名（前の `STATUS.md` を Drive 上で `update_file` により改名。中身は変えていない） | ルート |

ほかのファイル（`index.html`・`word-test.html`・`tools/check.py`・`tools/build.py`・`tools/tpl-review.html`・`tools/master-vocab.json`・`units/` の37本・`g2/` の単元ファイル・計画書類）は**1バイトも変えていません**（復元直後と作業後のファイル一覧とバイト数を機械で突き合わせ、差分は上の2本だけ）。**`check.py` は今回いっさい触っていません。**

### 中身（`g2/review03.html`）

`python tools/build.py --grade 2 review 3 "第3部　不定詞・動名詞" "Unit 9〜12" body.html` で組みました。部の名前は `UPDATE-PLAN-g2g3.md`「部の名前」のとおり。大問の構成・配点は `UPDATE-PLAN.md`「2. 総合テスト」と中2 review01・02 と同じ（全31問・100点）。

| 大問 | 配点 | 中身 | 出題の Unit |
|---|---|---|---|
| 1 文法 | 25（2×5＋3×5） | 4択5問（wants to be／enjoys playing／to read（目的）／how to get／stopped playing）、語形変化（Thank you for helping）、並べかえ2問（I have a lot of homework to do today. ／ I was happy to see my old friend.）、誤文訂正2問（wants to goes → go／finished to clean → cleaning） | 9〜12 |
| 2 資料つきの読解 | 18（3×6） | 料理部の「Japanese Cooking Day」の予定表（時刻・すること・料金）と、ユキが留学生エマに送るメッセージ **129語** | 9・11・12 |
| 3 対話文の読解 | 21（3・4・4・3・4・3） | エンジニアになりたいケンと ALT のブラウン先生の対話 **147語** | 9〜11 |
| 4 条件英作文 | 10 | 夏休みの活動、料理教室（Plan A）か海岸のごみ拾い（Plan B）か。**30語以上・because を使う・書き出しの want to のほかに不定詞か動名詞を1回以上** | 9〜12 |
| 5 長文の読解 | 26（2×3・3×2・4・4・6） | オーストラリアでのホームステイについてのリクのスピーチ **142語** | 9〜12 |

- 判断が要る問題は8問（英問英答5・日本語の記述2・条件英作文1）。すべてに模範解答と採点の目安があります。
- **単元の要注意事項を出題に入れました**：Unit 9 の「to のうしろは原形」（大問1 問1・誤文訂正・英問英答2問）、Unit 10 の「目的（〜するために）と原因（〜して）」（大問1 問3＝目的・並べかえ＝原因・大問3 の記述＝目的・Why に To 〜で答える英問英答・大問5 の ( 2 )＝原因）、Unit 11 の「名詞のうしろから説明する to」（並べかえ homework to do・( B ) の books to read）と「疑問詞＋to」（大問1 問4・大問5 の ( 1 ) what to say・英問英答 how to cook）、Unit 12 の「enjoy / finish / stop は動名詞」（大問1 問2・問5・誤文訂正 finished to clean）、「前置詞のうしろは動名詞」（Thank you for helping・look forward to cooking）、「stop 〜ing（やめる）」（大問1 問5）、「動名詞の主語は単数」（大問5 の英問英答 Is learning 〜? → No, it isn't.）。
- **語彙**：中1の479語＋中2 Unit 1〜12 の語の範囲で書きました。`master-vocab.json` と機械で突き合わせ、範囲外だった `alone`・`already`・`also`・`meaning`・`cap`・`well`（副詞）を書きかえています（`he can't walk fast`・`Ken knows`・`And you should`・`it is not a good gesture`・`a hat`）。残った範囲外は固有名詞（Emma・Yuki・Ken・Riku・Ms. Brown・Australia・Canada・Japan・October）と代名詞・be動詞・数詞などの基本語だけです。

### 検証結果

- `check.py --review 3 --grade 2`：**24項目 NG 0件**（375px で横スクロールなし・印刷 A4 11ページを含む）。**最初の版で NG 0件**でした。
- **中1の既存の検査はすべて NG 0件**：`--index`・`--word-test`・`--review 1`〜`4`・`--review final`、`check.py 1`〜`16`。中2：`--index --grade 2`・`--review 1`〜`3 --grade 2`・`check.py 9`〜`16 --grade 2`。**作業前にも同じ検査で NG 0件のベースラインを取ってあります。**
- `check.py 1`〜`8 --grade 2` は「ファイルが見つかりません」で NG 1件になりますが、これは今回の工程に要らないので `g2/unit01`〜`unit08` のワークブックを復元していないだけです（Drive には32本そろっていて、1バイトも触っていません）。
- **playwright（Chromium・375px）**：`g2/review03.html`・`g2/review02.html`・`g2/review01.html`・`g2/index.html`・`index.html`・`units/review03.html`・`units/review-final.html`・`word-test.html`（`?part=2-3`・`?unit=5`・`?grade=2`）の**10通り**で scrollWidth 375px・JS の例外0件。
- **満点の確認**：`g2/review03.html` に全31問の正解（記述は模範解答）を機械で入れて「採点する」を押し、**100点／大問ごとに 25・18・21・10・26 の満点**、結果画面の「Unit ごとの正答率」が Unit 9〜12 の4単元とも100%、リンク先が `unit09_infinitive-noun.html`〜`unit12_gerund.html` になることを確かめました。結果画面も 375px で横スクロールなし。**回帰として `g2/review01.html`・`review02.html` でも同じ満点テストを通しました**（どちらも100点）。
  - 中1の `units/review03.html`・`review-final.html` は同じ自動入力で 95点・94点でした。これは**今回の自動入力スクリプトが中1の模範解答の書き方（複数の要点を「／」で並べる形など）に合わせていないため**で、中1のファイルは1バイトも変えていません（JS の例外は0件）。前の回までに中1は満点テストを通してあります。

### 自分で判断したこと

1. **大問4の条件を「書き出しの want to のほかに、不定詞か動名詞を1回以上使う」にしました。** 中2 review01 は「because を使う」、review02 は「There is / There are か助動詞を1回以上」でした。第3部の中心の形を使わせるため同じ作りにしています。書き出しを「I want to join Plan A（または Plan B）」にしたので、書き出しの want to は数えない、と条件に明記しました。`data-avoid` には enjoy to／finish to／want to joins／good at cook／looking forward to go など、第3部でよく出る誤りの形を入れています。模範解答は Plan A（38語）・Plan B の両方を載せました。
2. **Unit 10 の出題を「目的」と「原因」の両方に分けました。** 大問1 問3・大問3 の記述・英問英答が「〜するために」、並べかえと大問5 の ( 2 ) が「〜して（うれしい）」です。
3. **大問5の英問英答に「Is learning a foreign language easy for Riku? → No, it isn't.」を置きました。** 動名詞のかたまりが主語のとき単数で受けることを見る問題で、No, they aren't を誤りの形にしています。`PLAN-g2g3.md` 3節 Unit 12 に明記はありませんが、動名詞の主語（`Learning 〜 is`）を本文で使ったので、その確認として入れました。
4. **資料（大問2）の日付を「Saturday, October 24」にしました。** 2026年10月24日は土曜日です。
5. 比較（Unit 13〜）・受動態（Unit 15〜）は使っていません。`than`・`better`・`more 〜`・`as 〜 as`・`be 〜ed by` が無いことは検査でも確認しました。

### 気になった点（次の回への申し送り）

- **次は順23＝中2の総合テスト 第4部（`g2/review04.html`、Unit 13〜16）です。** 要るもの：`tools/tpl-review.html`、`units/review04.html`（見本）、`g2/review03.html`（直前の見本）、`g2/unit13`〜`unit16` と `g2/vocab13`〜`vocab16`、`g2/index.html`。読解は120〜160語、条件英作文は30語以上。
- **第4部で比較・受動態が範囲内に入ります。** 中3の形（現在完了 `have + 過去分詞`・`too 〜 to`・`want 人 to`・間接疑問・関係代名詞・仮定法・付加疑問）は使わないでください。**受動態の `have been` や `has 〜ed` は現在完了として NG になる**ので注意（`LATER_GRAMMAR_G2` の 99 番）。`which` を関係代名詞として使わない（`the 名詞 which` が NG）。
- **語彙の範囲外でつまずきやすい語**（中1＋中2 Unit 1〜12 で確認したもの）：`alone`・`already`・`also`・`well`（副詞）・`meaning`・`cap`・`hall`・`center`・`top`・`back`・`course`。`also` は使いたくなるので、`And 〜`・`〜, too` で書きかえると早いです。
- 総合テストの本文は、`master-vocab.json` の `"1"`〜`"16"` ＋ `"g2-1"`〜その部の最後のキーから語を集め、語形（-s・-ed・-ing・子音重ね）を戻して照合すると速いです。代名詞・be動詞・冠詞・数詞・前置詞はキーに入っていないので、出てきても範囲外ではありません。
- `g2/vocab12_gerund.html` の `take part in 〜` の重複、`IRREGULAR` に無い過去分詞・`worse`／`worst`／`could`、中3 Unit 9 の whose・関係副詞の保留、使われていない `tools/gen-word-test.tpl.html` は前の回からの申し送りのままです（人の判断）。

### 飛ばした操作

- **なし。** 5フォルダを一覧し、**同名ファイルの重複が無いことを確認しました**（ルート25本、`units/` 37本、`tools/` 11本、`g2/` 33本、`g3/` は空）。復元は計画書類5本・`STATUS.md`・`index.html`・`word-test.html`・`tools/` の4本（`build.py`・`check.py`・`master-vocab.json`・`tpl-review.html`）・`units/` の37本・`g2/` の27本（`index`・`review01`・`review02`・Unit 9〜16 のワークブック8本・単語帳16本）の **76本**で、すべて Drive の `fileSize` とバイト数が一致しました（1回目で全部取れました）。

---

## Drive からの復元（毎回この方法で通っています）

- サブエージェントに `download_file_content` だけを呼ばせ（1体に3〜4本。モデルは haiku で足ります）、`~/.claude/projects/<作業ディレクトリ>/<セッションID>/subagents/**/*.jsonl` と `tool-results/*.txt` から長い base64 の連なりを正規表現（`[A-Za-z0-9+/]{2000,}={0,2}`）で拾って復号。**復号した長さが Drive の `fileSize` と一致したものだけ書き出す。**
- **サブエージェントが「大きすぎて返せなかった」と報告しても、記録側（`tool-results/*.txt`）には残っています。** 失敗扱いにせず、復号を試してください。親セッションで直接 `download_file_content` を呼んでも、大きいファイルは `tool-results/*.txt` に保存されるので同じ方法で復号できます。
- **ファイルの対応づけは「復号後のバイト数」で行うのが確実です**（タイトルは `index.html` がルートと g2 で重複し、ファイルIDは `__` を含むものがある）。落とす前に `search_files` で全件のサイズを控えておき、サイズが重複しないことを確かめてから落とします。
- `search_files` は1ページ5件ほどしか返さないので `nextPageToken` で全件を取る（`units` は8ページ）。一覧だけをサブエージェントに取らせ、「タイトル／ファイルID／サイズ」のタブ区切りで返させると速いです。

## Drive へのアップロード

- アップロードは `create_file` の `textContent` を使う（`base64Content` は長いと崩れる）。`disableConversionToGoogleType: true` と、`contentMimeType`（`text/html`・`text/x-python`・`application/json`・`text/markdown`）を付ける。
- アップロード後、Drive の `fileSize` とローカルのバイト数が一致することを確かめてから、同名の古いファイルを `trash_file` でゴミ箱に移す。
- STATUS.md が約45KBを超えそうなときは、古い版を `update_file` で `STATUS-archive-日付.md` に改名し、新しい STATUS.md を立てる（この2節を書き写す）。
