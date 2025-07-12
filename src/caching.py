import uvloop

from src.data import import_data
from src.images.base import generate_image
from src.images.social_media import generate_social_media_image


def precache_images(executor) -> None:
    data = uvloop.run(import_data())
    tasks = []

    tasks.append(
        executor.submit(
            generate_image,
            image_path="./public/static/icons/icon.svg",
            output_path="public/static/icons/icon.ico",
        )
    )

    default_social_media_background_path = "public/static/assets/defaultPreviewImage.jpeg"

    tasks.append(
        executor.submit(
            generate_social_media_image,
            title="Lucas' Refuge",
            output_path="public/static/social_media/default.png",
            background_path=default_social_media_background_path,
            title_font_path="public/static/fonts/Anton-Regular.ttf",
            quote_font_path="public/static/fonts/Anton-Regular.ttf",
        )
    )

    for x in [48, 72, 96, 144, 180, 192, 256, 384, 512]:
        tasks.append(
            executor.submit(
                generate_image,
                width=x,
                height=x,
                image_path="./public/static/icons/icon.svg",
                output_path=f"public/static/icons/icon-{x}x{x}.png",
            )
        )

    for article in data.sorted_articles:
        tasks.append(
            executor.submit(
                generate_social_media_image,
                title=article.title,
                avatar_path=article.authors[0].avatar_local_path,
                output_path=f"public/static/social_media/{article.slug}.png",
                background_path=default_social_media_background_path,
                quote=article.quote,
                quote_author=article.quote_author,
                title_font_path="public/static/fonts/Anton-Regular.ttf",
                quote_font_path="public/static/fonts/Anton-Regular.ttf",
            )
        )

    return tasks
