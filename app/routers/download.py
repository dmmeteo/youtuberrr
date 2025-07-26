import uuid

from litestar import Controller, get, post
from litestar.response import File, Template

from app.config import DOWNLOADS_DIR
from app.schemas.download import DownloadRequest, InfoRequest
from app.services.youtube import YouTubeService


class DownloadController(Controller):
    @post("/info", status_code=200)
    async def get_info(self, data: InfoRequest) -> Template:
        service = YouTubeService()
        info = service.get_video_info(data.url)
        info["url"] = data.url
        return Template(template_name="download.html", context=info)

    @post("/process-download", status_code=200)
    async def process_download(self, data: DownloadRequest) -> Template:
        # Pydantic v2 automatically handles bool conversion for "on"/"off"
        service = YouTubeService()
        url = str(data.url)
        download_id, filename = service.download_and_merge(
            url=url,
            download_video=data.download_video,
            download_audio=data.download_audio,
            download_subtitles=data.download_subtitles,
            video_quality=data.video_quality,
            output_format=data.output_format,
            subtitles=data.subtitles,
        )
        context = service.get_video_info(url)
        context["download_id"] = download_id
        context["filename"] = filename
        return Template(template_name="download.html", context=context)

    @get("/download-file/{download_id:uuid}/{filename:str}")
    async def download_file(self, download_id: uuid.UUID, filename: str) -> File:
        file_path = DOWNLOADS_DIR / str(download_id) / filename
        return File(path=file_path, filename=filename)
