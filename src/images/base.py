from pathlib import Path

from wand.color import Color
from wand.image import Image


def generate_image(
    image_path: str, output_path: str, width: int | None = None, height: int | None = None
) -> None:
    output_path_dir = Path(output_path).parent
    if not output_path_dir.exists():
        output_path_dir.mkdir(parents=True)

    with Image(filename=image_path, background=Color("transparent")) as img:
        with img.clone() as i:
            if width and height:
                i.sample(width, height)
            i.save(filename=output_path)
