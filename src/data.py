import uvloop
import asyncio

from collections import defaultdict
from datetime import datetime
from dataclasses import dataclass

from src.models import Items, Tag, Category, Article, Paginator, Author
from src.utils.items import items


@dataclass
class Data():
    articles_by_slug: dict[str, Article]
    articles_by_category: dict[Category, list[Article]]
    articles_by_tag: dict[Tag, list[Article]]
    sorted_articles: list[Article]
    num_pages: dict


async def import_data() -> Data:
    result = Data(
        articles_by_slug={},
        articles_by_category=defaultdict(list),
        articles_by_tag=defaultdict(list),
        sorted_articles=[],
        num_pages={},
    )

    async for (metadata, content) in items():
        category = Category(metadata["category"])
        tags = [Tag(tag) for tag in metadata["tags"]] if isinstance(metadata["tags"], list) else [Tag(metadata["tags"])]
        authors = [Author(name=author) for author in metadata["authors"]] if isinstance(metadata["authors"], list) else [Author(metadata["author"])]
        article = Article(
            **{
                **metadata,
                "authors": authors,
                "tags": tags,
                "category": category,
                "created_date": datetime.fromisoformat(metadata["created_date"]),
                "updated_date": datetime.fromisoformat(metadata["updated_date"]) if "update_date" in metadata else None,
                "summary": content[:120].strip() + "...",
                "content": content,
            }
        )

        result.articles_by_slug[metadata["slug"]] = article

    prev_article = None
    next_article = None

    for article in sorted(result.articles_by_slug.values(), key=lambda article: article.created_date, reverse=True):
        if prev_article:
            prev_article.next_article = article
            article.prev_article = prev_article

        result.sorted_articles.append(article)
        result.articles_by_category[article.category].append(article)
        for tag in article.tags:
            result.articles_by_tag[tag].append(article)

        prev_article = article

    result.num_pages = {
        "index": Paginator(result.sorted_articles, route_name=None, page=None).num_pages,
        "category": {
            category: Paginator(articles, route_name=None, page=None).num_pages
            for category, articles in result.articles_by_category.items()
        },
        "tag": {
            tag: Paginator(articles, route_name=None, page=None).num_pages
            for tag, articles in result.articles_by_tag.items()
        },
    }
    return result
