# STATUS

作業ログ。単位ごとに追記し、**「次の一歩」を必ず書く**。（ganjin の流儀に合わせています）

---

## いまの状態

| | 状態 |
| --- | --- |
| 第1作 | **放課後トークルーム**で確定。1時間・会話用BGM |
| 音源 | 完成（Suno v2）。1時間版まで書き出し済み |
| 映像 | 完成（1264×720 / 24fps / H.264、ループアニメーション） |
| 高画質版の所在 | ✅ **Google Driveの8分割バックアップから復元・SHA-256照合済み** |
| リポジトリ | ✅ **作成済み**（<https://github.com/manabi-ai-lab/manabi-bgm>）。中身もpush済み |
| Release | ✅ 公開済み（`v1.0.0-after-school-talk-room`） |
| YouTube | ✅ **一般公開**（2026-08-06） |
| サムネイル | ✅ Drive原本を `assets/thumbnails/after-school-talk-room.jpg` に配置済み |

---

## 次の一歩

第1作は**完走**（2026-08-06）。次は以下のどちらか。

1. **YouTube Shortsの投稿**（動画は制作済み。投稿文は [`tracks/after-school-talk-room/COPYPASTE.md`](tracks/after-school-talk-room/COPYPASTE.md) の STEP 4-5）
2. **第2作の制作**（[`docs/PLAYBOOK.md`](docs/PLAYBOOK.md) の工程順。`templates/` から `tracks/<slug>/` を作るところから）

1週間後にショートの維持率を確認して [`SHORTS.md`](tracks/after-school-talk-room/SHORTS.md) の記録欄に残す。100%超＝ループ視聴が取れていれば設計成功。

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

### 2026-08-06 — Codex

**やったこと**

- Driveの8分割バックアップを番号順に単純バイナリ結合し、高画質版MP4を復元
- 復元後MP4が 679,926,904 バイト、SHA-256 `118de0f31bca5de2386e4099df674d67cc40a59dbf9ddf11443b887211605cfc` と完全一致することを確認
- GitHub Release `v1.0.0-after-school-talk-room` を公開し、アセット名をASCIIの `after-school-talk-room-1h-hq.mp4` に統一
- Releaseから別名で再ダウンロードし、サイズとSHA-256が原本と完全一致することを確認
- Driveのサムネイルを無変換で `assets/thumbnails/after-school-talk-room.jpg` に配置（265,782 バイト）
- Release本文、配布状況、チェックサム記録、Release手順を更新

**次の一歩**

- YouTube限定公開投稿（あっきーがStudioで実施）

---

### 2026-08-06 — あっきー

- YouTube へ本編を**限定公開**で投稿（旧タイトルのまま。公開前にSEO版タイトルへ変更予定）
- 次の一歩：Studio設定の確認（合成コンテンツ・カテゴリ・自動チャプター）→ 5点再生チェック → SEO版タイトルに変更 → 一般公開

### 2026-08-06 — 第1作 完走 🎉

- YouTube本編を**一般公開**（https://youtu.be/i_RX6gUtuno）。SEO版タイトルで公開
- これで第1作『放課後トークルーム』の全工程が完了：
  復元・照合 → リポジトリ整備 → Release公開 → YouTube公開 → ショート制作 → TikTok投稿
- 再利用のため `.claude/skills/bgm-release/`（Claude用スキル）と
  `AGENTS.md`（Codex等がこのリポジトリで作業するときの標準指示）を整備
- 未了：YouTube Shortsの投稿、一時ブランチ `tmp-tiktok-upload` の削除

**次の一歩**

- Shorts投稿 または 第2作の制作

### （次の記入欄）

**日付 — 誰が**

- やったこと：
- 次の一歩：
