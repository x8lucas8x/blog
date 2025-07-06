import textwrap
import os

from io import BytesIO
from pathlib import Path
from wand.image import Image as WandImage
from wand.color import Color

from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageOps, ImageFilter


def round_corner(radius, fill):
    """Draw a round corner"""
    corner = Image.new('RGBA', (radius, radius), (0, 0, 0, 0))
    draw = ImageDraw.Draw(corner)
    draw.pieslice((0, 0, radius * 2, radius * 2), 180, 270, fill=fill)
    return corner


def round_rectangle(size, radius, fill):
    """Draw a rounded rectangle"""
    width, height = size
    rectangle = Image.new('RGBA', size, fill)
    corner = round_corner(radius, fill)
    rectangle.paste(corner, (0, 0))
    rectangle.paste(corner.rotate(90), (0, height - radius))
    rectangle.paste(corner.rotate(180), (width - radius, height - radius))
    rectangle.paste(corner.rotate(270), (width - radius, 0))
    return rectangle


def generate_social_media_image(
    title: str,
    output_path: str,
    avatar_path: str=None,
    quote: str | None=None,
    quote_author: str | None=None,
    background_path: str | None=None,
    title_font_path: str | None=None,
    quote_font_path: str | None=None,
) -> None:
    # Set image dimensions
    width, height = 970, 509
    border_width = 8
    border_offset = 35
    
    # Create base image
    if background_path and os.path.exists(background_path):
        with WandImage(filename=background_path, background=Color('transparent')) as wand_img:
            with wand_img.clone() as wand_img_clone:
                if width and height:
                    # Wand is faster at resizing than pillow.
                    wand_img_clone.sample(width, height)
                with BytesIO() as img_resize_output:
                    wand_img_clone.save(img_resize_output)
                    background = Image.open(img_resize_output).convert("RGBA")
 
        # Apply 90% transparency
        alpha = Image.new('L', background.size, 255)
        alpha = ImageEnhance.Brightness(alpha).enhance(0.1)
        background.putalpha(alpha)
    else:
        background = Image.new("RGBA", (width, height), (255, 255, 255, 255))

    # Create a blank image
    image = Image.new("RGBA", (width, height), (255, 255, 255, 255))

    # Paste the background onto the white image
    image = Image.alpha_composite(image, background)

    draw = ImageDraw.Draw(image)

    # Draw red rectangle
    draw.rectangle(
        [border_offset, border_offset, width - border_offset, height - border_offset],
        outline=(255, 0, 0, 255),
        width=border_width
    )

    # Load fonts
    title_font_size = 40
    quote_font_size = title_font_size - 3  # 3px bigger than the title
    
    if title_font_path and os.path.exists(title_font_path):
        title_font = ImageFont.truetype(title_font_path, title_font_size)
        quote_font = ImageFont.truetype(title_font_path, quote_font_size)
    else:
        title_font = ImageFont.load_default().font_variant(size=title_font_size)
        quote_font = ImageFont.load_default().font_variant(size=quote_font_size)

    # Add title with red background
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_height = 55
    title_x = (width - title_width) / 2
    title_y = 20  # 5px away from the top border
    
    # Draw red background for title
    draw.rectangle(
        [title_x - 10, title_y - 5, title_x + title_width + 10, title_y + title_height + 5],
        fill=(255, 0, 0, 255)
    )
    
    # Draw title text
    draw.text((title_x, title_y), title, font=title_font, fill=(255, 255, 255, 255))

    if quote and quote_author:
        # Add quote
        quote_lines = textwrap.wrap(quote, width=40)
        quote_y = ((height - len(quote_lines) * (quote_font_size + 5)) / 2) - 20
        for line in quote_lines:
            line_bbox = draw.textbbox((0, 0), line, font=quote_font)
            quote_x = (width - line_bbox[2]) / 2
            draw.text((quote_x, quote_y), line, font=quote_font, fill=(0, 0, 0, 255))
            quote_y += quote_font_size + 5

        quote_y += 30
        line_bbox = draw.textbbox((0, 0), quote_author, font=quote_font)
        quote_x = (width - line_bbox[2]) / 2
        draw.text((quote_x, quote_y), quote_author, font=quote_font, fill=(0, 0, 0, 255))

    if avatar_path:
        # Add rounded avatar
        if os.path.exists(avatar_path):
            avatar = Image.open(avatar_path).convert("RGBA")
            avatar_size = 140
            avatar = avatar.resize((avatar_size, avatar_size), Image.LANCZOS)

            # Apply sharp filter
            avatar = avatar.filter(ImageFilter.SHARPEN)

            # Create a mask for the avatar
            mask = Image.new('L', (avatar_size, avatar_size), 0)
            mask_draw = ImageDraw.Draw(mask)
            mask_draw.ellipse((0, 0, avatar_size, avatar_size), fill=255)

            # Apply the mask to the avatar
            output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
            output.putalpha(mask)

            # Paste the rounded avatar
            image.paste(output, (width - avatar_size - 12, height - avatar_size - 12), output)

    output_path_dir = Path(output_path).parent
    if not output_path_dir.exists():
        output_path_dir.mkdir(parents=True, exist_ok=True)

    image.save(output_path, quality=95, dpi=(300, 300))

