# 制作の記録

> **2026-10-12（夜）にこのファイルを分割しました。** 新しい記録は上に足しています（最新は 2026-10-13（夜）の順27：中3 Unit 2）。2026-10-11（昼）の順24：中2の総まとめテスト、10-11（夜）の順23：第4部、10-10（昼）の順22：第3部の記録は `STATUS-archive-2026-10-11.md` にそのまま入っています。それより前は `STATUS-archive-2026-10-10.md`、`STATUS-archive-2026-10-08.md`、`STATUS-archive-2026-10-07.md`、`STATUS-archive-2026-10-06.md`、`STATUS-archive-2026-10-05.md`、`STATUS-archive-2026-10-03.md`、`STATUS-archive-2026-10-02.md`、`STATUS-archive-2026-10-01.md`、`STATUS-archive-2026-09-30.md`、`STATUS-archive-2026-09-28.md`、`STATUS-archive-2026-09-26.md`、`STATUS-archive-2026-09-24.md`、`STATUS-archive-2026-09-23-night.md`、`STATUS-archive-2026-09-23.md`、`STATUS-archive-2026-09-22.md`、`STATUS-archive-2026-09.md` です。
>
> 手順は前回と同じで、**古い `STATUS.md` を `update_file` で `STATUS-archive-2026-10-11.md` に改名し、この新しい `STATUS.md` を置いています。** アーカイブ側の中身は1バイトも触っていません。リポジトリに反映するときは、改名されたアーカイブとこの新しい `STATUS.md` の両方を置いてください。「Drive からの復元」「Drive へのアップロード」の要点は下に書き写してあります。

---

## 2026-10-13（夜の枠／JST。開始 2026-10-12 16:13 UTC ＝ 2026-10-13 01:13 JST）　順27：中3 Unit 2「現在完了（完了・結果）」

手順5の判定：1番目は通過（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-N"` のキーで積む作り。中1 479語／中2 567語）。2番目は `g2/` に Unit 1〜16 の2本ずつが Drive にそろい、復元した Unit 1・16 は `--grade 2` で NG 0件。3番目は `word-test.html` に `data-g="2"` があり `--word-test` が NG 0件。4番目は `GRADE_REVIEW_SPEC[2]` あり。5・6番目は `g2/review01`〜`04`・`review-final` が NG 0件。7番目は `g3/index.html` あり・`LATER_GRAMMAR_G3` あり。8番目で N=1 は2本そろって NG 0件、**N=2 で `g3/unit02_*.html` が無い**ので、**順27＝中3 Unit 2** です。N=9 ではないので whose・関係副詞の判断は要りませんでした。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g3/unit02_perfect-result.html` | **新規**（49,604バイト）ワークブック。31問（A6・B6・C5・D7・E5・F2） | **g3** |
| `g3/vocab02_perfect-result.html` | **新規**（37,562バイト）単語帳。見出し語35語 | **g3** |
| `g3/index.html` | 変更（15,875 → 15,931バイト）Unit 2 のワークブック・単語帳をリンクに（単語テストは順41まで準備中） | g3 |
| `tools/check.py` | 変更（84,023 → 84,650バイト）`IRREGULAR` に `stood` → `stand` を追加、冒頭の履歴に追記 | tools |
| `tools/master-vocab.json` | 変更（10,766 → 11,134バイト）`"g3-2"` に35語を追加。中1・中2・`"g3-1"` のキーは1語も変えていない（前後で機械で一致を確認） | tools |
| `STATUS.md` | 変更（この記録） | ルート |

ほかの復元ファイル（`index.html`・`g2/index.html`・`word-test.html`・`build.py`・テンプレート2本・`units/` の22本・`g2/` の23本・`g3/` の2本・計画書類5本）は**1バイトも変えていません**（復元直後と作業後の md5 を機械で突き合わせ、差分は上の表の5本だけ＝無変更57件）。**`index.html` と `g2/index.html` は触っていません**（ヘッダーの「中3」は順26でリンクにしてあるため、この回では変える分がありません）。

### 中身

- **新出語35語**（めやす30〜40語）。動詞 `announce`・`decorate`・`reserve`・`select`、副詞 `just`・`already`・`yet`・`nearly`、名詞 `program`・`preparation`・`curtain`・`costume`・`decoration`・`ceiling`・`drum`・`drummer`・`theater`・`score`・`interview`・`headline`・`delivery`・`guest`・`mall`・`platform`・`parcel`・`taxi`・`subway`・`bicycle`・`coffee`、熟語 `not 〜 yet`・`just now`・`have gone to 〜`・`come back`・`put up 〜`・`sold out`。累計は中1 479語＋中2 567語＋中3 68語＝1,114語（重複を除くと1,113語）。
- **読解本文は学級新聞の記事「文化祭まで一週間」159語**（めやす130〜180語）。終わった準備と終わっていない準備を読み分ける内容で、完了・結果の用法と中3 Unit 1 までの文法だけで書きました。
- 解説：過去形との対比（`I did my homework.` ↔ `I have done my homework.`）→ **なぜ同じ形で意味が変わるか**（「持っている」中身が回数なら経験、作業の終わりなら完了）→ `just`・`already`・`yet` の意味・使う文・位置の表 → **いろいろな場面の例文（4段落16本）** → **`yet` が疑問文で「もう」、否定文で「まだ」になることを `transform` の図解と表で分ける** → **「完了」と「結果」は分けなくてよい**（下の判断1）→ `have gone to 〜` と `have been to 〜` の対比表 → 手順 → 境界（`just` と `just now`、過去の時を表す語、疑問文の `already`、`yet` と `never`）→ 入試での出方 → よくある間違い4件 → まとめ。

### 検証結果

- **`check.py 2 --grade 3`：17項目 NG 0件**（語の網羅 未収録0語・例文の一致 不一致0件・375px で横スクロールなし・A4 ワークブック16ページ／単語帳4ページ）。
- **`LATER_GRAMMAR_G3` で first が3以上の形を、ワークブックと単語帳の全文（設問・解答・読解を含む）に機械でかけて0件**。Unit 3 の継続（`since`／`for`＋期間）と現在完了進行形も使っていません（`since` は本文に1語も出てきません）。
- **中1の既存の検査はすべて NG 0件**：`--index`・`--word-test`・`--review 1`〜`4`・`--review final`・`check.py 1`。**中2もすべて NG 0件**：`--index --grade 2`・`--review 1`〜`4 --grade 2`・`--review final --grade 2`・`check.py 1 --grade 2`・`check.py 16 --grade 2`。**中3**は `--index --grade 3`・`check.py 1 --grade 3`・`check.py 2 --grade 3` が NG 0件。**合計19通りを、作業前（復元直後）と作業後の2回実行して、どちらも NG 0件**でした。
- **playwright（Chromium・375px、Google Fonts は空の CSS に差し替え）**：`g3/unit02`・`g3/vocab02`・`g3/unit01`・`g3/vocab01`・`g3/index.html`・`g2/index.html`・`index.html`・`units/review01.html`・`units/review-final.html`・`g2/review01.html`・`g2/review-final.html`・`word-test.html`（`?g=1`・`?g=2`・`?unit=5`・`?unit=2-5`・`?part=2-1`）の**16通り**で、`details` をすべて展開した状態も含めて scrollWidth 375px・JS の例外0件・console エラー0件。
- 新しい2本は `<script>` 0件、外部読み込みは Google Fonts だけ（ほか0件）。

### 自分で判断したこと

1. **「完了」と「結果」を分けさせない方針を、独立した節（h2）にして明記しました。** `PLAN-g2g3.md` 4節の中3 Unit 2 に「『完了』と『結果』を無理に分類させない（設問では区別を問わない）方針を解説に書く」とあるので、表で2つの言い方を並べて見せたうえで、「この教材では2つを分けて答えさせる問題は出しません」「大事なのは『今どうなっているか』を日本語に表すこと」と書きました。設問にも用法名を答えさせる問題は置いていません。
2. **`yet` の2つの意味は、`transform` の図解（同じ文を疑問文→否定文に変える）と4行の表の両方で分けました。** 同節の「図解で分ける」の指示に対し、図解だけだと例が1組しか示せないためです。あわせて「`yet` は終わったか／終わっていないかをたずねる語で、文の形が意味を決めている」という覚え方を1段落で書きました。
3. **`check.py` の `IRREGULAR` に `stood` → `stand` を足しました。** 読解本文の `I have never stood on a stage before.` で、`stand`（中1 Unit 12 の `stand up` で既出）の過去分詞 `stood` の寄せ先が無く、語の網羅が1語 NG になったためです。**追加前は未収録の語なので、中1・中2の検査結果は変わりません**（追加の前後で上の19通りを再実行して確認）。`stand` は既出なので新出語には立てていません。
4. **並べ替え（パートB）の6問目を「アヤは」から「私の姉は」に書き換えました。** 並べ替えの語群は文頭も小文字で示す決まりなので `[ aya / has / ... ]` となり、`check.py` の語の網羅が小文字の `aya` を固有名詞と見分けられずに NG になります。中1・中2・中3 Unit 1 の並べ替えも固有名詞を使っていないので、同じ扱いにそろえました（`Aya` は大文字で出てくる解説・パートC・読解ではそのまま使っています）。
5. **`reporter`・`glasses`・`sold` は新出語に立てていません。** `report`・`glass`・`sell` が既出で、`check.py` の `lemma` がそこへ寄せるため、語の網羅には出てきません。ただし `sold out` は決まった言い方なので熟語として1件立てました。
6. **`drum` と `drummer` を別の見出し語にしました。** 綴りの作り方（`m` を重ねる）が入試で問われる形なので、`drummer` 側に「綴り注意」のバッジを付けて独立させました。
7. **単語テストのボタンは「準備中」のままです**（順41まで）。`g3/index.html` の共通リンクの「単語テスト（中3）」も準備中のままです。

### 気になった点（次の回への申し送り）

- **次は順28＝中3 Unit 3（現在完了（継続）と現在完了進行形。スラッグ `perfect-continue`）です。** 要るもの：このワークブックと単語帳（`g3/unit02_perfect-result.html`・`g3/vocab02_perfect-result.html`。書きぶりの見本）、`tools/tpl-workbook.html`・`tools/tpl-vocab.html`。新出語は累計1,114語との差分で、`"g3-3"` のキーに積みます。
- Unit 3 で使う `since`・`for`（期間）・`How long 〜?`・`have been 〜ing` は、この単元では1度も使っていません。`since` は `master-vocab.json` にも `BASIC` にも無い語なので、Unit 3 の新出語になります。
- **`whose`・関係副詞は `UPDATE-PLAN-g2g3.md` で「保留」のままです。** 判断が要るのは中3 Unit 9（順34）の前です。`PLAN-g2g3.md` 4節の Unit 12 には「whose は扱わない」とありますが、最優先の `UPDATE-PLAN-g2g3.md` は保留なので、**和歌山の過去問での出題の有無を人が確かめて決める必要があります。**
- **この STATUS.md は約36KBです。次の回の記録を足すと約45KBを超える見込みなので、次の回は先に `update_file` で `STATUS-archive-2026-10-13.md` に改名し、新しい `STATUS.md` を立ててください**（「Drive からの復元」「Drive へのアップロード」の2節を書き写すこと）。
- ［参考］の「解説に出ていない出題語」が16語（中3 Unit 1 は13語）あります。どれも既出語で NG ではありませんが、`drum`・`concert`・`plates`・`city` などは設問と読解だけに出てくる語です。
- `g2/vocab12_gerund.html` の `take part in 〜` の重複、`IRREGULAR` に無い `worse`／`worst`／`could`、過去分詞一覧に無い `thought`・`began`・`kept`・`became`、`video`・`year`（単数形）・`hi` が `master-vocab.json` にも `BASIC` にも無いこと、使われていない `tools/gen-word-test.tpl.html` は前の回からの申し送りのままです（人の判断）。

### 飛ばした操作

- **なし。** 5フォルダを一覧し、**同名ファイルの重複が無いことを確認しました**（ルート28本、`units/` は今回 vocab16本・review5本・unit01 を確認、`tools/` 11本、`g2/` 37本、`g3/` 3本）。復元は計画書類5本・`STATUS.md`・`index.html`・`word-test.html`・`tools/` の5本（`build.py`・`check.py`・`master-vocab.json`・`tpl-workbook.html`・`tpl-vocab.html`）・`units/` の22本（単語帳16本・`review01`〜`04`・`review-final`・`unit01`）・`g2/` の23本（`index`・単語帳16本・`review01`〜`04`・`review-final`・`unit01`・`unit16`）・`g3/` の3本（`index`・`unit01`・`vocab01`）の **61本**で、すべて Drive の `fileSize` とバイト数が一致しました。`check.py`・`word-test.html`・`review*.html`・`g2/unit01`・`g2/unit16`・`g3/unit01` などはサブエージェントが「大きすぎて返せなかった」と報告しましたが、`tool-results/*.txt` に残っていたので復号できました（下の節の要点どおり）。

---

## 2026-10-12（昼の枠／JST。開始 2026-10-12 06:08 UTC ＝ 15:08 JST）　順26：中3 Unit 1「現在完了（経験）」

手順5の判定：1番目は通過（`g2/index.html` あり・`--grade` あり・`"g2-N"` キー）。2番目は `g2/` に Unit 1〜16 の2本ずつがそろい、復元した Unit 1・16 は `--grade 2` で NG 0件。3番目は `data-g="2"` あり・`--word-test` NG 0件。4番目は `GRADE_REVIEW_SPEC[2]` あり。5・6番目は `g2/review01`〜`04`・`review-final` がそろい NG 0件。7番目は `g3/index.html` あり・`LATER_GRAMMAR_G3` あり。8番目で **`g3/unit01_*.html` が無い**ので、**順26＝中3 Unit 1** です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g3/unit01_perfect-experience.html` | **新規**（55,580バイト）ワークブック。31問（A6・B6・C5・D7・E5・F2） | **g3** |
| `g3/vocab01_perfect-experience.html` | **新規**（35,798バイト）単語帳。見出し語33語 | **g3** |
| `g3/index.html` | 変更（15,811 → 15,875バイト）Unit 1 のワークブック・単語帳をリンクに（単語テストは順41まで準備中） | g3 |
| `index.html` | 変更（17,197 → 17,176バイト）ヘッダーの「中3」をリンクに（`g3/index.html`） | ルート |
| `g2/index.html` | 変更（17,277 → 17,259バイト）ヘッダーの「中3」をリンクに（`../g3/index.html`） | g2 |
| `tools/check.py` | 変更（81,705 → 84,023バイト）`IRREGULAR`・`CONTRACTIONS` に現在完了の形を追加、`--word-test` の学年の扱いを修正（下の判断3）、冒頭の履歴に追記 | tools |
| `tools/master-vocab.json` | 変更（10,439 → 10,766バイト）`"g3-1"` に33語を追加。中1・中2のキーは1語も変えていない（前後で機械で一致を確認） | tools |
| `STATUS.md` | 変更（この記録） | ルート |

ほかの復元ファイル（`word-test.html`・`build.py`・テンプレート2本・`units/` 23本・`g2/` のほかの22本・計画書類4本）は**1バイトも変えていません**（復元直後と作業後の md5 を機械で突き合わせ）。

### 中身

- **新出語33語**（めやす30〜40語）。動詞 `shake`、副詞 `ever`、名詞（`life`・`top`・`sunset`・`sunrise`・`tent`・`trail`・`bear`・`insect`・`feeling`・`whale`・`panda`・`koala`・`kangaroo`・`camel`・`desert`・`ocean`・`volcano`・`turtle`・`snake`・`medal`・`kimono`・`sushi`・`fish`）、形容詞 `gold`・`raw`・`wild`、熟語 `have been to 〜`・`how many times 〜?`・`in my life`・`shake hands with 〜`・`hear of 〜`。累計は中1 479語＋中2 567語＋中3 33語＝1,079語。
- **読解本文はスピーチ「山の上の夜」160語**（めやす130〜180語）。経験の用法と中2までの文法だけで書きました。
- 解説：have／has＋過去分詞（なぜ have か・主語での選び方）→ **過去分詞の一覧表（中2 Unit 15 の3表をそのまま再掲）＋この単元で足す形**（been・met・flown・ridden・swum・worn・climbed・touched・shaken）→ 経験を表す語と位置（ever・never・before・once・twice・〜 times・many times）と例文 → 否定文・疑問文と答え方（**Yes, I have. ／ No, I haven't. ／ No, never.**、How many times）→ **have been to を独立説明** → 手順 → 境界（2つの have、過去の時を表す語とは使わない、been to と gone to、once の2つの意味）→ 入試での出方 → よくある間違い → まとめ。

### 検証結果

- **`check.py 1 --grade 3`：17項目 NG 0件**（語の網羅 未収録0語・例文の一致 不一致0件・375px で横スクロールなし・A4 ワークブック19ページ／単語帳4ページ）。
- **`LATER_GRAMMAR_G3` で first が2以上の形を、ワークブック全文（設問・解答・読解を含む）に機械でかけて0件**。完了・結果（just／already／yet）と継続（since／for＋期間）の現在完了も使っていません。
- **中1の既存の検査はすべて NG 0件**：`--index`・`--word-test`・`--review 1`〜`4`・`--review final`・`check.py 1`。**中2もすべて NG 0件**：`--index --grade 2`・`--review 1`〜`4 --grade 2`・`--review final --grade 2`・`check.py 1 --grade 2`・`check.py 16 --grade 2`。`--index --grade 3` も NG 0件。作業前（復元直後）にも同じ検査で NG 0件のベースラインを取りました。
- **playwright（Chromium・375px、Google Fonts は空の CSS に差し替え）**：`g3/unit01`・`g3/vocab01`・`g3/index.html`・`g2/index.html`・`index.html`・`units/review-final.html`・`g2/review01.html`・`g2/review-final.html`・`word-test.html`（`?g=1`・`?g=2`・`?unit=5`・`?unit=2-5`）の**12通り**で scrollWidth 375px・JS の例外0件。

### 自分で判断したこと

1. **過去分詞の一覧表は中2 Unit 15 の3表を1行も変えずに再掲し、そのうしろに「この単元で足す形」の表（be-been、meet-met、fly-flown、ride-ridden、swim-swum、wear-worn、climb、touch、shake-shaken）を別に置きました。** `PLAN-g2g3.md` の「中2 Unit 15 のものを再掲する」を守りつつ、経験の文で要る形を足すためです。
2. **`check.py` の `IRREGULAR` に been・gone・flew/flown・rode/ridden・swam/swum・wore/worn・shook/shaken を、`CONTRACTIONS` に haven't・hasn't・I've・you've・we've・they've を足しました。** 中2の各単元と同じやり方です。どれも追加前は未収録の語なので、中1・中2の検査結果は変わりません（上の再実行で確認）。
3. **`--word-test` の検査を直しました。** 中3の単語帳ができた時点で、`--word-test` が「中3の語が一覧に無い」など8件 NG になりました（順18で作った検査が「単語帳のある学年はすべて一覧と突き合わせる」作りだったため）。このままだと**次の回の手順5の3番目（`--word-test` が NG → 順18）に当たって工程が逆戻りする**ので、**単語テストにまだ `data-g="3"` が無い学年は突き合わせから外して［参考］に出す**ようにしました（目次の `wt_ready()` と同じ判定。中3のボタンが disabled・準備中であることは引き続き見ています）。中1・中2の突き合わせは変えていません。順41で中3の語を足せば、自動的に中3も突き合わせの対象に戻ります。
4. **「〜へ行ったことがある」の境界事例として `has gone to`（Unit 2 の結果の用法）を解説で1文だけ示し、誤文訂正で1問（gone→been）出しました。** `PLAN-g2g3.md` の「been to を独立説明」には gone to との区別が欠かせないためです。意味の説明は「行ってしまって今ここにいない（Unit 2 で扱う）」にとどめ、gone to を正解にする設問は置いていません。
5. **「過去の時を表す語とは使わない」も境界事例として短く置きました**（くわしくは Unit 4 と明記）。Unit 1 の誤りとして多いためです。
6. **単語テストのボタンは「準備中」のままです**（順41まで）。`g3/index.html` の共通リンクの「単語テスト（中3）」も準備中のままです。

### 気になった点（次の回への申し送り）

- **次は順27＝中3 Unit 2（現在完了（完了・結果）。スラッグ `perfect-result`）です。** 要るもの：このワークブックと単語帳（`g3/unit01_perfect-experience.html`・`g3/vocab01_perfect-experience.html`。書きぶりの見本）、`tools/tpl-workbook.html`・`tools/tpl-vocab.html`。新出語は累計1,079語との差分で、`"g3-2"` のキーに積みます。
- Unit 2 で使う `just`・`already`・`yet` は未収録の語です（中3 Unit 1 では使っていません）。`gone` は `IRREGULAR` に入れてあります。
- **`whose`・関係副詞は `UPDATE-PLAN-g2g3.md` で「保留」のままです。** 判断が要るのは中3 Unit 9（順34）の前です。
- `fish` はこの単元の見出し語にしました（前の回からの申し送りで「master にも BASIC にも無い」とされていた語）。`video`・`year`（単数形）・`hi`・`take part in 〜` の重複・`worse`／`worst`／`could` は前の回からの申し送りのままです（人の判断）。

### 飛ばした操作

- **なし。** 5フォルダを一覧し、同名ファイルの重複が無いことを確認しました。復元は計画書類4本・`STATUS.md`・`index.html`・`word-test.html`・`tools/` の5本（`build.py`・`check.py`・`master-vocab.json`・`tpl-workbook.html`・`tpl-vocab.html`）・`units/` の23本・`g2/` の25本（`index`・単語帳16本・`review01`〜`04`・`review-final`・`unit01`・`unit15`・`unit16`）・`g3/index.html` の **61本**で、すべて Drive の `fileSize` とバイト数が一致しました。

---

## 2026-10-12（夜の枠／JST。開始 2026-10-11 16:13 UTC ＝ 2026-10-12 01:13 JST）　順25：中3の道具の準備

手順5の判定：1番目は通過（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-N"` のキーで積む作り。中1 479語／中2 567語）。2番目は `g2/` に Unit 1〜16 の2本ずつが Drive にそろい、復元した Unit 1 は `check.py 1 --grade 2` が NG 0件。3番目は `word-test.html` に `data-g="2"` があり `--word-test` が NG 0件。4番目は `GRADE_REVIEW_SPEC[2]` あり。5番目は `g2/review01`〜`04` がそろい4本とも NG 0件。6番目は `g2/review-final.html` あり NG 0件。7番目で **`g3/index.html` が無く、`check.py` に中3の `LATER_GRAMMAR` も無い**ので、**順25＝中3の道具の準備**です。**教材は作らない回です。**

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g3/index.html` | **新規**（15,811バイト）中3の目次。全15単元・全テストが「準備中」 | **g3** |
| `tools/check.py` | 変更（74,928 → 81,705バイト）中3の `LATER_GRAMMAR_G3` と `ING_STOP_G3` を追加・`GRADE_LATER_GRAMMAR` に `3:` を追加・冒頭の履歴に追記 | tools |
| `STATUS.md` | 新規（この記録。前の版は `STATUS-archive-2026-10-11.md` に改名） | ルート |
| `STATUS-archive-2026-10-11.md` | 改名のみ（中身は1バイトも触っていない） | ルート |

ほかのファイル（`index.html`・`word-test.html`・`g2/index.html`・`tools/build.py`・`tools/master-vocab.json`・復元した `units/` の23本・`g2/` の22本・計画書類5本）は**1バイトも変えていません**（復元直後と作業後の md5 を機械で突き合わせ、差分は `tools/check.py` だけ＋新規の `g3/index.html`）。**`build.py`・`master-vocab.json`・テンプレート3本はいっさい触っていません。** `master-vocab.json` は中1キー16件479語・中2キー16件567語のまま、中3のキーはまだありません。

### 中身1：`g3/index.html`

`g2/index.html` と同じ作り（CSS はそのまま。単元ごとに ワークブック／単語帳／単語テスト の3枠、部ごとのまとめ枠、最下段に濃い地の「中3のまとめ」）。**単元が1本も無いので、3枠とも・テスト枠とも「準備中」でリンクを張っていません。** ヘッダーの学年切り替えは「中1」「中2」がリンク、「中3」が `<span class="here">`（JS なし・ただのリンク）。共通リンクは中3の単語テストが準備中、中2・中1の単語テストと基本語リスト・総索引はリンク。

| 部 | 名前 | Unit |
|---|---|---|
| 第1部 | 現在完了 | 1〜4 |
| 第2部 | 不定詞の発展・原形不定詞 | 5〜8 |
| 第3部 | まとまりで名詞を説明する | 9〜12 |
| 第4部 | 仕上げ | 13〜15 |

単元名は `PLAN-g2g3.md`「1. 単元数と部の構成」の表どおりです（Unit 5 は `It is 〜 (for 人) to …`、Unit 10 は「分詞の後置修飾（現在分詞・過去分詞）」、Unit 15 は「中1〜中3の文法の整理」）。

### 中身2：`tools/check.py` の中3の `LATER_GRAMMAR_G3`（14件）

`PLAN-g2g3.md` 5.2 の `first` の振り分けどおりです。**中2までの形はすべて中3の範囲内なので `first` を振っていません。**

| first | 見る形 |
|---|---|
| 1 | 現在完了 |
| 3 | 現在完了進行形 |
| 5 | It is 〜 to（形式主語。be going to を拾わないよう `going` を外した） |
| 6 | too 〜 to / 〜 enough to / so 〜 that |
| 7 | 人 + to 不定詞（want / tell / ask） |
| 8 | 人 + 原形（make / let / help） |
| 9 | 間接疑問 |
| 10 | 分詞の後置修飾（現在分詞・過去分詞の2件） |
| 11 | 関係代名詞（主格） |
| 12 | 関係代名詞の省略 |
| 13 | 仮定法 |
| 14 | 付加疑問・感嘆文（2件） |

**綴りだけでは見分けられない形は、`LATER_GRAMMAR_G2` と同じ方針で入れていません**（誤検出のほうが害が大きいため）。入れていないのは、関係代名詞の that（接続詞・指示語と同じ綴り）、人以外を説明する分詞の後置修飾、疑問詞が主語の間接疑問（`I know who came.`）、`help 人 to 原形`（不定詞の目安と重なる）です。この4つは `PLAN-g2g3.md` 4節の「必ずやること」を見て人が確かめる必要があります。コードのコメントにもそう書きました。

### 検証結果

- **中1の既存の検査はすべて NG 0件**：`--index`・`--word-test`・`--review 1`〜`4`・`--review final`・`check.py 1`。**作業前（復元直後）にも同じ検査で NG 0件のベースラインを取ってあります。**
- **中2もすべて NG 0件**：`--index --grade 2`・`--review 1`〜`4 --grade 2`・`--review final --grade 2`・`check.py 1 --grade 2`。
- **新規：`--index --grade 3` が 15項目 NG 0件。**
- `--review 1 --grade 3` は想定どおり「中3 の総合テストの仕様（GRADE_REVIEW_SPEC）はまだありません（順42 で足します）」で止まります。
- **`LATER_GRAMMAR_G3` の当たり外れを機械でテストしました**：中3で後に出る形の例文**19本すべてを正しい `first` で検出**し、中2までの形の例文**18本では1件も誤検出しませんでした**（`He made me happy`＝SVOC、`The boy was playing tennis`＝過去進行形、`It is going to rain`＝be going to、`The next day I visited 〜`、`The letter was written by Tom`＝受動態、`What time do you get up?`＝疑問詞 など）。
- **playwright（Chromium・375px、Google Fonts は空の CSS に差し替え）**：`g3/index.html`・`g2/index.html`・`index.html`・`units/review-final.html`・`g2/review-final.html`・`g2/review01.html`・`word-test.html`（`?g=1`・`?g=2`）の**8通り**で scrollWidth 375px・JS の例外0件。

### 自分で判断したこと

1. **第2部の名前を「不定詞の発展・原形不定詞」にしました。** `UPDATE-PLAN-g2g3.md`「部の名前」の表の「It is 〜 to・too 〜 to・人 + to・人 + 原形」は、375px の目次見出し（1.08rem）では3行に折り返して蛍光ペンの帯が崩れます。同節に「長くて目次で折り返す場合は『不定詞の発展・原形不定詞』にしてよい（制作した回が判断して STATUS.md に書く）」とあるので、短い方を採りました。
2. **「人 + 原形」の目安は、うしろを動詞の原形の一覧に限りました。** `make 人 原形` を素朴に書くと、中2 Unit 8 の SVOC（`made me happy`）を誤って拾います。原形の一覧（約90語）に限ることで、`made me clean my room` は拾い、`made me happy` は拾わないようにしました。
3. **「関係代名詞の省略」の目安は、時を表す名詞（day・morning・week・year・time など）を外し、うしろの動詞を他動詞の一覧に限りました。** そうしないと「The next day I visited the old temple.」のような、中1から出てくる普通の文を誤って拾います。
4. **感嘆文は「!」で終わる形だけを拾うようにしました。** `What a 〜` `How 〜` は疑問詞（中1 Unit 10）と綴りが同じで、`What time do you 〜?` を誤って拾ってしまうためです。
5. **`ING_STOP_G3` という名前を付けて、-ing 形に見える語の一覧（interesting・morning など18語）を中1・中2の表と同じ内容で使い回しました。** 中3は現在完了進行形と分詞の後置修飾の2か所で同じ一覧が要るためです。中1・中2の表の中身は変えていません。
6. **`build.py` は触りませんでした。** 順1の時点で `GRADE_DIR`・`GRADE_PARTS`・`GRADE_UNITS` に中3（`g3`・1-4/5-8/9-12/13-15・15単元）が入っており、`out_dir(3)` も `review_home(3)` も中3で正しく動くので、順25で足すものがありませんでした。
7. **`index.html`・`g2/index.html` は触りませんでした。** `UPDATE-PLAN-g2g3.md` 順25 の「ヘッダーの『中3』は準備中のまま」どおりです。`g3/index.html` を置いても、`grade_ready(3)` は単元ファイル（`g3/unit??_*.html`）を見るので False のままで、両方の目次の検査は NG 0件を保っています。
8. **`GRADE_REVIEW_SPEC[3]`（中3の総合テストの仕様）は足していません。** 順42 の分なので、`UPDATE-PLAN-g2g3.md` の工程の区切りを守りました。

### 気になった点（次の回への申し送り）

- **次は順26＝中3 Unit 1（現在完了（経験）。スラッグ `perfect-experience`）です。** 要るもの：中2 Unit 16 のワークブックと単語帳（`g2/unit16_passive-advanced.html`・`g2/vocab16_passive-advanced.html`。書きぶりの見本）、`tools/tpl-workbook.html`・`tools/tpl-vocab.html`、それに **`g2/unit15_passive.html`**（`PLAN-g2g3.md` 4節の中3 Unit 1 に「過去分詞の一覧表は中2 Unit 15 のものを再掲する」とあるため）。**中3 Unit 1 の回で、`index.html` と `g2/index.html` のヘッダーの「中3」をリンクにします。**
- 新出語は `master-vocab.json` の累計（中1 479語＋中2 567語＝1,046語）との差分で決め、`"g3-1"` のキーで積みます。中3の1単元の新出語は30〜40語、読解本文は Unit 1〜8 が130〜180語（`PLAN-g2g3.md` 2節）です。
- **`whose`・関係副詞は `UPDATE-PLAN-g2g3.md` で「保留」のままです。** 判断が要るのは中3 Unit 9（順34）に着手する前です。`PLAN-g2g3.md` 4節の Unit 12 には「whose は扱わない」と書いてありますが、`UPDATE-PLAN-g2g3.md`（最優先）は保留なので、**和歌山の過去問での出題の有無を人が確かめて決める必要があります。**
- `g2/vocab12_gerund.html` の `take part in 〜` の重複、`IRREGULAR` に無い `worse`／`worst`／`could`、過去分詞一覧に無い `thought`・`began`・`kept`・`became`、`fish`・`video`・`year`（単数形）・`hi` が `master-vocab.json` にも `BASIC` にも無いこと、使われていない `tools/gen-word-test.tpl.html` は前の回からの申し送りのままです（人の判断）。

### 飛ばした操作

- **なし。** 5フォルダを一覧し、**同名ファイルの重複が無いことを確認しました**（ルート27本、`units/` 37本、`tools/` 11本、`g2/` 37本、`g3/` は空）。復元は計画書類5本・`STATUS.md`・`index.html`・`word-test.html`・`tools/` の3本（`build.py`・`check.py`・`master-vocab.json`）・`units/` の23本（単語帳16本・`review01`〜`04`・`review-final`・`unit01`）・`g2/` の23本（`index`・単語帳16本・`review01`〜`04`・`review-final`・`unit01`）の **55本**で、すべて Drive の `fileSize` とバイト数が一致しました。`check.py`（74,928バイト）と `STATUS.md`（39,543バイト）はサブエージェントが「大きすぎて返せなかった」と報告しましたが、`tool-results/*.txt` に残っていたので復号できました（この節の下の要点どおり）。

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
