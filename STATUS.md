# STATUS

作業ログ。単位ごとに追記し、**「次の一歩」を必ず書く**。（ganjin の流儀に合わせています）

---

## いまの状態

| | 状態 |
| --- | --- |
| 第1作 | **放課後トークルーム**で確定。1時間・会話用BGM |
| 音源 | 完成（Suno v2）。1時間版まで書き出し済み |
| 映像 | 完成（1264×720 / 24fps / H.264、ループアニメーション） |
| 高画質版の所在 | **Google Drive に8分割で退避済み**。復元は未実施 |
| リポジトリ | ✅ **作成済み**（<https://github.com/manabi-ai-lab/manabi-bgm>）。中身もpush済み |
| Release | 未作成（`v1.0.0-after-school-talk-room`） |
| YouTube | 未投稿。投稿文と設定は確定済み |
| サムネイル | Drive にある。リポジトリへは未配置 |

---

## 次の一歩

**あっきーのPCで高画質版を復元して照合する** → [`docs/RESTORE.md`](docs/RESTORE.md)
その後は Release作成（[`docs/RELEASE.md`](docs/RELEASE.md)）→ YouTube投稿（[`docs/YOUTUBE.md`](docs/YOUTUBE.md)）。

---

## ログ

### 2026-08-06 — あっきー ＋ Claude

- あっきーが Public リポジトリ `manabi-ai-lab/manabi-bgm` を作成
- Claude が中身一式（32ファイル）を `main` に push
- Drive の共有設定（全員編集者）は意図したものと確認。変更しない方針に記述を修正

### 2026-08-06 — ChatGPT（じぴ）→ Claude

- `docs/PROMPT_GPT.md` の指示書で、ChatGPT側の制作情報を回収
- 判明：Suno生成日（8/6）・曲ID（v1/v2）・提示プロンプト・スライダー値・
  v1/v2の実測ラウドネス・1時間化の方法（音31周＋6秒クロスフェード、映像10秒×360）・
  最終書き出しCRF 27・**59分版にAAC破損があり作り直した**経緯
- 不明のまま確定：Sunoのモデル名・実入力プロンプト・映像生成ツール名・サムネイル文字入れツール
- `SUNO.md` と `VIDEO_SPEC.md` に転記済み。あっきーがSunoの作品ページで確認できたら格上げする項目を `SUNO.md` 末尾に列挙
- ChatGPT作業領域とDriveに素材（v1/v2のMP3・10秒ループ動画・サムネイル）が現存することを確認。**Drive側を正**とする

---

### 2026-08-06 — Claude（リモート実行環境）

**やったこと**

- Drive バックアップフォルダ（`1BwpEpgVjfd5aLJRp1fL8SwKiKnxt-Hpp`）を確認。13ファイル、欠品なし
- 小さいメタデータ5点を取得して検証
  - 8パーツ合計 **679,926,904 バイト**＝648.4 MiB。「約649MiB」と一致
  - 復元スクリプトは part-00→07 の順で**単純バイナリ連結**。再エンコードなしを確認
  - 原本SHA-256 `118de0f3…` が README・ORIGINAL_SHA256.txt・依頼内容の3か所で一致
- `scripts/restore-and-verify.sh` を作成。**正常系／欠品／破損の3経路を実行して検証**
- `scripts/split-for-backup.sh` を作成。250MBのファイルで**分割→復元がバイト単位で完全一致**することを実測
- リポジトリ一式を作成（README / 利用条件 / docs 5点 / tracks 5点＋backup / templates / scripts）
- Drive の YouTube投稿文資料を取り込み、`tracks/after-school-talk-room/YOUTUBE.md` を正本化

**できなかったこと**

- 高画質版の実復元と照合 — **この環境から Drive に到達できない**（`drive.google.com` は 403）
- スマホ用URLの作成 — 元ファイルが手元に来ないため
- `manabi-bgm` リポジトリの作成 — GitHub App に org のリポジトリ作成権限がない（403）
- Release 作成・YouTube投稿 — 上記に依存、およびログインが必要
- サムネイルのリポジトリ配置 — バイナリを会話経由で運ぶと破損リスクがあるため見送り

詳細と代替案は [`docs/HANDOFF.md`](docs/HANDOFF.md)。

**メモ**

- Drive バックアップフォルダは「リンクを知っている全員」＝編集者。**意図した設定**とあっきーに確認済み。変更しない

**次の一歩**

- あっきー：`manabi-bgm` リポジトリを作る（そのあとの push は Claude が実行できる）

---

### （次の記入欄）

**日付 — 誰が**

- やったこと：
- 次の一歩：
