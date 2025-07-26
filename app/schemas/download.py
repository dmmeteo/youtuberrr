from typing import List, Optional

from pydantic import BaseModel, Field, HttpUrl


class DownloadRequest(BaseModel):
    url: HttpUrl
    download_video: bool = Field(default=False)
    download_audio: bool = Field(default=False)
    download_subtitles: bool = Field(default=False)
    video_quality: Optional[int] = None
    output_format: str = "mp4"
    subtitles: Optional[List[str]] = None


class InfoRequest(BaseModel):
    url: str
