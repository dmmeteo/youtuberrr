import re

from jinja2 import Environment, FileSystemLoader
from litestar import Litestar, Request, get
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.response import Response, Template
from litestar.template.config import TemplateConfig
from yt_dlp import version
from yt_dlp.utils import YoutubeDLError

from app.routers.download import DownloadController


def filesizeformat(value):
    if value is None:
        return "N/A"
    if not isinstance(value, (int, float)):
        return value
    if value < 1024:
        return f"{value} B"
    if value < 1024 * 1024:
        return f"{value / 1024:.2f} KB"
    if value < 1024 * 1024 * 1024:
        return f"{value / (1024 * 1024):.2f} MB"
    return f"{value / (1024 * 1024 * 1024):.2f} GB"


@get("/", sync_to_thread=False)
def index() -> Template:
    yt_dlp_version = f"{version.ORIGIN}:{version.CHANNEL} ({version.__version__})"
    return Template(template_name="index.html", context={"message": yt_dlp_version})


# 1. Create a Jinja Environment
jinja_env = Environment(loader=FileSystemLoader("app/templates"), autoescape=True)

# 2. Register the custom filter
jinja_env.filters["filesizeformat"] = filesizeformat

# 3. Create the Litestar TemplateConfig
template_config = TemplateConfig(engine=JinjaTemplateEngine.from_environment(jinja_env))


def handle_youtube_dl_errors(request: Request, exc: YoutubeDLError) -> Response:
    """Handle YoutubeDL errors."""
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    error_message = ansi_escape.sub("", str(exc))
    return Response(
        content={"status_code": 500, "detail": error_message},
        status_code=500,
        media_type="application/json",
    )


app = Litestar(
    route_handlers=[index, DownloadController],
    template_config=template_config,
    exception_handlers={YoutubeDLError: handle_youtube_dl_errors},
)
