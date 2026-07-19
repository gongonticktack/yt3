# YouTube MP3 Web App

このプロジェクトは、YouTube URL を入力すると MP3 に変換する小さな Flask Web アプリのプロトタイプです。

## 概要

- ブラウザから YouTube URL を入力する
- サーバー側で URL を受け取り、音声抽出と MP3 変換を実行する
- 変換後の MP3 は [output](output) フォルダに保存する
- 変換結果のメッセージを画面に返す

## 依存関係

- Python 3.10 以上
- Flask
- yt-dlp
- ffmpeg
- pytest

インストールコマンド:

```bash
python -m pip install -r requirements.txt
```

## 起動手順

Windows では、プロジェクトフォルダの [start.bat](start.bat) をダブルクリックするだけで起動できます。

1. プロジェクトフォルダで [start.bat](start.bat) をダブルクリックします。
2. 自動的に `.venv` 仮想環境が作成・有効化されます。
3. 依存関係が入っていなければ [requirements.txt](requirements.txt) を読みてインストールします。
4. 変換に必要な ffmpeg が PATH に見つかるか確認します。見つからない場合は、Windows 側で ffmpeg をインストールして PATH を通してください。
5. Flask の起動スクリプトが実行され、ブラウザで `http://localhost:8000` を開けるようになります。
6. URL を入力して送信すると、サーバーが受け取って変換を開始します。
7. 変換が終わると結果ページに表示され、[output](output) フォルダに MP3 が保存されます。

### ffmpeg を入れる方法（Windows）

1. FFmpeg の公式インストール方法に従って、Windows 用のバイナリを入れます。
2. `ffmpeg.exe` が実行できる場所を PATH に追加します。
3. ターミナルや VS Code を再起動してから、再度 [start.bat](start.bat) を実行してください。
4. その後、`ffmpeg -version` で動作確認できます。

## start.bat で行っていること

[start.bat](start.bat) は、Windows での起動を簡単にするためのバッチファイルです。実際には次の処理を行います。

- `.venv` がなければ仮想環境を作成する
- 仮想環境を有効化する
- Python と ffmpeg が使えるか確認する
- 必要なら [requirements.txt](requirements.txt) を読み込んで依存関係を入れる
- 最後に `python -m src.run` で Flask アプリを起動する

## 仕様

- `/` で入力フォームを表示します。
- `/convert` で URL を受け取り、MP3 生成を試みます。
- 変換成功時は保存先のパスを返します。ffmpeg が未導入だとエラーで通知されます。

## ディレクトリ構成

```text
.
├── .github/                  # GitHub / Copilot 向けの設定・補助ファイル
├── src/                      # Flask アプリ本体とテンプレート、静的ファイル
│   ├── app.py                # ルーティングと画面表示を担当
│   ├── converter.py          # YouTube から音声を取得し MP3 に変換する処理
│   ├── run.py                # Flask アプリを起動するエントリーポイント
│   ├── templates/            # HTML テンプレート群
│   │   ├── index.html        # 入力フォーム画面
│   │   └── result.html       # 変換結果画面
│   └── static/               # CSS / JavaScript の静的ファイル群
│       ├── css/
│       │   └── style.css     # 画面の見た目を定義するスタイルシート
│       └── js/
│           └── main.js       # フォーム送信時の動作を制御する JS
├── output/                   # 変換後の MP3 ファイルを保存する場所
├── tests/                    # pytest のテストコード群
├── requirements.txt          # Python の依存関係一覧
├── start.bat                 # Windows で起動するためのバッチファイル
└── README.md                 # このドキュメント
```

- [.github](.github): GitHub や Copilot の補助設定を置くフォルダです。
- [src/run.py](src/run.py): 実行用エントリーポイントです。
- [src/app.py](src/app.py): Flask アプリ本体で、URL を受け取って画面に返す役割です。
- [src/converter.py](src/converter.py): YouTube から音声を取得し、MP3 に変換する処理を担当します。
- [src/templates](src/templates): HTML テンプレートを置くフォルダです。
- [src/static/css/style.css](src/static/css/style.css): スタイルシートです。
- [src/static/js/main.js](src/static/js/main.js): フロントエンド JS です。
- [output](output): 変換済みの MP3 が保存される出力フォルダです。
- [tests](tests): 自動テストを置くフォルダです。

## 仕組み

このアプリは、いくつかの部品を組み合わせて動いています。

- [src/templates/index.html](src/templates/index.html) で、ブラウザ上の入力フォームを表示します。
  - ここでユーザーが YouTube の URL を入力します。
- [src/app.py](src/app.py) で、入力された URL を受け取ります。
  - Flask という Web サーバー用の Python の道具を使って、URL を受け取る役割を担当します。
- [src/converter.py](src/converter.py) で、YouTube から音声だけを取り出して MP3 に変換します。
  - `yt-dlp` という機能を使うことで、YouTube の動画や音声を取得できます。
  - `ffmpeg` という音声処理の機能を使うことで、音声を MP3 形式へ変換できます。
- 変換が終わると、生成された MP3 を [output](output) フォルダに保存し、結果ページにリンクを表示します。

### ユーザー操作から変換までの流れ

1. ユーザーがブラウザで URL を入力して送信します。
2. Flask がその URL を受け取ります。
3. 変換処理が始まり、YouTube から音声データを取得します。
4. 取得した音声を MP3 形式に変換します。
5. 変換済みの MP3 を [output](output) フォルダに保存します。
6. 画面に「ダウンロード」リンクを表示します。

### それぞれの機能は何ができるか

- Flask: Web 画面とサーバーのやり取りを担当します。
- yt-dlp: YouTube から音声や動画を取得する役割です。
- ffmpeg: 音声形式を変換したり、音声を取り出したりする役割です。
- HTML/CSS/JavaScript: 画面の見た目や入力フォームの動きを担当します。
