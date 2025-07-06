import os

from functools import cache

from src.settings import dev
from src.settings import prod


@cache
def env() -> dict:
    env = dev

    if os.getenv("ENV", "").lower() == "prod":
        env = prod

    return vars(env)