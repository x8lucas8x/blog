from starlette.requests import Request
from starlette.routing import Route

from src.models import Category, Items, Tag
from src.utils.env import env
from src.utils.templates import templates


async def get_rss_feed(request: Request) -> templates.TemplateResponse:
    articles = Items(request.state.sorted_articles)

    site_name = env()["SITE_NAME"]
    return templates.TemplateResponse(
        request,
        "feed.rss.jinja",
        context=dict(
            title=f"{site_name} Full RSS feed",
            description=f"{site_name} RSS feed for all articles.",
            url=request.url_for("index_list"),
            request=request,
            articles=articles,
            **env(),
        ),
    )


async def get_atom_feed(request: Request) -> templates.TemplateResponse:
    articles = Items(request.state.sorted_articles)

    site_name = env()["SITE_NAME"]
    return templates.TemplateResponse(
        request,
        "feed.atom.jinja",
        context=dict(
            title=f"{site_name} Full ATOM feed",
            description=f"{site_name} ATOM feed for all articles.",
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

    site_name = env()["SITE_NAME"]
    articles = Items(request.state.articles_by_category[category])
    return templates.TemplateResponse(
        request,
        "feed.rss.jinja",
        context=dict(
            title=f"{site_name} RSS feed - Category: {category}",
            description=(
                f"{site_name} RSS feed for all articles "
                f"categorized as {category} related."
            ),
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

    site_name = env()["SITE_NAME"]
    articles = Items(request.state.articles_by_category[category])
    return templates.TemplateResponse(
        request,
        "feed.atom.jinja",
        context=dict(
            title=f"{site_name} ATOM feed - Category: {category}",
            description=(
                f"{site_name} ATOM feed for all articles "
                f"categorized as {category} related."
            ),
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

    site_name = env()["SITE_NAME"]
    articles = Items(request.state.articles_by_tag[tag])
    return templates.TemplateResponse(
        request,
        "feed.rss.jinja",
        context=dict(
            title=f"{site_name} RSS feed - Tag: {tag}",
            description=(
                f"{site_name} RSS feed for all articles tagged as {tag} related."
            ),
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

    site_name = env()["SITE_NAME"]
    articles = Items(request.state.articles_by_tag[tag])
    return templates.TemplateResponse(
        request,
        "feed.atom.jinja",
        context=dict(
            title=f"{site_name} ATOM feed - Tag: {tag}",
            description=(
                f"{site_name} ATOM feed for all articles tagged as {tag} related."
            ),
            url=request.url_for("tag_detail", tag=tag),
            request=request,
            articles=articles,
            **env(),
        ),
    )


routes_for_feeds = [
    Route("/all.feed.rss", get_rss_feed, name="all_rss_feed"),
    Route("/all.feed.atom", get_atom_feed, name="all_atom_feed"),
    Route(
        "/{category:str}.category.feed.rss",
        get_category_rss_feed,
        name="category_rss_feed",
    ),
    Route(
        "/{category:str}.category.feed.atom",
        get_category_atom_feed,
        name="category_atom_feed",
    ),
    Route("/{tag:str}.tag.feed.rss", get_tag_rss_feed, name="tag_rss_feed"),
    Route("/{tag:str}.tag.feed.atom", get_tag_atom_feed, name="tag_atom_feed"),
]
