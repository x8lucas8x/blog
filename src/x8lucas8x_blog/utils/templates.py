from jinja2 import FileSystemBytecodeCache
from markdown import Markdown
from starlette.templating import Jinja2Templates

md_with_extensions = Markdown(extensions=["extra", "meta", "toc", "codehilite"])
templates = Jinja2Templates(directory="templates", auto_reload=True)


def markdown_filter(text: str) -> str:
    return md_with_extensions.reset().convert(text)


templates.env.filters["markdown"] = markdown_filter
templates.env.bytecode_cache = FileSystemBytecodeCache()
templates.env.autoescape = False
