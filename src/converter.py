import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import parse_qs, urlparse


def _safe_output_name(url: str) -> str:
    """MP3用の安全なファイル名を作る。

    概要:
        YouTube URLから動画IDなどを取り出し、保存に使うMP3ファイル名を作ります。
    引数:
        url: 変換したいYouTube動画のURLです。
    戻り値:
        outputフォルダに保存するときのMP3ファイル名です。
    """
    return f"{_safe_output_stem(url)}.mp3"


def _safe_output_stem(url: str) -> str:
    """拡張子なしの安全なファイル名を作る。

    概要:
        URLのクエリやパスから動画IDらしい文字列を取り出し、ファイル名の土台にします。
    引数:
        url: 変換したいYouTube動画のURLです。
    戻り値:
        拡張子を付ける前のファイル名です。
    """
    # URLを部品に分けると、動画IDを取り出しやすくなります。
    parsed = urlparse(url)
    video_id = None

    # 通常のYouTube URLでは、v=xxxx の xxxx が動画IDです。
    if parsed.query:
        params = parse_qs(parsed.query)
        video_id = params.get("v", [None])[0]

    # v= がない短縮URLなどでは、パスの最後を名前として使います。
    if not video_id:
        video_id = parsed.path.strip("/").split("/")[-1] or "video"
    return video_id


def _resolve_tool_path(tool_name: str) -> str:
    """必要な外部ツールの場所を探す。

    概要:
        yt-dlpやffmpegがどこにあるかを探し、実行できるパスを返します。
    引数:
        tool_name: 探したいツール名です。例: "yt-dlp"、"ffmpeg"。
    戻り値:
        見つかった実行ファイルのパスです。
    """
    # Windowsでは .exe 付きの名前で見つかることがあるため、候補を増やします。
    candidates = [tool_name]
    if tool_name == "ffmpeg":
        candidates.append("ffmpeg.exe")
    if tool_name == "yt-dlp":
        candidates.append("yt-dlp.exe")

    # PATHに登録されている場所から、指定したツールを探します。
    for candidate in candidates:
        tool_path = shutil.which(candidate)
        if tool_path:
            return tool_path

    # ffmpegはPythonパッケージに同梱したものも使えます。
    if tool_name == "ffmpeg":
        try:
            import imageio_ffmpeg

            return imageio_ffmpeg.get_ffmpeg_exe()
        except Exception as exc:
            raise FileNotFoundError(tool_name) from exc

    raise FileNotFoundError(tool_name)


def convert_youtube_to_mp3(url: str) -> str:
    """YouTube動画をMP3音声に変換する。

    概要:
        YouTubeから音声をダウンロードし、ffmpegでMP3ファイルに変換します。
    引数:
        url: 変換したいYouTube動画のURLです。
    戻り値:
        作成されたMP3ファイルの保存先パスです。
    """
    # 変換後のファイルを入れるoutputフォルダを用意します。
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / _safe_output_name(url)

    # 同じ名前の古いファイルがあれば、新しい変換結果で置き換えます。
    if output_path.exists():
        output_path.unlink()

    # ダウンロード用のyt-dlpと、変換用のffmpegの場所を確認します。
    yt_dlp = _resolve_tool_path("yt-dlp")
    ffmpeg = _resolve_tool_path("ffmpeg")

    # 一時フォルダに元データを置き、最後にMP3だけをoutputへ残します。
    with tempfile.TemporaryDirectory(dir=str(output_dir), prefix="tmp_", suffix="_audio") as temp_dir_name:
        temp_dir = Path(temp_dir_name)
        download_template = str(temp_dir / "%(title)s.%(ext)s")

        # yt-dlpには、まず一番よい音声データを保存してもらいます。
        download_command = [
            yt_dlp,
            "--format",
            "bestaudio/best",
            "--no-playlist",
            "--output-na-placeholder",
            "",
            "-o",
            download_template,
            url,
        ]

        # ログに日本語や特殊文字が混ざっても落ちないよう、文字コードを指定します。
        subprocess.run(
            download_command,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )

        # ダウンロード中の.partファイルは未完成なので除外します。
        downloaded_files = sorted(
            path for path in temp_dir.iterdir() if path.is_file() and path.suffix.lower() != ".part"
        )
        if not downloaded_files:
            raise RuntimeError("No audio file was produced by yt-dlp")

        # ffmpegで元の音声をMP3形式に変換します。
        source_audio = downloaded_files[0]
        convert_command = [
            ffmpeg,
            "-y",
            "-i",
            str(source_audio),
            "-vn",
            "-acodec",
            "libmp3lame",
            "-q:a",
            "2",
            str(output_path),
        ]

        # 変換時のログも、文字コードの違いで落ちないように読み取ります。
        subprocess.run(
            convert_command,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )

    return str(output_path)


def convert_youtube_to_mp4(url: str) -> str:
    """YouTube動画をMP4動画に変換する。

    概要:
        YouTubeから動画をダウンロードし、ffmpegでMP4ファイルに変換します。
    引数:
        url: 変換したいYouTube動画のURLです。
    戻り値:
        作成されたMP4ファイルの保存先パスです。
    """
    # 変換後のファイルを入れるoutputフォルダを用意します。
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / f"{_safe_output_stem(url)}.mp4"

    # 同じ名前の古いファイルがあれば、新しい変換結果で置き換えます。
    if output_path.exists():
        output_path.unlink()

    # ダウンロード用のyt-dlpと、変換用のffmpegの場所を確認します。
    yt_dlp = _resolve_tool_path("yt-dlp")
    ffmpeg = _resolve_tool_path("ffmpeg")

    # 一時フォルダに元データを置き、最後にMP4だけをoutputへ残します。
    with tempfile.TemporaryDirectory(dir=str(output_dir), prefix="tmp_", suffix="_video") as temp_dir_name:
        temp_dir = Path(temp_dir_name)
        download_template = str(temp_dir / "%(title)s.%(ext)s")

        # 音声と映像が両方入っている動画を、できるだけMP4形式で取得します。
        download_command = [
            yt_dlp,
            "--format",
            "best[ext=mp4][vcodec!=none][acodec!=none]/best[vcodec!=none][acodec!=none]",
            "--no-playlist",
            "--output-na-placeholder",
            "",
            "-o",
            download_template,
            url,
        ]

        # ログに日本語や特殊文字が混ざっても落ちないよう、文字コードを指定します。
        subprocess.run(
            download_command,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )

        # ダウンロード中の.partファイルは未完成なので除外します。
        downloaded_files = sorted(
            path for path in temp_dir.iterdir() if path.is_file() and path.suffix.lower() != ".part"
        )
        if not downloaded_files:
            raise RuntimeError("No video file was produced by yt-dlp")

        # ffmpegで、ブラウザやスマホで扱いやすいMP4形式に変換します。
        source_video = downloaded_files[0]
        convert_command = [
            ffmpeg,
            "-y",
            "-i",
            str(source_video),
            "-c:v",
            "libx264",
            "-c:a",
            "aac",
            "-movflags",
            "+faststart",
            str(output_path),
        ]

        # 変換時のログも、文字コードの違いで落ちないように読み取ります。
        subprocess.run(
            convert_command,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )

    return str(output_path)
