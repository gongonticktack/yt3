import pytest
from src.app import app


@pytest.fixture
def client():
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client


def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"YouTube URL" in response.data
    assert b"MP3 / MP4 Converter" in response.data
    assert b'value="mp3"' in response.data
    assert b'value="mp4"' in response.data
    assert b"color-scheme: dark" in response.data
    assert b"/static/css/style.css" in response.data
    assert b"/static/js/main.js" in response.data


def test_convert_requires_url(client):
    response = client.post('/convert', data={})
    assert response.status_code == 400
    assert b"URL is required" in response.data


def test_convert_mp4_uses_mp4_converter(client, monkeypatch):
    def fake_convert(url):
        assert url == "https://www.youtube.com/watch?v=abc123"
        return "output/abc123.mp4"

    monkeypatch.setattr("src.app.convert_youtube_to_mp4", fake_convert)

    response = client.post(
        '/convert',
        data={"url": "https://www.youtube.com/watch?v=abc123", "format": "mp4"},
    )

    assert response.status_code == 200
    assert b"Saved MP4" in response.data
    assert b"Download MP4" in response.data
