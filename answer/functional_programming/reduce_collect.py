from functools import reduce
from typing import Iterable, TypeVar

T = TypeVar("T")


def flatten(it: Iterable[list[T]]) -> list[T]:
    return reduce(lambda a, b: a + b, it)


def horner_eval_polynomial(x: float, it: Iterable[float]) -> float:
    return reduce(lambda r, c: r * x + c, it)


assert flatten([[1, 2], [3, 4], [5, 6, 7], [8]]) == [1, 2, 3, 4, 5, 6, 7, 8]
assert horner_eval_polynomial(3, [2, 3, 4]) == 31
assert horner_eval_polynomial(3, [2, 3, 4, 1]) == 94
print("通过了所有测试！")
