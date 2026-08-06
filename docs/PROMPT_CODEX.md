# Codex への指示書 — 高画質版の復元・照合・Release作成

あっきーがCodexに**そのまま貼る**ためのプロンプト。
目的：Google Drive の8分割バックアップから高画質MP4を復元し、SHA-256照合のうえ GitHub Release に添付する。
（ganjin の `HANDOFF_GPT_CODEX.md` と同じ、他AIへの作業引き渡しの流儀）

## 前提

- Codex が **drive.google.com と github.com に接続できる**環境で動いていること
- 作業ディスクに **1.5GB 以上**の空きがあること
- GitHub のログインが必要になったら、Codex はあっきーに操作を渡すこと（パスワードをチャットで扱わない）

---

## 貼るプロンプト

（ここから）

```
manabi-ai-lab のBGMプロジェクトの作業です。以下を順番に実行してください。

## 背景
『放課後トークルーム』1時間BGMの高画質MP4（649MiB）が、Google Drive に8分割で
バックアップされています。これを復元し、GitHub Release で配布します。
手順書・スクリプト・期待ハッシュはすべて GitHub リポジトリに用意済みです。

## 絶対に守るルール
1. 動画・音声の再エンコード・変換・圧縮を一切しない（画質を守る最優先事項）
2. SHA-256 が一致しないファイルを Release に上げない
3. MP4 や .bin を git にコミットしない（.gitignore で弾かれるが、-f で入れない）
4. 「放課後トークルーム_1時間_スマホDrive版.mp4」（HEVC・約101.6MB）は低画質版。
   一切使わない
5. GitHub のログインが必要になったら、自分で認証情報を扱わず、ユーザーに操作を渡す
6. Drive に接続できない環境だったら、回避策を探さずにその旨を報告して止まる

## 手順

### 1. リポジトリを取得
git clone https://github.com/manabi-ai-lab/manabi-bgm
cd manabi-bgm
docs/RESTORE.md と docs/RELEASE.md を読む。

### 2. Drive からパーツをダウンロード
公開フォルダ（リンクを知っていれば認証不要）:
https://drive.google.com/drive/folders/1BwpEpgVjfd5aLJRp1fL8SwKiKnxt-Hpp

after-school-talk-room-one-hour-youtube.part-00.bin 〜 part-07.bin の8個を
work/ ディレクトリにダウンロードする。個別のファイルIDと期待サイズは
docs/RESTORE.md の表にある（part-00〜06 は各 94,371,840 バイト、
part-07 は 19,324,024 バイト）。

サイズが一致しないファイルはダウンロード失敗なので取り直す。

### 3. 復元と照合
cd work
sh ../scripts/restore-and-verify.sh

このスクリプトはパーツ個別のSHA-256照合→結合→原本照合まで自動で行う。
成功条件：「✅ 完全に一致しました」が出ること。
期待SHA-256: 118de0f31bca5de2386e4099df674d67cc40a59dbf9ddf11443b887211605cfc
期待サイズ: 679,926,904 バイト

失敗したら docs/RESTORE.md の「4. 一致しなかったとき」に従う。
どのパーツが壊れているかまで特定して報告する。再エンコードは絶対にしない。

### 4. GitHub Release を作成
照合が成功した場合のみ:
cd work
sh ../scripts/create-release.sh "放課後トークルーム_1時間_高画質版.mp4"

このスクリプトはアップロード前にもう一度ハッシュを照合してから、
タグ v1.0.0-after-school-talk-room、タイトル「放課後トークルーム — 1時間BGM」で
Release を作り、MP4 を添付する。gh が未ログインなら指示が出るので、
ユーザーにログイン操作を渡してから再実行する。

### 5. アップロード後の再照合
Release のアセットURLから別名でダウンロードし直し、SHA-256 が
118de0f3... に一致することを確認する（手順は docs/RELEASE.md）。

### 6. サムネイルをリポジトリに配置
Drive のサムネイル（期待サイズ 265,782 バイト・JPEG）:
https://drive.google.com/file/d/1cviVqBQ1hGlBI7BaEy-AX816QVMoSRHv/view

ダウンロードしてサイズが 265,782 バイトであることを確認し、
assets/thumbnails/after-school-talk-room.jpg として main にコミット・push する。
画像の変換・リサイズはしない。

### 7. 記録を更新して push
- tracks/after-school-talk-room/CHECKSUMS.md の「照合の記録」表に、
  実施日・実施者（Codex）・結果を追記
- tracks/after-school-talk-room/README.md の「配布物」表の
  Release とサムネイルの状態を ✅ に更新
- STATUS.md のログに今回の作業を追記（このリポジトリの流儀：次の一歩を必ず書く。
  次の一歩は「YouTube限定公開投稿（あっきーがStudioで実施）」）
- main に push する

## 報告フォーマット
1. 復元結果（成功/失敗）
2. 復元後の SHA-256 実測値（全文）
3. Release URL
4. Release から再ダウンロードした時の SHA-256 実測値（全文）
5. サムネイル配置の結果（サイズ実測値）
6. できなかったことと、その理由
```

（ここまで）

---

## Codex が終わったあとにあっきーがやること

1. Codex の報告の **SHA-256 が2か所とも** `118de0f3…` に一致しているか目視確認
2. Release ページをスマホで開き、MP4がタップで再生できるか確認
3. YouTube へ限定公開で投稿 → `docs/YOUTUBE.md`（ここはログインが要るのであっきーの作業）

## うまくいかないときの切り分け

| 症状 | 原因と対応 |
| --- | --- |
| Drive からダウンロードできない | Codex の実行環境にネットワーク制限。**PCのCodex CLI か、あっきーの手動ダウンロード**に切り替える |
| パーツのハッシュ不一致 | ダウンロード失敗。該当パーツだけ取り直し |
| gh auth でエラー | あっきーがブラウザでログイン操作。パスワードはCodexに渡さない |
| Release 作成が 403 | その GitHub アカウントに manabi-ai-lab への write 権限がない。あっきーのアカウントで gh にログインし直す |
