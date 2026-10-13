# 制作の記録

> **2026-10-02（夜）にこのファイルを分割しました。** 10-01（夜）の順5：中2 Unit 4、10-02（昼）の順6：中2 Unit 5 の記録は `STATUS-archive-2026-10-02.md` にそのまま入っています。それより前は `STATUS-archive-2026-10-01.md`、`STATUS-archive-2026-09-30.md`、`STATUS-archive-2026-09-28.md`、`STATUS-archive-2026-09-26.md`、`STATUS-archive-2026-09-24.md`、`STATUS-archive-2026-09-23-night.md`、`STATUS-archive-2026-09-23.md`、`STATUS-archive-2026-09-22.md`、`STATUS-archive-2026-09.md` です。
>
> 手順は前回と同じで、**古い `STATUS.md` を `update_file` で改名し、この新しい `STATUS.md` を置いています。**アーカイブ側の中身は1バイトも触っていません。リポジトリに反映するときは、改名されたアーカイブとこの新しい `STATUS.md` の両方を置いてください。「Drive からの復元」「Drive へのアップロード」の要点は下に書き写してあります。

---

## 2026-10-03（夜の枠／JST。開始 2026-10-03 16:12 UTC ＝ 10-04 01:12 JST）　順9：中2 Unit 8（目的語が2つの文（SVOO）と 補語のある文（SVOC））

手順5の判定：1番目（`g2/index.html` あり・`check.py --help` に `--grade` あり・`"g2-N"` のキーで積む作り）は通過。N=1〜7 は Drive に `g2/unit0N_*.html`・`vocab0N_*.html` がそろっており（復元して `python tools/check.py N --grade 2` を走らせ、1〜7 すべて NG 0件を確認）、`g2/unit08_*.html` が無い N=8 で止まったので、**順9＝中2 Unit 8（スラッグ `svoo-svoc`）**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/unit08_svoo-svoc.html` | **新規**（49,925バイト） | g2 |
| `g2/vocab08_svoo-svoc.html` | **新規**（38,283バイト） | g2 |
| `g2/index.html` | 変更（16,317 → 16,363バイト）Unit 8 をリンクに（`li class="ready"`、単語帳は「36語」） | g2 |
| `tools/check.py` | 変更（61,451 → 61,668バイト）語の網羅で全部大文字の語を飛ばす2行と、`IRREGULAR` に `told → tell`・`sent → send` の1行を追加 | tools |
| `tools/master-vocab.json` | 変更（6,845 → 7,201バイト）`"g2-8"` を追加 | tools |
| `STATUS.md` | 変更（この記録を上に追加） | ルート |

**`tools/build.py`・`units/` の中1のファイル・`index.html`・`word-test.html`・テンプレート・計画書類は1バイトも変えていません。**

### 中身

- **ワークブック**：30問（A 5／B 6（うち「1語不要」2問）／C 5／D 7／E 5／F 2）。解説は「動詞のうしろに名詞が2つ並ぶ文（SVOO）」（図解・語順は「だれに」→「なにを」・この形をとる動詞の列挙）→ **中1 Unit 8 の4格表を再掲**（人の位置は目的格）→「前置詞を使った書きかえ　to と for」（図解・動詞を分けた表・`transform` 2本・書きかえ対応表4組）→「補語のある文（SVOC）」（図解で `him ＝ Mike` を示す・call / name / make の3語に絞った表・補語が名詞か形容詞かの表・**keep も同じ形をとることに1段落だけ触れる**）→ 判定手順4段 → 境界事例4つ → 入試での出方 → よくある間違い4つ → 例文、の順です。
- `PLAN-g2g3.md` 3節 Unit 8 の4点はすべて入れました：①**SVOO を前置詞で書きかえる形**（独立した見出し・`transform` 2本・対応表4組・B 9/10番・C 12/13番・D 21番）②**to をとる動詞（give・show・teach・send・tell・lend・pass）と for をとる動詞（buy・make・cook・get）の表**（解説の表・判定手順4・まとめ）③**SVOC は call / name / make の3語に絞り、中1 Unit 8 の代名詞の格とつなげる**（4格表を SVOO の節に置き、SVOC の節から「上の4格の表にもどって確かめてください」と参照。A 2番・C 14番）④**make が SVOO と SVOC の両方をとること**を境界事例の1つ目に置きました（`made me a sweater` ／ `made us sad`、見分け方は「2つ目が形容詞なら SVOC、渡せるものなら SVOO」）。
- 前回の申し送りどおり、**今回あえて避けられていた `lend me 〜`・`show me the way` を使い**、**`keep` の SVOC にも触れました**（「この単元では出題しません」と明記）。
- **読解**：ユカのスピーチ（帰国する ALT のブラウン先生へクラスでアルバムを作った話）。本文136語（めやす 100〜140語）。下線部①が `I wrapped the album in red paper.`（和訳）、②が `The album made him very happy.`（補語を1語で書きぬく）。
- **単語帳**：新出語 **36語**（めやす30〜40語）。動詞5（lend offer share print wrap）・熟語6（each other／show 〜 around／tell a lie／make a speech／one of 〜／at last）・名詞21（album audience calendar chance clerk curry envelope favor glove grade memory necklace nickname page postcard ribbon stamp sweater title truth wallet）・形容詞4（perfect proud soft thirsty）。累計は中1 479語＋中2 289語＝**768語**。

### 検証結果

- **`check.py 8 --grade 2`：17項目 NG 0件**（パート構成・設問数30・解答数30・並べ替えの語群と語数・和訳の有無・語の網羅 未収録0語・例文一致 不一致0件・見出し語36語・重複なし・375px 横スクロールなし・印刷 A4 ワークブック16ページ／単語帳5ページ）。
- **後続文法の検査**（`LATER_GRAMMAR_G2` のうち first が9以上の形を、英文333本＝`<span class="en">`・読解本文の文・解答キー。誤答例の行・選択肢・パートCは除く、に1文ずつ当てる）：**当たり0件**。不定詞・疑問詞+to・動名詞・比較・as 〜 as・受動態・現在完了・関係代名詞・間接疑問・仮定法はすべて避けて書きました。正規表現に無い形も目で確かめて0件（`-ing` 0件、`than`／`more`／`most` 0件、`have`／`has`／`had` ＋ 過去分詞 0件、`as 〜 as` 0件、`too 〜 to`／`enough` 0件、`make` ＋ 原形 0件）。
- **中1の既存の検査はすべて NG 0件**：`--index`・`--word-test`・`--review 1`〜`4`・`--review final`・`check.py 16`。**`check.py` を変える前後の両方で走らせて確認しています。**
- **中2の既存の検査もすべて NG 0件**：`--index --grade 2`（15項目）・`check.py 1`〜`7 --grade 2`。
- **`master-vocab.json`**：中1のキー（`"1"`〜`"16"`、479語）と `"g2-1"`〜`"g2-7"` は作業前の写し（復元直後の6,845バイト）とキーごとに突き合わせて**完全に一致**。増えたのは `"g2-8"` の36語だけです。
- **playwright（Chromium）**：`g2/unit08`・`g2/vocab08`・`g2/index.html`・`index.html`・`word-test.html`・`units/review01.html`・`units/review-final.html` の7本を375px幅で開き、**scrollWidth 375px・`getBoundingClientRect()` ではみ出した要素0個・ページのJSエラー0件**（テストページは選択肢を選んでボタンを押したあとも0件・採点後も375px）。コンソールに1件出るのは Google Fonts への接続がこの作業環境のプロキシに拒否されるもので、中1の既存ファイルでも同じように出ます。教材側の問題ではありません（失敗したリクエストのうち Google Fonts 以外は0件であることを確かめました）。
- **未定義クラス0件**（本文の `class="..."` をテンプレートの CSS と突き合わせ）。新しい2本と `g2/index.html` に `<script>` は0件、外部読み込みは Google Fonts だけ。
- 図解3つを375pxでスクリーンショットして目視確認。枠は3つとも幅335pxで、ノードの右端は最大342px（`for` のノード）。いずれも枠の中に収まっています。

### 自分で判断したこと

1. **`check.py` の語の網羅に「全部大文字の語は飛ばす」2行を足しました。** `SVOO`・`SVOC` は文法の記号で語ではないのに、`proper`（`[A-Z][a-z]+`）では拾えず未収録38語になっていました。単語帳に立てるのは筋が通らず、全角に書きかえるのも読みにくいので、`w.isupper() and len(w) >= 2` を飛ばす形にしました。中1の検査5種と `check.py 16` を前後で走らせて影響0件を確認しています。**中3 Unit 15 でも文型の記号を使うなら、この行がそのまま効きます。**
2. **`IRREGULAR` に `told → tell`・`sent → send` を足しました**（`won`／`lost` を足した順3、`built`／`sold`／`spent` を足した順4と同じ扱い）。`tell`・`send` は中1の既出語ですが過去形が見出し語に寄らず、この単元は過去形で SVOO を書く場面が多いので、1語ずつ見出し語に立てるより `IRREGULAR` のほうが筋が通ります。
3. **誤答の選択肢と誤文訂正は、既出語だけで組みました。** 最初の案は `himself`・`quietness`・`sadly` を誤答に使っていましたが、いずれも未収録語になります（誤答の選択肢は語の網羅の対象から外れません）。`hers`・`quiets`・`quietly` に差しかえました。**次の回も、誤答に使う語が既出かどうかを先に確かめてください。**
4. **並べ替えの語群の人名は大文字のままにしました**（`[ we / named / the / baby / Hana ]`）。順7の申し送り（曜日・月・国名は大文字のまま）と同じ理由です。小文字にすると固有名詞の除外に引っかからず未収録1語になります。
5. **`name` を動詞として使いましたが、見出し語には立てていません。** 名詞の `name` が中1で既出で、累計との差分では新出語に数えられないためです。単語帳の末尾に「この単元で初めて動詞として使っている」と書きました。
6. **`keep` の SVOC は、解説で1段落だけ触れて出題しませんでした**（順7の申し送りに従いました）。`PLAN-g2g3.md` が SVOC を call / name / make の3語に絞ると決めているので、問題に出すと範囲が広がります。
7. **`LATER_GRAMMAR_G2` の SVOO の正規表現には手を付けていません。** 前回の申し送りで `lend`・`pass`・`bring` を足す案が出ていましたが、SVOO は first=8 でこの単元から範囲内になるため、足しても今回以降の検出は変わりません。1回1工程の決まりもあるので見送りました。
8. **「入試での出方」と「よくある間違い」は4項目ずつ**にし、バッジは既存の「使い方／綴り注意／セットで／別の品詞／対になる語」だけを使いました。

### 気になった点（次の回への申し送り）

- **次は順10＝中2 Unit 9（不定詞の名詞的用法、スラッグ `infinitive-noun`）です。** `PLAN-g2g3.md` の要注意事項どおり、**名詞的用法から入って「to のうしろは原形」を最初に固め**、主語になる `To read books is 〜` は1〜2例にとどめ、`want to`／`like to`／`try to` の目的語を中心にしてください。**中1 Unit 13 の can のうしろの原形と同じ理屈であることに触れる**のを忘れずに。
- **順10 に入ると、順7の申し送りにあった `LATER_GRAMMAR_G2` entry 9（不定詞）の誤検出問題が解消します**（first=9 がその単元から範囲内になるため）。`have to` ＋ 原形との切り分けは不要になります。
- **`word-test.html` の中2の語（順18）は、中2 Unit 16 まで作ってから**です。今回までで中2は289語（Unit 1〜8）です。
- 中3 Unit 9 の whose・関係副詞は `UPDATE-PLAN-g2g3.md` でまだ「保留」です。順26（中3 Unit 1）までは着手に影響しません。

### 飛ばした操作

- **なし。** 5フォルダ（ルート・units・tools・g2・g3）を一覧し、同名ファイルの重複が無いことを確認しました（`g3/` は空、`units/` は37本、`g2/` は作業前17本）。回帰検査のため `units/` の単語帳16本・総合テスト5本・`unit16`・`word-test.html`・`g2/` の Unit 1〜7 の14本も復元し、すべて Drive の `fileSize` と一致しました。

### Drive からの復元（今回も同じ方法で通りました）

- サブエージェントに `download_file_content` だけを呼ばせ（1体に3〜4本）、`~/.claude/projects/<作業ディレクトリ>/<セッションID>/subagents/*.jsonl` と `tool-results/*.txt` から長い base64 の連なりを正規表現（`[A-Za-z0-9+/]{2000,}={0,2}`）で拾って復号。**復号した長さが Drive の `fileSize` と一致したものだけ書き出す。** 今回は52本すべて一致しました。
- **サブエージェントが「大きすぎて返せなかった」と報告しても、記録側（`tool-results/*.txt`）には残っています。** 失敗扱いにせず、復号を試してください。
- **ファイルの対応づけは「復号後のバイト数」で行うのが確実です**（タイトルは `index.html` がルートと g2 で重複し、ファイルIDは `__` を含むものがある）。落とす前に `search_files` で全件のサイズを控えておき、サイズが重複しないことを確かめてから落とします。
- `search_files` は1ページ5件しか返さないので `nextPageToken` で全件を取る（`units` は8ページ）。一覧だけをサブエージェントに取らせ、「タイトル／ファイルID／サイズ」のタブ区切りで返させると速いです。
- アップロードは `textContent` を使う（`base64Content` は長いと崩れる）。

---

## 2026-10-03（昼の枠／JST。開始 2026-10-03 06:08 UTC ＝ 15:08 JST）　順8：中2 Unit 7（助動詞 may / should と Will you / Shall I / Shall we）

手順5の判定：1番目（`g2/index.html` あり・`check.py --help` に `--grade` あり・`"g2-N"` のキーで積む作り）は通過。N=1〜6 は `g2/unit0N_*.html`・`vocab0N_*.html` がそろい、`python tools/check.py N --grade 2` がいずれも NG 0件。`g2/unit07_*.html` が無い N=7 で止まったので、**順8＝中2 Unit 7（スラッグ `may-should`）**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/unit07_may-should.html` | **新規**（46,799バイト） | g2 |
| `g2/vocab07_may-should.html` | **新規**（38,912バイト） | g2 |
| `g2/index.html` | 変更（16,269 → 16,317バイト）Unit 7 をリンクに（`li class="ready"`、単語帳は「36語」） | g2 |
| `tools/check.py` | 変更（61,355 → 61,451バイト）`CONTRACTIONS` に `"shouldn't": ["should", "not"]` を1行追加 | tools |
| `tools/master-vocab.json` | 変更（6,481 → 6,845バイト）`"g2-7"` を追加 | tools |
| `STATUS.md` | 変更（この記録を上に追加） | ルート |

**`tools/build.py`・`units/` の中1のファイル・`index.html`・`word-test.html`・テンプレート・計画書類は1バイトも変えていません。**

### 中身

- **ワークブック**：30問（A 5／B 6（うち「1語不要」2問）／C 5／D 7／E 5／F 2）。解説は may の2つの意味（許可・推量。見分け方は「人がしてよいことか、そうなる見こみか」）→ May I 〜? と答え方（断るときは `I'm sorry, you can't.`）→ should と must の強さの表（must＞should＞may）→ **Will you 〜? ／ Shall I 〜? ／ Shall we 〜? を「決まった言い方」として別の見出しに置き、答え方（Sure. / All right. ／ Yes, please. / No, thank you. ／ Yes, let's. / No, let's not.）を表でセットに**。答え方は「だれが動くか（相手／自分／いっしょに）」で決まると説明 → 判定手順 → 境界事例4つ（未来をたずねる Will you 〜? と依頼の Will you 〜?／may not の2通りの読み／推量の may と予測の will・perhaps／**must の推量「〜にちがいない」を may と並べて紹介**）→ 入試での出方 → よくある間違い4つ → 例文、の順です。
- `PLAN-g2g3.md` 3節 Unit 7 の3点はすべて入れました：①may の2つの意味（解説の表・境界事例・A 1番・D 6番・E 3番）②should の強さ（must との差の表）③Will you / Shall I / Shall we を別枠に置き答え方をセットに（表・図解・A 3〜5番・B 1/3/5番・C 3/4番・E 4番）。
- **読解**：対話文（カナダから来たエマのホームステイ先の朝。母・エマ・サキの3人）。本文129語（話し手の名前11語を含む。`reading-wc` は名前を除いて「およそ120語」）。下線部①が `Shall I call your school?`（意味を選ぶ）、②が `You should stay home today.`（和訳）。
- **単語帳**：新出語 **36語**（めやす30〜40語）。助動詞2（may should）・熟語7（Will you 〜?／Shall I 〜?／Shall we 〜?／No, thank you.／Excuse me.／pick up 〜／lie down）・動詞4（decide repeat order copy）・名詞18（fever headache throat advice seat menu message appointment dentist exam towel salt tea jacket temperature clinic address note）・形容詞3（sore serious rude）・副詞2（perhaps inside）。累計は中1 479語＋中2 253語＝**732語**。

### 検証結果

- **`check.py 7 --grade 2`：17項目 NG 0件**（設問30・解答30・並べ替えの語群と語数・和訳の有無・語の網羅 未収録0語・例文一致 不一致0件・375px 横スクロールなし・印刷 A4 ワークブック15ページ／単語帳5ページ）。
- **後続文法の検査**（`LATER_GRAMMAR_G2` のうち first が8以上の形を、英文300本＝`<span class="en">`・読解本文の文・解答キー。誤答例の行とパートCは除く、に1文ずつ当てる）：**当たり0件**。不定詞（want to など）・SVOO（`show you the way` など）・比較・間接疑問はすべて避けて書きました。
- **中1・中2の既存の検査はすべて NG 0件**：`--index`・`--index --grade 2`・`--word-test`・`--review 1`〜`4`・`--review final`・`check.py 16`・`check.py 1`〜`6 --grade 2`。
- **`master-vocab.json`**：中1のキー（`"1"`〜`"16"`、479語）と `"g2-1"`〜`"g2-6"` は作業前と完全に一致。増えたのは `"g2-7"` の36語だけ。
- **playwright**：`g2/unit07`・`g2/vocab07`・`g2/index.html`・`index.html`・`word-test.html`・`units/review01.html`・`units/review-final.html` の7本を375px幅で開き、scrollWidth 375px・はみ出し要素0個・JS エラー0件。未定義クラス0件、新しい2本と `g2/index.html` に `<script>` は0件。

### 自分で判断したこと

1. **3つを並べた図解（Will you／Shall I／Shall we の3ノード）は375pxで5pxはみ出したので、2ノード（Shall I ≠ Shall we）に変えました。** 3つの区別は直後の表で示しています。同じ `Shall` で動く人がちがう点が一番の間違えどころなので、図解はそこに絞りました。
2. **`check.py` の `CONTRACTIONS` に `shouldn't` を足しました**（`mustn't` を足した前回と同じ扱い。足さないと語の網羅で未収録1語になる）。中1の検査には影響しません（前後で全部走らせて確認済み）。
3. **`shall` は単独の見出し語に立てず、`Shall I 〜?`・`Shall we 〜?` の熟語で立てました**（現代の英語で `shall` が使われるのはほぼこの2つの形だけなので）。単語帳の末尾にその旨を書いています。
4. **`lend` は使いませんでした。** `Will you lend me 〜?` は SVOO で中2 Unit 8 の範囲になるためです。貸し借りは中1既出の `borrow` で済ませています。
5. **must の推量（〜にちがいない）は前回の申し送りどおり境界事例で may と並べました**が、問題では使っていません（「この単元の問題では must は Unit 6 の意味だけを使う」と解説に明記）。
6. **人名の所有格（`Saki's`）は使っていません**（語の網羅で NG になるため。「サキの家」は日本語の前書きとキャプションで示した）。
7. 新しいバッジ名は作らず、既存の「使い方／綴り注意／セットで／別の品詞／対になる語」だけを使いました。

### 気になった点（次の回への申し送り）

- **次は順9＝中2 Unit 8（SVOO と SVOC、スラッグ `svoo-svoc`）です。** `PLAN-g2g3.md` の要注意事項どおり、to をとる動詞（give・show・teach・send・tell）と for をとる動詞（buy・make・cook・get）の表、SVOC は call / name / make の3語、中1 Unit 8 の代名詞の格表とのつなぎ、make の SVOO／SVOC の境界事例を入れてください。**今回あえて避けた `lend me 〜`・`show you the way` は Unit 8 で使えます。**
- `LATER_GRAMMAR_G2` の SVOO の正規表現は動詞の一覧に `lend` `pass` `bring` が無いので、Unit 8 以降で増やすなら足すと検出が強くなります（今回は触っていません）。
- 中3 Unit 9 の whose・関係副詞は `UPDATE-PLAN-g2g3.md` でまだ「保留」です。

### 飛ばした操作

- **なし。** 5フォルダを一覧し、同名の重複が無いことを確認しました（`g3/` は空）。回帰検査のため `units/` 37本・`word-test.html`・`g2/` の Unit 1〜5 の10本も復元し、すべて `fileSize` と一致しました。

### Drive からの復元（今回も同じ方法で通りました）

- サブエージェント（haiku）に `download_file_content` だけを呼ばせ（1体に2〜4本）、`~/.claude/projects/<作業ディレクトリ>/<セッションID>/subagents/*.jsonl` と `tool-results/*.txt` から `{"content":"<base64>","id":"…","mimeType":"…","title":"…"}` を正規表現で拾って復号。**キーはタイトルではなくファイルIDにすること**（`index.html` がルートと g2 に同名であるため。今回これで1本取り違えかけた）。復号した長さが `fileSize` と一致したものだけ書き出す。
- **ファイルIDに `__` を含むものがある**（例 `19YfsGWlFC__BWWHORv_…`）。「ID__タイトル」の形で一時保存して `split('__')` すると壊れるので、区切りは別の文字にするか `rsplit` を使う。
- `search_files` は1ページ5件しか返さないので `nextPageToken` で全件を取る（units は8ページ）。一覧もサブエージェントに取らせ、その jsonl から正規表現で拾うと速い。
- 小さいファイル（20KB 程度）なら自分で `download_file_content` を呼んでもメインのセッション記録（`<セッションID>.jsonl`）から同じ方法で復号できる。

---

## 2026-10-02（夜の枠／JST。開始 2026-10-02 16:13 UTC ＝ 10-03 01:13 JST）　順7：中2 Unit 6（助動詞 must / have to）

手順5の判定は**2番目で止まりました**。1番目（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-N"` のキーで積む作り）は通過し、N=1〜5 は `python tools/check.py N --grade 2` がいずれも NG 0件、`g2/unit06_*.html` が無い N=6 で止まったので、**順7＝中2 Unit 6（助動詞 must / have to、スラッグ `must-have-to`）**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/unit06_must-have-to.html` | **新規**（45,575バイト） | g2 |
| `g2/vocab06_must-have-to.html` | **新規**（39,933バイト） | g2 |
| `g2/index.html` | 変更（16,217 → 16,269バイト）Unit 6 をリンクに（`li class="ready"`、単語帳は「36語」） | g2 |
| `tools/check.py` | 変更（61,265 → 61,355バイト）`CONTRACTIONS` に `"mustn't": ["must", "not"]` を1行追加 | tools |
| `tools/master-vocab.json` | 変更（6,122 → 6,481バイト）`"g2-6"` を追加 | tools |
| `STATUS.md` | 変更（この記録を上に追加） | ルート |

**`tools/build.py`・`units/` の中1のファイル・`index.html`・`word-test.html`・テンプレート・計画書類は1バイトも変えていません。** `IRREGULAR` に足す語もありませんでした（新出の動詞 `keep` `pay` の不規則な過去形 `kept` `paid` は単語帳のメモにしか書いておらず、ワークブック本文に1つも出てきません）。`check.py` への追加が1行だけで済んだのは、`must` `have to` `has to` `had to` がすべて既存の仕組みで見出し語に寄るためです（`had` は `IRREGULAR` の `had → have`、`has` は中1 Unit 9 の見出し語）。

### 中身

- **ワークブック**：30問（A 5／B 6（うち「1語不要」2問）／C 5／D 7／E 5／F 2）。解説は「must と have to は『〜しなければならない』」（図解・うしろは原形・must と have to のニュアンス差）→「have to は主語と時で形が変わる」（has to／had to／will have to の表、**must に過去形も未来形も無い**）→「**must not と don't have to は意味が逆**」（図解・表・打ち消す場所で考える理屈・短縮形 mustn't）→「否定文と疑問文」（`Must I 〜?` と `Do I have to 〜?` の表、**`Must I 〜?` に No で答えるときは `No, you don't have to.`**）→ 判定手順 → 境界事例 → 入試での出方 → よくある間違い → 例文、の順です。
- **`PLAN-g2g3.md` 3節 Unit 6 の3点はすべて入れました**：①**must not（禁止）と don't have to（不要）が逆であることを図解と誤文訂正の両方で**扱いました。独立した見出しを立て、図解（2ノード）・4行の表・「`not` が打ち消している場所がちがうから意味が逆になる」という理屈を置き、「よくある間違い」の2番目（`You don't have to cross the street here.` → `must not`）とパートC 2番で誤文訂正としても出題しています。A 1番・2番も同じ対立を選ばせる問題です。②**must に過去形が無いので had to**。表で「形がない」と明示し、「よくある間違い」3番・パートC 3番・A 4番・B 6番・読解の下線部②（E 4番で理由を問う）の5か所で扱いました。③**have to の三単現 has to**。表と A 3番・パートC 4番・「よくある間違い」1番で扱っています。
- **読解**：ユイのスピーチ（日本の学校とオーストラリアの学校の決まりの比較）。本文138語（めやす 100〜140語）。下線部①に `They don't have to clean their classrooms, because someone cleans them every evening.`（和訳）、下線部②に `Last year we had to clean the gym`（must にならない理由）を置きました。
- **単語帳**：新出語 **36語**（めやす 30〜40語）。助動詞1（must）・熟語6（have to 〜／don't have to 〜／hand in 〜／on time／put on 〜／once a week）・動詞10（follow keep pay cross enter lock raise check rest save）・名詞13（safety health medicine accident passport textbook entrance gate elevator report group stairs visitor）・形容詞5（dangerous healthy polite public wrong）・副詞1（twice）。累計は中1 479語＋中2 217語＝**696語**。

### 検証結果

- **`check.py 6 --grade 2`：17項目 NG 0件**（パート構成・設問数30・解答数30・並べ替えの語群と語数・和訳の有無・語の網羅 未収録0語・例文一致 不一致0件・375px 横スクロールなし・印刷 A4 ワークブック15ページ／単語帳5ページ）。
- **`LATER_GRAMMAR_G2` のうち first が7以上の形を、英文255本（ワークブックの `<span class="en">` と読解本文の文。誤答例の行とパートCは除く）に1文ずつ当てて、残った当たりは「不定詞」の9件だけ**。9件はすべて `have to` ／ `had to` ／ `didn't have to` ＋ 原形で、**この単元自身の形（first=6）を entry 9 の正規表現が拾った誤検出**です（順4の `going to visit` と同じ性質）。確かめ方として、本文中の「語 ＋ to ＋ 語」をすべて取り出し、`to` の直前が `have` ／ `has` ／ `had` でないものを列挙したところ、`come to school`・`polite to visitors`・`carry the chairs to the gym`・`sends an email to her family` の前置詞の `to` と、パートCの誤文 `must to practice`（意図した誤り）だけでした。**Unit 9 の不定詞は0件です。**
- 正規表現に無い形も目で確かめて0件：`may` `should` `shall` 0件、`than` `more` `most` `better` `best` `enough` `been` `ever` 0件、`as 〜 as` 0件、`who` `which` 0件、受動態の `by` 0件、`-ing` は `morning` と `evening` の2語だけ（動名詞・進行形としては使っていません）。**`Will you 〜?` は中2 Unit 7 の決まった言い方なので1つも書いていません**（`will` は `will have to` と `I will talk about 〜` だけ）。`keep O C`・`SVOC` も避けました（「自分で判断したこと」3）。
- **中1の既存の検査はすべて NG 0件**：`--index`・`--word-test`・`--review 1`〜`4`・`--review final`。`--index --grade 2`（15項目）、`check.py 1`〜`5 --grade 2`、`16`（中1 Unit 16）も NG 0件。**作業前にも同じ14本を走らせて全部 NG 0件であることを確かめてから着手しています。**
- **`master-vocab.json` の中1のキー（`"1"`〜`"16"`、479語）と `"g2-1"`〜`"g2-5"` は作業前と完全に一致**（復元直後の6,122バイトの写しをセッション記録から取り直し、キーごとに語のリストを突き合わせ。増えたのは `"g2-6"` の36語だけ）。
- **playwright（Chromium）**：`g2/unit06_must-have-to.html`・`g2/vocab06_must-have-to.html`・`g2/index.html`・`index.html`・`word-test.html`・`units/review01.html`・`units/review-final.html` の7本を375px幅で開き、**横スクロールなし（scrollWidth 375px）・JSエラー0件**（テストページは選択肢を選んで採点ボタンを押したあとも0件）。前回の申し送りどおり、`getBoundingClientRect()` で**左右にはみ出した要素を数える確認も7本すべてで0個**でした。コンソールに出る1件は Google Fonts への接続がこの作業環境のプロキシに拒否されるもので（`requestfailed` の URL が `fonts.googleapis.com` であることを確かめました）、中1の既存ファイルでも同じように出ます。教材側の問題ではありません。
- **未定義クラス0件**（本文の `class="..."` をテンプレートの CSS と突き合わせ）。新しい2本と `g2/index.html` に `<script>` は0件、外部読み込みは Google Fonts だけ。
- 図解2つを375pxでスクリーンショットして目視確認。ノードの実測幅は `You must` 90px／`follow` 70px／`must not` 104px／`don't have to` 112px で、いずれも枠の中に収まっています。

### 自分で判断したこと

1. **`check.py` の `CONTRACTIONS` に `mustn't` を足しました。** `must not` の短縮形は入試の禁止表現で実際に出るので解説に入れたかったのですが、足さないと語の網羅で未収録1語になります（`lemma("mustn't")` が `must` と `not` に割れないため）。追加は1行で、中1の検査には影響しません（`--index`・`--word-test`・`--review` 5本を前後で走らせて確認済み）。
2. **must の「〜に違いない」（推量）は扱いませんでした。** `PLAN-g2g3.md` 3節 Unit 6 の必須3点に入っておらず、**Unit 7 が「may の2つの意味（許可・推量）」と「should の強さ（must との差）」を扱う**ので、推量の must はそこで may・should と並べて出すほうが筋が通ります。今回は義務・禁止・不要の3つに絞りました。**Unit 7 を作る回で、must の推量を may の推量と並べて置いてください。**
3. **`keep` を SVOC で使いませんでした。** `keep this room clean` ／ `keep us safe` は補語のある文（SVOC）で、**中2 Unit 8 の範囲**です。`We have to keep our promise.`（SVO）だけにし、読解本文も `Some rules are for our safety.` と書きかえました。**`keep` は入試では SVOC でよく出るので、Unit 8 で「keep も SVOC をとる」と触れる価値があります。**
4. **読解本文を一度書き直しました。** 最初の案は `a cleaner`（清掃員）という新出語が要る形でしたが、1語のためだけに見出し語を立てるのは割に合わないので `someone cleans them every evening` に変え、`someone`（中1の既出語）で済ませました。
5. **`deep` を落としました。** A 1番を最初 `This river is deep and dangerous` と書いていましたが、`deep` が未収録1語になりました。この単元の焦点（must not）と関係がないので、見出し語に足さず `This river is dangerous` に縮めています。
6. **並べ替えの語群で `Monday` だけ大文字のままにしました。** 「文の最初に来る語も小文字で示す」のは文頭の語の約束で、曜日は文の途中でも大文字です。小文字の `monday` にすると語の網羅で未収録1語になります（固有名詞の除外は大文字で始まる語だけが対象のため）。**次の回も、語群の中の曜日・月・国名は大文字のままにしてください。**
7. **単語帳の末尾のまとめを `wrap-up` ではなく `v-intro` にしました。** `wrap-up` ／ `wrap-up-t` は `tpl-workbook.html` の CSS にしか無く、`tpl-vocab.html` には定義がありません。前回の申し送りの未定義クラス検査で捕まえました。中2 Unit 5 の単語帳も `v-intro` を使っています。
8. **熟語を6つ立てました**（have to 〜／don't have to 〜／hand in 〜／on time／put on 〜／once a week）。`have to` 系の3つはこの単元の中心なので外せず、残りの3つは学校・公共の場の決まりを言う場面で入試に頻出するものに絞っています。

### 気になった点（次の回への申し送り）

- **次は順8＝中2 Unit 7（助動詞 may / should と Will you / Shall I / Shall we、スラッグ `may-should`）です。** `PLAN-g2g3.md` の要注意事項どおり、**may の2つの意味（許可・推量）、should の強さ（must との差）**を扱い、**`Will you 〜?` ／ `Shall I 〜?` ／ `Shall we 〜?` は「助動詞の疑問文」ではなく決まった言い方として別枠に置き**、答え方（`Sure.` ／ `All right.` ／ `Yes, let's.`）をセットで載せてください。「自分で判断したこと」2 のとおり、**must の推量もここで並べる**のがよいです。
- **`check.py` の `LATER_GRAMMAR_G2` の「不定詞」（entry 9）は `have to` ＋ 原形を拾います。** 今回のように `have to` を扱う単元では必ず当たるので、検証では「`to` の直前が `have` ／ `has` ／ `had` かどうか」で切り分けてください。順9（中2 Unit 9、不定詞）に入れば本物と区別がつかなくなるので、**その回までに entry 9 の正規表現へ `(?<!\bhave )(?<!\bhas )(?<!\bhad )` のような除外を入れることを検討してもよい**と思います（今回は1回1工程の決まりがあるので触っていません）。
- **`keep` の SVOC は Unit 8 で触れてください**（「自分で判断したこと」3）。
- 前々回からの申し送りの **`g2/unit03_be-going-to.html` の未定義クラス `<span class="sub">`** は、1回1工程の決まりがあるので今回も直していません。
- **人名の所有格（`Ken's` など）は語の網羅で NG になります。** 今回も英文で人名の `'s` は使っていません。
- **中3 Unit 9 の whose・関係副詞は、`UPDATE-PLAN-g2g3.md` でまだ「保留」です。**

### 飛ばした操作

- **なし。** ルート・units・tools・g2・g3 の5フォルダを一覧して同名の重複が無いことを確認したので、片付けは不要でした（`g3/` は空です）。

### Drive からの復元（今回も同じ方法で通りました）

`download_file_content` を**サブエージェントに呼ばせるだけ**にして（1体に3〜4本、haiku で十分）、セッション記録から base64 を復号します。今回は60本（ルートの仕様ファイル6本・`tools/` 5本・`g2/` 11本・`units/` 37本・`word-test.html`）すべてで Drive の `fileSize` とローカルのバイト数が一致しました。サブエージェント16体、数分で済みます。

- 小さいファイル（おおむね30KB未満）は `subagents/*.jsonl` の `tool_result` に JSON（`{"content": "<base64>"}`）で入っています。
- 大きいファイルは「exceeds maximum allowed tokens」になり、中身は `~/.claude/projects/<作業ディレクトリ>/<セッションID>/tool-results/*.txt` に残ります。**`subagents/*.jsonl` と `tool-results/*.txt` の両方から base64 の連続を拾って復号し、長さが Drive の `fileSize` と一致したものだけ書き出します。** サブエージェントの「失敗」報告は無視してかまいません（今回も10本が「FAILED」と報告されましたが、全部 `tool-results/` に残っていました）。
- サイズで突き合わせる方式なので、**同じバイト数のファイルが2本あると取り違えます。** 落とす前に一覧の `fileSize` で重複が無いことを確かめてください（今回の60本はすべて異なるサイズでした）。
- **`search_files` は `pageSize` を指定しても1ページ5件しか返しません。** フォルダの一覧は `nextPageToken` でページを送って全件を取ってください（`units/` は8ページあります）。
- **`units/` にファイルが無いと `--index --grade 2` が NG になります。** 単元を作る回は中1の38本まで落とすのを既定にしてください。

### Drive へのアップロード

**`textContent` で上げ、Drive の `fileSize` とローカルのバイト数を照合してから、古い同名ファイルを `trash_file` に送ります**（`create_file` は同名でも上書きしないため）。**`textContent` は末尾の改行を1つ落とすことがあります。** 末尾が空行で終わるファイルは1バイト短く上がるので、照合して1バイト足りなければ改行を1つ足して上げ直してください。

- **アップロードも1ファイル1体のサブエージェントに任せられます**（2026-10-02 夜の枠から）。本体の文脈に45KBのHTMLを2回通さずに済むので、ずっと安く上がります。指示は「このパスのファイルを読み、1文字も変えずに `textContent` で `create_file` に渡す。読み取りには `sed -n 'A,Bp'` を使う。上げる前に自分の写しをスクラッチに書き出し、`md5sum` で原本と突き合わせ、合うまで直す」です。
- **`tools/check.py` のような日本語の多いファイルは、転記を拒否するサブエージェントがいます。** 全角スペース（U+3000、35か所）・波ダッシュ（U+301C、28か所）・マイナス記号（U+2212、1か所）が目で見分けられないから、という理由です。**「写しが違っていても呼び出し側がハッシュで検出して捨てるので、まず上げてほしい」と伝えると通ります。** 実際、md5 を自分で突き合わせさせれば一致します。
- **納めたあとは必ず `download_file_content` で取り直し、ローカルとの SHA256 を突き合わせてください。** `fileSize` の一致だけでは、同じ長さの取り違えを拾えません。今回は6本すべて SHA256 まで一致しました。

### 検証に使うスクリプト（毎回使うもの）

- **後続文法の検査**：ワークブックの `<span class="en">` と読解本文を1文ずつ取り出し、`LATER_GRAMMAR_G2` のうち first がその単元番号より大きい規則を**1文ずつ**当てます（全文を連結して当てると別々の要素がつながった断片を拾います）。誤答例（`contrast-row bad`）・`strike`・パートCの誤文は除きます。
- **はみ出しの検査**：`document.querySelectorAll('body *')` の `getBoundingClientRect()` で `right > 375.5` か `left < -0.5` の要素を数えます。`check.py` の横スクロール検査はこれを拾いません。
- **未定義クラスの検査**：本文の `class="..."` を全部集め、テンプレート（`tpl-workbook.html` ／ `tpl-vocab.html`）の `<style>` にある `.名前` と差を取ります。
- **playwright** は Python 版を使います（node 側には `playwright` のパッケージが入っていません）。`chromium.launch(executable_path="/opt/pw-browsers/chromium")` で起動します。`playwright install` は不要です。
- Google Fonts への接続はこの作業環境のプロキシが拒否するので、コンソールに `ERR_TUNNEL_CONNECTION_FAILED` が1件出ます。教材側の問題ではありません（`requestfailed` の URL で確かめられます）。
