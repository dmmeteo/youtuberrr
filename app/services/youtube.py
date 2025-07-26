import uuid

from typing import List, Optional, Tuple

import yt_dlp


class YouTubeService:
    def get_video_info(self, url: str) -> dict:
        ydl_opts = {
            "noplaylist": True,
            "extract_flat": "discard_in_playlist",
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return ydl.sanitize_info(info)

    def download_and_merge(
        self,
        url: str,
        download_video: bool,
        download_audio: bool,
        download_subtitles: bool,
        video_quality: Optional[int],
        output_format: str,
        subtitles: Optional[List[str]] = None,
    ) -> Tuple[str, str]:
        download_id = uuid.uuid4()
        output_template = f"/app/downloads/{download_id}/%(title)s.%(ext)s"

        format_string = "best"
        if download_audio:
            format_string += f"bestvideo[height<={video_quality}]+bestaudio/best"
        elif download_video:
            format_string = f"bestvideo[height<={video_quality}]"
        elif download_audio:
            format_string = "bestaudio"
        else:
            raise ValueError("Either video or audio must be selected for download.")

        final_filepath = None

        def progress_hook(d):
            nonlocal final_filepath
            if d["status"] == "finished":
                final_filepath = d.get("_filename") or d.get("filename")

        ydl_opts = {
            "subtitleslangs": "all" if download_subtitles else None,
            "noplaylist": True,
            "writethumbnail": True,
            "outtmpl": output_template,
            "format": format_string,
            "merge_output_format": output_format,
            "progress_hooks": [progress_hook],
        }

        if subtitles:
            ydl_opts["writesubtitles"] = True
            ydl_opts["subtitleslangs"] = subtitles

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        if not final_filepath:
            raise Exception("Download finished, but the final file path could not be determined.")

        filename = final_filepath.split("/")[-1]
        return str(download_id), filename
