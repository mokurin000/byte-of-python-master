# implement your own sum(), product()
# that accepts numerous of primitive numeric data.
# iterable object support is optional, implement it if you can

# Note: product calculates product off all input numbers,
# unlike `itertools.product`, which produces Cartesian product.

from decimal import Decimal # 高精度有限位数十进制数计算
from typing import Any


def my_sum(*nums, initial: int | float | Any = 0):
    sum_ = initial

    for num in nums:
        sum_ += num
    return sum_


def my_product(*nums, initial: int | float | Any = 1):
    product = initial

    for num in nums:
        product *= num
    return product

print(my_sum(1.,2.,3.,4.,5., initial=0.0))
print(my_sum(Decimal("10000000"), Decimal("0.003001"), initial=Decimal("0.0")))