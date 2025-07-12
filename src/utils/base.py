from collections.abc import Iterable
from itertools import islice
from typing import TypeVar

X = TypeVar("X")


def batch[X](it: Iterable[X], size: int) -> Iterable[tuple[X, ...]]:
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())
