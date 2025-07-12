import concurrent
import contextlib

import uvicorn
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from x8lucas8x_blog.caching import precache_images
from x8lucas8x_blog.data import import_data
from x8lucas8x_blog.routes.categories import routes_for_categories
from x8lucas8x_blog.routes.feeds import routes_for_feeds
from x8lucas8x_blog.routes.index import routes_for_index
from x8lucas8x_blog.routes.posts import routes_for_posts
from x8lucas8x_blog.routes.tags import routes_for_tags
from x8lucas8x_blog.utils.env import env
from x8lucas8x_blog.utils.templates import templates


async def not_found_index(
    request: Request, exc: Exception | None = None
) -> templates.TemplateResponse:
    return templates.TemplateResponse(
        request,
        "404.html.jinja",
        context=dict(
            request=request,
            **env(),
        ),
    )


@contextlib.asynccontextmanager
async def lifespan(app):
    data = await import_data()

    # Add data to request.state, which views can access.
    yield {**data.__dict__}


routes = [
    Mount(
        "/static", StaticFiles(directory="public/static", check_dir=True), name="static"
    ),
    Mount("/posts", routes=routes_for_posts),
    Mount("/categories", routes=routes_for_categories),
    Mount("/tags", routes=routes_for_tags),
    Mount("/feeds", routes=routes_for_feeds),
    Route("/404/", not_found_index, name="404_detail"),
    Mount("", routes=routes_for_index),
]


exception_handlers = {
    404: not_found_index,
}

app = Starlette(
    debug=True, routes=routes, lifespan=lifespan, exception_handlers=exception_handlers
)


def run_server(port: int) -> None:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        tasks = precache_images(executor)

        for task in tasks:
            task.result()
    uvicorn.run(
        "x8lucas8x_blog.app:app",
        host="127.0.0.1",
        port=port,
        log_level="info",
        reload=True,
    )
