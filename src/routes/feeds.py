import asyncio
import uvicorn
import uvloop

from dataclasses import asdict
from starlette.routing import Route
from starlette.requests import Request

from src.models import Items, Paginator, Category, Tag
from src.utils.templates import templates
from src.utils.env import env


async def get_rss_feed(request: Request) -> templates.TemplateResponse:
    articles = Items(request.state.sorted_articles)

    return templates.TemplateResponse(
        request,
        'feed.rss.jinja',
        context=dict(
            title=f"{env()['SITE_NAME']} Full RSS feed",
            description=f"{env()['SITE_NAME']} RSS feed for all articles.",
            url=request.url_for("index_list"),
            request=request,
            articles=articles,
            **env(),
        ),
    )


async def get_atom_feed(request: Request) -> templates.TemplateResponse:
    articles = Items(request.state.sorted_articles)

    return templates.TemplateResponse(
        request,
        'feed.atom.jinja',
        context=dict(
            title=f"{env()['SITE_NAME']} Full ATOM feed",
            description=f"{env()['SITE_NAME']} ATOM feed for all articles.",
            url=request.url_for("index_list"),
            request=request,
            articles=articles,
            **env(),
        ),
    )


async def get_category_rss_feed(request: Request) -> templates.TemplateResponse:
    category = Category(request.path_params["category"])

    if category not in request.state.articles_by_category:
        return None

    articles = Items(request.state.articles_by_category[category])
    return templates.TemplateResponse(
        request,
        'feed.rss.jinja',
        context=dict(
            title=f"{env()['SITE_NAME']} RSS feed - Category: {category}",
            description=f"{env()['SITE_NAME']} RSS feed for all articles categorized as {category} related.",
            url=request.url_for("category_detail", category=category),
            request=request,
            articles=articles,
            **env(),
        ),
    )


async def get_category_atom_feed(request: Request) -> templates.TemplateResponse:
    category = Category(request.path_params["category"])

    if category not in request.state.articles_by_category:
        return None

    articles = Items(request.state.articles_by_category[category])
    return templates.TemplateResponse(
        request,
        'feed.atom.jinja',
        context=dict(
            title=f"{env()['SITE_NAME']} ATOM feed - Category: {category}",
            description=f"{env()['SITE_NAME']} ATOM feed for all articles categorized as {category} related.",
            url=request.url_for("category_detail", category=category),
            request=request,
            articles=articles,
            **env(),
        ),
    )


async def get_tag_rss_feed(request: Request) -> templates.TemplateResponse:
    tag = Tag(request.path_params["tag"])

    if tag not in request.state.articles_by_tag:
        return None

    articles = Items(request.state.articles_by_tag[tag])
    return templates.TemplateResponse(
        request,
        'feed.rss.jinja',
        context=dict(
            title=f"{env()['SITE_NAME']} RSS feed - Tag: {tag}",
            description=f"{env()['SITE_NAME']} RSS feed for all articles tagged as {tag} related.",
            url=request.url_for("tag_detail", tag=tag),
            request=request,
            articles=articles,
            **env(),
        ),
    )


async def get_tag_atom_feed(request: Request) -> templates.TemplateResponse:
    tag = Tag(request.path_params["tag"])

    if tag not in request.state.articles_by_tag:
        return None

    articles = Items(request.state.articles_by_tag[tag])
    return templates.TemplateResponse(
        request,
        'feed.atom.jinja',
        context=dict(
            title=f"{env()['SITE_NAME']} ATOM feed - Tag: {tag}",
            description=f"{env()['SITE_NAME']} ATOM feed for all articles tagged as {tag} related.",
            url=request.url_for("tag_detail", tag=tag),
            request=request,
            articles=articles,
            **env(),
        ),
    )


routes_for_feeds = [
    Route("/all.feed.rss", get_rss_feed, name="all_rss_feed"),
    Route("/all.feed.atom", get_atom_feed, name="all_atom_feed"),
    Route("/{category:str}.category.feed.rss", get_category_rss_feed, name="category_rss_feed"),
    Route("/{category:str}.category.feed.atom", get_category_atom_feed, name="category_atom_feed"),
    Route("/{tag:str}.tag.feed.rss", get_tag_rss_feed, name="tag_rss_feed"),
    Route("/{tag:str}.tag.feed.atom", get_tag_atom_feed, name="tag_atom_feed"),
]
