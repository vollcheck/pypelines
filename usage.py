from functools import partial
from typing import Union, List

from pypelines import pypeline


def add_two(x: int) -> int:
    return x + 2


def make_double(x: int) -> int:
    return x * 2


@pypeline()
def magic_computations(x: int) -> int:
    return x | add_two | make_double


@pypeline()
def even_more_magic_comps(x: int) -> int:
    return x | range | sum | (lambda x: x * 2)


@pypeline()
def magic_equation(x: int) -> bool:
    return x | range | sum | make_double == 90


@pypeline()
def even_more_interesting_computations(x: int) -> List[int]:
    return x | range | partial(map, lambda x: x * x) | list


def fizz_detector(x: int) -> Union[str, int]:
    return (
        "FizzBuzz"
        if x % 15 == 0
        else "Buzz"
        if x % 5 == 0
        else "Fizz"
        if x % 3 == 0
        else x
    )


@pypeline()
def fizzbuzz(x: int) -> List[Union[str, int]]:
    return x | partial(range, 1) | partial(map, fizz_detector) | list
