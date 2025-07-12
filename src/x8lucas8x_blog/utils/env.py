import os
from functools import cache

from x8lucas8x_blog.settings import dev, prod


@cache
def env() -> dict:
    env = dev

    if os.getenv("ENV", "").lower() == "prod":
        env = prod

    return vars(env)
