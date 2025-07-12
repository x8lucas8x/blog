import json

from starlette.requests import Request
from starlette.routing import Route

from src.models import Items, Paginator, Tag
from src.utils.env import env
from src.utils.templates import templates


async def get_tag_index(request: Request) -> templates.TemplateResponse:
    return templates.TemplateResponse(
        request,
        "directories.html.jinja",
        context=dict(
            request=request,
            categories=list(request.state.articles_by_category.keys()),
            directory_title="Articles by tag",
            directories=request.state.articles_by_tag.items(),
            **env(),
        ),
    )


async def get_tag(request: Request) -> templates.TemplateResponse:
    tag = Tag(request.path_params["tag"])

    try:
        page = int(request.path_params.get("page", "1"))
    except ValueError:
        page = 1

    if tag not in request.state.articles_by_tag:
        return None

    articles = Items(request.state.articles_by_tag[tag])
    paginator = Paginator(items=articles, route_name="tag_detail", page=page)
    return templates.TemplateResponse(
        request,
        "directory.html.jinja",
        context=dict(
            request=request,
            tag=tag.alias,
            directory_title=f"Articles with {tag} tag",
            articles=paginator.items_for_page(),
            paginator=paginator,
            json_ld=json.dumps(
                [
                    {
                        "@context": "https://schema.org",
                        "@type": "BreadcrumbList",
                        "itemListElement": [
                            {
                                "@type": "ListItem",
                                "position": 1,
                                "name": "Posts",
                                "item": request.url_for("index_list").path,
                            },
                            {
                                "@type": "ListItem",
                                "position": 2,
                                "name": tag.alias,
                                "item": tag.path(request),
                            },
                        ],
                    },
                ]
            ),
            **env(),
        ),
    )


routes_for_tags = [
    Route("/", get_tag_index, name="tag_list"),
    Route("/{tag:str}/", get_tag, name="tag_detail"),
    Route("/{tag:str}/pages/{page:int}/", get_tag, name="tag_detail_by_page"),
]
