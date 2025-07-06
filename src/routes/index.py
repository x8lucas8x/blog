import asyncio
import uvicorn
import uvloop
import json

from dataclasses import asdict
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.models import Items, Paginator, Category, Tag
from src.utils.templates import templates
from src.utils.env import env


async def get_index(request: Request) -> templates.TemplateResponse:
    try:
        page = int(request.path_params.get('page', "1"))
    except:
        page = 1

    articles = Items(request.state.sorted_articles)
    paginator = Paginator(items=articles, route_name="index_list", page=page)
    return templates.TemplateResponse(
        request,
        'index.html.jinja',
        context=dict(
            request=request,
            categories=list(request.state.articles_by_category.keys()),
            articles=paginator.items_for_page(),
            paginator=paginator,
            **env(),
        ),
    )


async def get_robots(request: Request) -> templates.TemplateResponse:
    return templates.TemplateResponse(
        request,
        'robots.txt.jinja',
        context=dict(
            request=request,
            **env(),
        ),
    )


async def get_sitemap(request: Request) -> templates.TemplateResponse:
    return templates.TemplateResponse(
        request,
        'sitemap.xml.jinja',
        context=dict(
            request=request,
            items=request.state.sorted_articles,
            **env(),
        ),
    )

async def get_manifest(request: Request) -> JSONResponse:
    icons: list[dict] = []

    for x in [48, 72, 96, 144, 180, 192, 256, 384, 512]:
        icons.append(
            {
                "src": str(request.url_for("static", path=f"/icons/icon-{x}x{x}.png")),
                "sizes": f"{x}x{x}",
                "type": "image/png"
            }
        )

    return JSONResponse({
        "id": "lucas-lira-gomes-blog",
        "name": env()["SITE_NAME"],
        "short_name": "LUR",
        "start_url": "/",
        "background_color": "#ffffff",
        "theme_color": "#c53030",
        "display": "fullscreen",
        "icons": icons,
        "description": env()["SITE_DESCRIPTION"],
        "lang": "en"
    })


async def get_menu(request: Request) -> templates.TemplateResponse:
    return templates.TemplateResponse(
        request,
        'menu.html.jinja',
        context=dict(
            request=request,
            **env(),
        ),
    )


async def get_search(request: Request) -> templates.TemplateResponse:
    return templates.TemplateResponse(
        request,
        'search.html.jinja',
        context=dict(
            request=request,
            num_documents=len(request.state.sorted_articles),
            **env(),
        ),
    )


async def get_search_index(request: Request) -> JSONResponse:
    return JSONResponse(list(dict(
        id=article.slug,
        title=article.title,
        category=article.category.alias,
        tags=[tag.alias for tag in article.tags],
        quote=article.quote,
        summary=article.summary,
        url=article.path(request),
    ) for article in request.state.sorted_articles))



routes_for_index = [
    Route('/', get_index, name="index_list"),
    Route('/robots.txt', get_robots, name="robots_detail"),
    Route('/sitemap.xml', get_sitemap, name="sitemap_detail"),
    Route('/manifest.json', get_manifest, name="manifest_detail"),
    Route('/menu/', get_menu, name="menu_detail"),
    Route('/search/', get_search, name="search_detail"),
    Route('/search/index.json', get_search_index, name="search_index_detail"),
    Route('/pages/{page:int}', get_index, name="index_list_by_page"),
]
