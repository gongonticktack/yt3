# YouTube MP3 / MP4 Web App

このプロジェクトは、YouTube URL を入力すると MP3 または MP4 に変換できる Flask 製のWebアプリです。

## 概要

- ブラウザから YouTube URL を入力できます。
- `Convert to MP3` ボタンで音声ファイルを作成できます。
- `Convert to MP4` ボタンで動画ファイルを作成できます。
- 変換後のファイルは [output](output) フォルダに保存されます。
- 結果ページに目立つダウンロードボタンが表示されます。
- Windows では [start.bat](start.bat) をダブルクリックするだけで起動できます。

## 依存関係

- Python 3.10 以上
- Flask
- yt-dlp
- Deno 2.3 以上、または Node.js 22 以上（YouTube の JavaScript チャレンジ用）
- imageio-ffmpeg
- pytest

`imageio-ffmpeg` を使うため、通常はWindowsへ別途 ffmpeg を手動インストールしなくても動作します。JavaScript ランタイムは PATH に登録してください。Deno があればそれを、なければ Node.js を `yt-dlp` に指定します。`yt-dlp[default]` から EJS チャレンジ処理もインストールされます。

手動で依存関係を入れる場合:

```bash
python -m pip install -r requirements.txt
```

## 起動手順

Windows では、プロジェクトフォルダの [start.bat](start.bat) をダブルクリックします。

1. Python が入っているか確認します。
2. Python が見つからない場合、`winget` が使える環境では Python 3.12 のインストールを試します。
3. `.venv` がなければ仮想環境を作成します。
4. 仮想環境を有効化します。
5. `pip` が使えるか確認します。
6. [requirements.txt](requirements.txt) から必要なPythonパッケージをインストールします。
7. `imageio-ffmpeg` 同梱の ffmpeg が使えるか確認します。
8. YouTube 用の JavaScript ランタイムがあるか確認します。
9. `python -m src.run` で Flask アプリを起動します。

古い仮想環境で JavaScript ランタイムの警告や HTTP 403 が出た場合は、プロジェクトフォルダで `.venv\Scripts\python.exe -m pip install -U -r requirements.txt` を実行してから再起動してください。動画固有の公開範囲や YouTube 側の制限による 403 は、更新後も発生する場合があります。

起動できたら、ブラウザで次のURLを開きます。

```text
http://127.0.0.1:8000
```

## 使い方

1. 画面の入力欄に YouTube URL を入れます。
2. 音声だけ保存したい場合は `Convert to MP3` を押します。
3. 動画として保存したい場合は `Convert to MP4` を押します。
4. 変換が終わると結果ページに移動します。
5. `Download MP3` または `Download MP4` ボタンからファイルをダウンロードできます。

## start.bat で行っていること

[start.bat](start.bat) は、Windowsで起動しやすくするためのバッチファイルです。

- プロジェクトフォルダへ移動する
- Python が使えるか確認する
- 必要なら `winget` で Python を入れる
- `.venv` 仮想環境を作成する
- 仮想環境を有効化する
- `pip` を確認する
- [requirements.txt](requirements.txt) の依存関係を入れる
- `ffmpeg` が使えるか確認する
- Deno または Node.js が使えるか確認する
- Flask アプリを起動する

## 仕様

- `/`
  - URL入力フォームを表示します。
- `/convert`
  - URLと変換形式を受け取ります。
  - `format=mp3` の場合は MP3 を作成します。
  - `format=mp4` の場合は MP4 を作成します。
- `/download/<filename>`
  - [output](output) フォルダ内の変換済みファイルをダウンロードします。

## ディレクトリ構成

```text
.
├── .github/                  # GitHub / Copilot 向けの設定ファイル
│   ├── copilot-instructions.md  # 作業内容に合うスキルへの道案内
│   └── skills/               # このプロジェクトと用途別のスキル
│       ├── .system/          # スキル・プラグイン管理など
│       ├── aspnet-core/      # 用途別スキルの例（ほかにも直下に配置）
│       ├── app-structure/   # アプリ構成と出力
│       ├── ai-resource-efficiency/ # AI 全般の品質を保つリソース効率化
│       ├── quality-checks/  # コード変更時の品質確認
│       ├── readme/          # README の維持
│       ├── ui-design/       # UI デザイン
│       └── work-guidelines/ # 共通の作業方針
├── docs/                     # 調査・運用資料
│   └── skills-inventory.md   # スキル一覧と配置
├── output/                   # 変換後のMP3/MP4を保存する場所
│   └── .gitkeep              # outputフォルダをGitに残すための空ファイル
├── src/                      # Flaskアプリ本体
│   ├── __init__.py           # Pythonパッケージとして扱うためのファイル
│   ├── app.py                # ルーティングと画面表示を担当
│   ├── converter.py          # YouTubeから取得してMP3/MP4へ変換する処理
│   ├── run.py                # Flaskアプリを起動する入口
│   ├── static/               # CSS / JavaScript
│   │   ├── css/
│   │   │   └── style.css     # 画面の見た目
│   │   └── js/
│   │       └── main.js       # フォーム送信時の動き
│   └── templates/            # HTMLテンプレート
│       ├── index.html        # URL入力画面
│       └── result.html       # 変換結果画面
├── tests/                    # pytestのテスト
├── .gitignore                # Git管理から外すファイルの設定
├── README.md                 # この説明書
├── requirements.txt          # Python依存関係
└── start.bat                 # Windows用起動ファイル
```

## Git管理について

[.gitignore](.gitignore) では、次のように設定しています。

- `.venv/` はGit管理外
- `__pycache__/` や `.pytest_cache/` はGit管理外
- [output](output) の中に作られるMP3/MP4ファイルはGit管理外
- [output/.gitkeep](output/.gitkeep) だけはGit管理に含め、フォルダ自体を残す

## 仕組み

このアプリは、次の流れで変換を行います。

1. [src/templates/index.html](src/templates/index.html) が入力画面を表示します。
2. ユーザーがURLを入力し、MP3またはMP4のボタンを押します。
3. [src/app.py](src/app.py) がURLと変換形式を受け取ります。
4. [src/converter.py](src/converter.py) が `yt-dlp` でYouTubeから音声または動画を取得します。
5. `ffmpeg` でMP3またはMP4形式へ変換します。
6. 変換済みファイルを [output](output) フォルダへ保存します。
7. 結果ページにダウンロードボタンを表示します。

## テスト

テストは `pytest` で実行できます。

```bash
python -m pytest
```

現在のテストでは、トップページ表示、URL未入力時のエラー、MP4変換分岐、MP3/MP4変換コマンドの組み立てなどを確認しています。
