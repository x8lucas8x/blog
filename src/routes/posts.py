import asyncio
import contextlib
import uvicorn
import uvloop
import json

from dataclasses import asdict
from starlette.routing import Route
from starlette.requests import Request

from src.utils.templates import templates
from src.utils.env import env


async def get_article(request: Request) -> templates.TemplateResponse:
    slug = request.path_params['slug']
    article = request.state.articles_by_slug.get(slug)

    if article is None:
        return None

    return templates.TemplateResponse(
        request,
        'article.html.jinja',
        context=dict(
            request=request,
            categories=list(request.state.articles_by_category.keys()),
            article=article,
            num_minutes=len(article.content) / 250,
            json_ld=json.dumps([
                {
                    "@context": "https://schema.org",
                    "@type": "BreadcrumbList",
                    "itemListElement": [
                        {
                            "@type": "ListItem",
                            "position": 1,
                            "name": "Posts",
                            "item": request.url_for('index_list').path
                        },
                        {
                            "@type": "ListItem",
                            "position": 2,
                            "name": article.category.alias,
                            "item": article.category.path(request)
                        },
                    ],
                },
                {
                    "@context": "https://schema.org",
                    "@type": "NewsArticle",
                    "headline": article.title,
                    "datePublished": article.created_date.isoformat(),
                    "dateModified": article.last_modified.isoformat(),
                    "image": [
                        article.social_media_path(request)
                    ],
                    "author": [
                        {
                            "@type": "Person",
                            "name": author.name
                        } for author in article.authors
                    ],
                },
            ]),
            **env(),
        ),
    )


async def get_article_share(request: Request) -> templates.TemplateResponse:
    slug = request.path_params['slug']
    article = request.state.articles_by_slug.get(slug)

    if article is None:
        return None

    return templates.TemplateResponse(
        request,
        'article_share.html.jinja',
        context=dict(
            request=request,
            article=article,
            **env(),
        ),
    )


routes_for_posts = [
    Route('/{slug:str}/', get_article, name="article_detail"),
    Route('/{slug:str}/share/', get_article_share, name="article_share_detail"),
]
