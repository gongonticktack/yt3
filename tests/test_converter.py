import subprocess
import sys
from types import SimpleNamespace
from pathlib import Path

from src import converter


def test_convert_youtube_to_mp3_uses_ffmpeg_to_write_mp3(monkeypatch, tmp_path):
    calls = []

    def fake_run(command, check=True, capture_output=True, text=True, encoding=None, errors=None):
        calls.append(command)
        output_dir = Path("output")
        if output_dir.exists():
            temp_dirs = sorted(
                path for path in output_dir.iterdir() if path.is_dir() and path.name.startswith("tmp_")
            )
            if temp_dirs:
                (temp_dirs[-1] / "sample.webm").write_bytes(b"dummy")
        return subprocess.CompletedProcess(command, 0, "", "")

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(converter.shutil, "which", lambda tool: tool)
    monkeypatch.setattr(converter.subprocess, "run", fake_run)

    output_path = converter.convert_youtube_to_mp3("https://www.youtube.com/watch?v=abc123")

    assert output_path.endswith(".mp3")
    assert len(calls) == 2
    assert calls[0][0] == "yt-dlp"
    assert "--extract-audio" not in calls[0]
    assert "--format" in calls[0]
    assert "bestaudio/best" in calls[0]
    assert calls[1][0] == "ffmpeg"
    assert calls[1][-1] == str(Path("output") / "abc123.mp3")


def test_resolve_ffmpeg_falls_back_to_bundled_package(monkeypatch):
    monkeypatch.setattr(converter.shutil, "which", lambda tool: None)
    monkeypatch.setitem(
        sys.modules,
        "imageio_ffmpeg",
        SimpleNamespace(get_ffmpeg_exe=lambda: "bundled-ffmpeg.exe"),
    )

    assert converter._resolve_tool_path("ffmpeg") == "bundled-ffmpeg.exe"


def test_convert_youtube_to_mp4_writes_mp4(monkeypatch, tmp_path):
    calls = []

    def fake_run(command, check=True, capture_output=True, text=True, encoding=None, errors=None):
        calls.append(command)
        output_dir = Path("output")
        if output_dir.exists():
            temp_dirs = sorted(
                path for path in output_dir.iterdir() if path.is_dir() and path.name.startswith("tmp_")
            )
            if temp_dirs:
                (temp_dirs[-1] / "sample.webm").write_bytes(b"dummy")
        return subprocess.CompletedProcess(command, 0, "", "")

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(converter.shutil, "which", lambda tool: tool)
    monkeypatch.setattr(converter.subprocess, "run", fake_run)

    output_path = converter.convert_youtube_to_mp4("https://www.youtube.com/watch?v=abc123")

    assert output_path.endswith(".mp4")
    assert len(calls) == 2
    assert calls[0][0] == "yt-dlp"
    assert "--format" in calls[0]
    assert calls[1][0] == "ffmpeg"
    assert "-c:v" in calls[1]
    assert calls[1][-1] == str(Path("output") / "abc123.mp4")
