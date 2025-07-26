import uuid

from unittest.mock import patch

from litestar.testing import TestClient

from app.main import app


def test_get_video_info_success():
    mock_info = {
        "title": "Test Video",
        "thumbnail": "http://example.com/thumb.jpg",
        "formats": [
            {"format_id": "1", "ext": "mp4", "resolution": "1080p"},
            {"format_id": "2", "ext": "webm", "resolution": "720p"},
        ],
        "subtitles": {
            "en": [{"ext": "srt", "url": "http://example.com/en.srt"}],
            "uk": [{"ext": "vtt", "url": "http://example.com/uk.vtt"}],
        },
    }

    with patch("app.services.youtube.YouTubeService.get_video_info", return_value=mock_info) as mock_get_info:
        with TestClient(app=app) as client:
            response = client.post("/info", json={"url": "http://youtube.com/watch?v=test"})
            assert response.status_code == 200
            mock_get_info.assert_called_once_with("http://youtube.com/watch?v=test")


def test_process_download_success():
    download_id = uuid.uuid4()
    filename = "test_video.mp4"
    mock_return_value = (str(download_id), filename)

    with patch(
        "app.services.youtube.YouTubeService.download_and_merge", return_value=mock_return_value
    ) as mock_download:
        with TestClient(app=app) as client:
            response = client.post(
                "/process-download",
                json={
                    "url": "http://youtube.com/watch?v=test",
                    "download_video": True,
                    "download_audio": True,
                    "video_quality": "1080p",
                    "output_format": "mp4",
                    "subtitles": ["en"],
                },
            )
            assert response.status_code == 200
            mock_download.assert_called_once_with(
                url="http://youtube.com/watch?v=test",
                download_video=True,
                download_audio=True,
                video_quality="1080p",
                output_format="mp4",
                subtitles=["en"],
            )
            assert f"/download-file/{download_id}/{filename}" in response.text
