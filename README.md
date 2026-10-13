# YT3 — YouTube MP3 / MP4変換アプリ

## 概要

YouTube URLを入力して、MP3音声またはMP4動画として取得するFlask製のローカルWebアプリです。変換済みファイルをブラウザからダウンロードできます。

## 主な機能

- URLからMP3 / MP4への変換。
- 変換結果ページとダウンロード。
- Windows用の環境準備・起動スクリプト。
- `output/`への変換ファイル保存。

## 推奨要件

| 項目 | 環境 |
| --- | --- |
| OS | Windows（簡単起動対応） |
| Python | 3.10以上 |
| JavaScriptランタイム | Deno 2.3以上、またはNode.js 22以上。PATHへ登録 |
| ブラウザ | 現行のChromeまたはEdge |
| その他 | インターネット接続、変換ファイルを保存する空き容量 |

JavaScriptランタイムはYouTubeのチャレンジ処理に使用します。Denoを優先し、なければNode.jsを利用します。

## 必要なライブラリ

| ライブラリ | 用途 |
| --- | --- |
| Flask | Web画面・ダウンロード |
| yt-dlp[default] | YouTube取得とEJSチャレンジ処理 |
| imageio-ffmpeg | 同梱FFmpegを使う変換処理 |
| pytest | テスト |

導入範囲・バージョンは`requirements.txt`を参照してください。通常はWindowsへFFmpegを別途手動導入する必要はありません。

## 使い方

### Windowsで起動

1. Deno 2.3以上またはNode.js 22以上を導入し、PATHへ登録します。
2. ルートの`start.bat`をダブルクリックします。
3. Pythonがない場合は、wingetが使える環境でPython 3.12の導入を試します。
4. 仮想環境・依存関係・FFmpeg・JavaScriptランタイムの確認が終わるまで待ちます。
5. `http://127.0.0.1:8000/`を開きます。
6. URLを入力して「Convert to MP3」または「Convert to MP4」を押します。
7. 完了後、「Download MP3」または「Download MP4」で保存します。

停止は起動コンソールで`Ctrl+C`を押します。

### 手動起動

ルートで実行します。

```bash
python -m venv .venv
# OSに応じて .venv を有効化
python -m pip install -r requirements.txt
python -m src.run
```

## フォルダ構成

| 相対パス | 役割 |
| --- | --- |
| `src/app.py` | 入力画面・変換受付・ダウンロード |
| `src/converter.py` | yt-dlpとFFmpegの処理 |
| `src/run.py` | 起動入口 |
| `src/templates/` | 入力・結果画面のHTML |
| `src/static/` | CSS・JavaScript |
| `output/` | 変換したMP3・MP4 |
| `tests/` | 画面・変換コマンドのテスト |
| `docs/` | 運用資料とスキル一覧 |
| `.github/` | 開発ルールとスキル |
| `requirements.txt` | Python依存関係 |
| `start.bat` | Windowsセットアップ・起動 |
| `.venv/` | 初回起動で生成するPython環境 |

`.venv/`、キャッシュ、変換済み音声・動画はGit管理外です。`output/.gitkeep`で出力フォルダを保持しています。

## 仕組み

ブラウザがURLと形式を`POST /convert`へ送ります。yt-dlpが音声・動画を取得し、FFmpegが指定形式に変換します。`output/`へ保存して、`/download/<filename>`からファイルを返します。

## 確認方法

```bash
python -m pytest
```

## トラブル対処

- JavaScriptランタイム警告：Deno / Node.jsのバージョンとPATHを確認します。
- 古い依存関係によるエラー：仮想環境で `python -m pip install -U -r requirements.txt` を実行して再起動します。
- HTTP 403：依存更新に加えて動画の公開範囲・ログイン要求・YouTube側制限を確認します。更新だけでは解決しない場合があります。
- 起動失敗：8000番ポートの使用状況とコンソールに表示されたエラーを確認します。

取得・変換は利用権限のあるコンテンツを対象にしてください。
