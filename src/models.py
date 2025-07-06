import urllib.parse

from typing import Any
from datetime import datetime
from dataclasses import dataclass
from collections import UserList
from starlette.requests import Request


@dataclass(eq=True, order=True)
class Directory:
    alias: str

    def __post_init__(self) -> None:
        self.alias = self.alias.lower()

    def __str__(self) -> str:
        return self.alias

    def __hash__(self) -> str:
        return hash(self.alias)


class Tag(Directory):
    def path(self, request: Request) -> str:
        return request.url_for("tag_detail", tag=self.alias).path


class Category(Directory):
    def path(self, request: Request) -> str:
        return request.url_for("category_detail", category=self.alias).path


@dataclass
class Author:
    name: str

    @property
    def avatar_local_path(self) -> str:
        return f"./public/static/avatars/{self.name.lower().replace(" ", "")}.jpeg"

    def avatar_path(self, request: Request) -> str:
        return request.url_for("static", path=f"/avatars/{self.name.lower().replace(" ", "")}.jpeg").path


@dataclass
class Item:
    title: str
    slug: str
    created_date: datetime
    updated_date: datetime

    @property
    def last_modified(self) -> datetime:
        return self.updated_date if self.updated_date else self.created_date

    def social_media_absolute_url(self, request: Request) -> str:
        return str(request.url_for("static", path=f"/social_media/{self.slug}.png"))


@dataclass
class Article(Item):
    parent_dir: str
    content: str
    summary: str
    category: list[Category]
    tags: list[Tag]
    authors: list[Author]
    quote: str=None
    quote_author: str=None
    draft: bool=False
    prev_article: Item | None=None
    next_article: Item | None=None

    def absolute_url(self, request: Request) -> str:
        return str(request.url_for("article_detail", slug=self.slug))    

    def path(self, request: Request) -> str:
        return request.url_for("article_detail", slug=self.slug).path

    def share_path(self, request: Request) -> str:
        return request.url_for("article_share_detail", slug=self.slug).path

    def social_share_path(self, platform: str, request: Request) -> str:
        absolute_url = urllib.parse.quote_plus(bytes(self.absolute_url(request), encoding="utf-8"))
        title = urllib.parse.quote_plus(bytes(self.title, encoding="utf-8"))
        text = urllib.parse.quote_plus(bytes(self.summary[:50].strip(), encoding="utf-8"))
        
        share_url = ""
        
        match platform:
            case 'facebook':
                share_url = f"https://www.facebook.com/sharer/sharer.php?u={absolute_url}"
            case 'twitter':
                share_url = f"https://twitter.com/intent/tweet?url={absolute_url}&text={title}"
            case 'linkedin':
                share_url = f"https://www.linkedin.com/sharing/share-offsite/?url={absolute_url}"
            case 'whatsapp':
                share_url = f"https://wa.me/?text={title} {absolute_url}"
            case 'telegram':
                share_url = f"https://t.me/share/url?url={absolute_url}&text={title}"
            case 'reddit':
                share_url = f"https://reddit.com/submit?url={absolute_url}&title={title}"
            case 'pinterest':
                share_url = f"https://pinterest.com/pin/create/a/?url={absolute_url}&description={title}"
            case 'email':
                share_url = f"mailto:?subject={title}&body={text}%20{absolute_url}"
        
        return share_url


@dataclass
class Paginator:
    items: list[Item]
    route_name: str
    page: int

    @property
    def current_page(self) -> int:
        return self.page if (1 <= self.page <= self.num_pages) else 1

    @property
    def items_per_page(self) -> int:
        return 10

    @property
    def num_pages(self) -> int:
        return (len(self.items) // self.items_per_page) + 1

    @property
    def has_next_page(self) -> bool:
        return self.current_page < self.num_pages

    @property
    def has_prev_page(self) -> bool:
        return self.current_page > 1

    @property
    def has_other_pages(self) -> bool:
        return self.has_next_page or self.has_prev_page

    @property
    def next_page(self) -> int:
        return min(self.current_page + 1, self.num_pages)

    @property
    def prev_page(self) -> int:
        return max(1, self.current_page - 1)

    def next_page_path(self, request: Request) -> str:
        path_params = {**request.path_params, "page": self.next_page}
        return request.url_for(f"{self.route_name}_by_page", **path_params).path

    def prev_page_path(self, request: Request) -> str:

        if self.prev_page == 1:
            return self.first_page_path(request)
        else:
            path_params = {**request.path_params, "page": self.prev_page}
            return request.url_for(f"{self.route_name}_by_page", **path_params).path

    def first_page_path(self, request: Request) -> str:
        path_params = {**request.path_params}
        del path_params["page"]

        return request.url_for(self.route_name, **path_params).path

    def last_page_path(self, request: Request) -> str:
        path_params = {**request.path_params, "page": self.num_pages}
        return request.url_for(f"{self.route_name}_by_page", **path_params).path

    def items_for_page(self) -> list[Item]:
        index = (self.current_page - 1) * self.items_per_page
        return self.items[index:index + self.items_per_page]


class Items(UserList):
    data: list[Item]

