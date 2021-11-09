from typing import Iterable

from pypelines import pypeline


def add_two(x: int) -> int:
    return x + 2


def make_double(x: int) -> int:
    return x * 2


@pypeline
def magic_computations(x: int) -> int:
    return x | add_two | make_double


@pypeline
def even_more_magic_comps(x: Iterable[int]) -> int:
    return x | sum | make_double


@pypeline
def even_more_magic_comps2(x: Iterable[int]) -> int:
    return x | sum | make_double


@pypeline
def even_more_magic_comps3(x: Iterable[int]) -> bool:
    return x | sum | make_double == 90


assert even_more_magic_comps3(range(10))
