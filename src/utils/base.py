from typing import Iterable
from typing import TypeVar
from itertools import islice

X = TypeVar("X")


def batch(it: Iterable[X], size: int) -> Iterable[tuple[X, ...]]:
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())