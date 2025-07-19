import asyncio
import concurrent
from collections.abc import Generator
from itertools import chain
from pathlib import Path

import anyio
import minify_html
import uvloop
from anyio import Path as AsyncPath
from anyio import open_file
from httpx import Response
from rich.progress import track
from starlette.testclient import TestClient

from x8lucas8x_blog.app import app
from x8lucas8x_blog.caching import precache_images
from x8lucas8x_blog.data import import_data
from x8lucas8x_blog.utils.base import batch
from x8lucas8x_blog.utils.env import env

MINIFIABLE_EXTENSIONS = frozenset((".html", ".css", ".js", ".json", ".xml"))


def output_paths() -> Generator[tuple[str, str], None, None]:
    data = uvloop.run(import_data())

    for url in [
        app.url_path_for("index_list"),
        app.url_path_for("robots_detail"),
        app.url_path_for("sitemap_detail"),
        app.url_path_for("manifest_detail"),
        app.url_path_for("all_rss_feed"),
        app.url_path_for("all_atom_feed"),
        app.url_path_for("menu_detail"),
        app.url_path_for("search_detail"),
        app.url_path_for("search_index_detail"),
        app.url_path_for("category_list"),
        app.url_path_for("tag_list"),
        app.url_path_for("404_detail"),
    ]:
        yield str(url)

    for url in chain(
        [
            app.url_path_for("index_list_by_page", page=page)
            for page in range(1, data.num_pages["index"] + 1)
        ],
        [
            app.url_path_for("category_detail_by_page", category=category, page=page)
            for category in data.articles_by_category.keys()
            for page in range(1, data.num_pages["category"][category] + 1)
        ],
        [
            app.url_path_for("tag_detail_by_page", tag=tag, page=page)
            for tag in data.articles_by_tag.keys()
            for page in range(1, data.num_pages["tag"][tag] + 1)
        ],
        [
            app.url_path_for("article_detail", slug=slug)
            for slug in data.articles_by_slug.keys()
        ],
        [
            app.url_path_for("article_share_detail", slug=slug)
            for slug in data.articles_by_slug.keys()
        ],
        [
            app.url_path_for("category_detail", category=category)
            for category in data.articles_by_category.keys()
        ],
        [app.url_path_for("tag_detail", tag=tag) for tag in data.articles_by_tag.keys()],
        [
            app.url_path_for("category_rss_feed", category=category)
            for category in data.articles_by_category.keys()
        ],
        [
            app.url_path_for("category_atom_feed", category=category)
            for category in data.articles_by_category.keys()
        ],
        [
            app.url_path_for("tag_rss_feed", tag=tag)
            for tag in data.articles_by_tag.keys()
        ],
        [
            app.url_path_for("tag_atom_feed", tag=tag)
            for tag in data.articles_by_tag.keys()
        ],
    ):
        yield str(url)

    for path in Path("public").glob("**/*.*"):
        yield str(path.relative_to("public"))


async def generate_static(output_paths) -> None:
    limiter = anyio.to_thread.current_default_thread_limiter()
    limiter.total_tokens = 100
    output_path_by_task = dict()

    # Not using the AsyncClient as it won't setup the lifespan context.
    with TestClient(app, base_url=env()["SITE_URL"]) as client:
        async with asyncio.TaskGroup() as tg:
            for url in output_paths:
                output_path = url

                if url.endswith("/"):
                    output_path = f"{url}index.html"

                output_path_file = AsyncPath(f"output/{output_path}")
                output_path_dir = output_path_file.parent
                tg.create_task(create_dir_if_unavailable(output_path_dir))
                task = tg.create_task(anyio.to_thread.run_sync(client.get, url))
                output_path_by_task[task] = output_path_file

        async with asyncio.TaskGroup() as tg:
            async for task in asyncio.as_completed(output_path_by_task.keys()):
                output_path_file = output_path_by_task[task]
                response: Response = task.result()
                tg.create_task(write_file(output_path_file, response))


async def create_dir_if_unavailable(output_path_dir: AsyncPath) -> None:
    if not await output_path_dir.exists():
        await output_path_dir.mkdir(parents=True, exist_ok=True)


async def write_file(output_path_file: AsyncPath, response: Response) -> None:
    if output_path_file.suffix in MINIFIABLE_EXTENSIONS:
        # Text based files.
        file_mode = "wt"
        content = response.text
        # Minifying JS fails.
        content = minify_html.minify(content, minify_css=True, minify_js=False)
    else:
        # Images and other files.
        file_mode = "wb"
        content = response.content

    async with await open_file(output_path_file, file_mode) as file:
        await file.write(content)


def generate_static_chunk(output_paths: tuple[str, str]) -> None:
    uvloop.run(generate_static(output_paths))


def run_generate_static() -> None:
    total_paths = 0
    tasks = []

    with concurrent.futures.ProcessPoolExecutor() as executor:
        tasks.extend(precache_images(executor))

        for chunk in batch(output_paths(), 5):
            total_paths += 5
            task = executor.submit(generate_static_chunk, chunk)
            tasks.append(task)

        for task in track(tasks, description="Generating..."):
            task.result()
