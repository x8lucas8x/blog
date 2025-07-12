import json

from starlette.requests import Request
from starlette.routing import Route

from src.models import Category, Items, Paginator
from src.utils.env import env
from src.utils.templates import templates


async def get_category_index(request: Request) -> templates.TemplateResponse:
    return templates.TemplateResponse(
        request,
        "directories.html.jinja",
        context=dict(
            request=request,
            categories=list(request.state.articles_by_category.keys()),
            directory_title="Articles by category",
            directories=request.state.articles_by_category.items(),
            **env(),
        ),
    )


async def get_category(request: Request) -> templates.TemplateResponse:
    category = Category(request.path_params["category"])

    try:
        page = int(request.path_params.get("page", "1"))
    except ValueError:
        page = 1

    if category not in request.state.articles_by_category:
        return None

    articles = Items(request.state.articles_by_category[category])
    paginator = Paginator(items=articles, route_name="category_detail", page=page)
    return templates.TemplateResponse(
        request,
        "directory.html.jinja",
        context=dict(
            request=request,
            category=category.alias,
            directory_title=f"Articles with {category} category",
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
                                "name": category.alias,
                                "item": category.path(request),
                            },
                        ],
                    },
                ]
            ),
            **env(),
        ),
    )


routes_for_categories = [
    Route("/", get_category_index, name="category_list"),
    Route("/{category:str}/", get_category, name="category_detail"),
    Route(
        "/{category:str}/pages/{page:int}/", get_category, name="category_detail_by_page"
    ),
]
