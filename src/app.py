import os
import subprocess
from pathlib import Path
from flask import Flask, jsonify, render_template, request, send_from_directory

from src.converter import convert_youtube_to_mp3, convert_youtube_to_mp4

app = Flask(__name__, template_folder="templates", static_folder="static")


def log_status(message: str) -> None:
    """バッチ画面に進み具合を表示する。

    概要:
        start.bat で開いた黒い画面に、変換の開始や完了などの状態を表示します。
    引数:
        message: 画面に表示したいメッセージです。
    戻り値:
        ありません。
    """
    print(f"[app] {message}", flush=True)


@app.get('/')
def index():
    """トップページを表示する。

    概要:
        YouTube URLを入力して、MP3またはMP4変換を選ぶ画面を返します。
    引数:
        ありません。
    戻り値:
        入力フォームを含むHTMLページです。
    """
    return render_template('index.html')


@app.post('/convert')
def convert():
    """YouTube URLを指定形式に変換する。

    概要:
        フォームから送られたURLと形式を受け取り、MP3またはMP4ファイルを作ります。
    引数:
        ありません。URLと形式はブラウザから送られるフォームデータで受け取ります。
    戻り値:
        成功時は結果ページ、失敗時はエラー内容を含むJSONレスポンスです。
    """
    # ブラウザから送られてきたURLと変換形式を取り出します。
    url = request.form.get('url', '').strip()
    output_format = request.form.get('format', 'mp3').strip().lower()

    # URLが空、または形式がMP3/MP4以外なら、変換せずにエラーを返します。
    if not url:
        return jsonify({"error": "URL is required"}), 400
    if output_format not in {"mp3", "mp4"}:
        return jsonify({"error": "Format must be mp3 or mp4"}), 400

    log_status(f"Received URL: {url}")
    log_status(f"Starting {output_format.upper()} conversion")

    try:
        # 押されたボタンに合わせて、MP3用またはMP4用の変換処理を選びます。
        if output_format == "mp4":
            output_path = convert_youtube_to_mp4(url)
        else:
            output_path = convert_youtube_to_mp3(url)
    except FileNotFoundError as exc:
        # yt-dlpやffmpegなど、必要な道具が見つからないときのエラーです。
        tool_name = str(exc)
        log_status(f"Required tool not found: {tool_name}")
        detail = (
            f"Required tool not found: {tool_name}. "
            "Please install ffmpeg and make sure it is available on PATH."
            if tool_name == "ffmpeg" else
            f"Required tool not found: {tool_name}."
        )
        return jsonify({"error": detail}), 500
    except subprocess.CalledProcessError as exc:
        # yt-dlpやffmpegが途中で失敗したときは、出力された説明を画面へ返します。
        detail = exc.stderr or exc.stdout or str(exc)
        log_status(f"Conversion failed: {detail}")
        return jsonify({"error": f"Conversion failed: {detail}"}), 500
    except Exception as exc:  # pragma: no cover - defensive path
        log_status(f"Unexpected error: {exc}")
        return jsonify({"error": f"Unexpected error: {exc}"}), 500

    # 作ったファイル名だけを取り出して、ダウンロードリンクに使います。
    output_file = Path(output_path).name
    log_status(f"Conversion completed: {output_path}")
    return render_template(
        'result.html',
        message=f"Saved {output_format.upper()} to {output_path}",
        filename=output_file,
        format=output_format.upper(),
    ), 200


@app.get('/download/<path:filename>')
def download(filename: str):
    """変換済みファイルをダウンロードする。

    概要:
        outputフォルダに保存されたMP3またはMP4ファイルをブラウザへ送ります。
    引数:
        filename: ダウンロードしたいファイル名です。
    戻り値:
        指定されたファイルを添付ファイルとして返すレスポンスです。
    """
    return send_from_directory(Path('output').resolve(), filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 8000)))
