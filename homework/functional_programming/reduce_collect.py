from functools import reduce
from typing import Iterable, TypeVar

# 标准库 reduce() 的签名中，
# 先写函数，再写迭代对象，
# 最后是初始化值（可选，没有时从 iterable 取）

# 或者说：
# reduce(function, iterable, initial = None)

# 基于 reduce 实现下列函数，通过测试。

T = TypeVar("T")  # 自定义类型，只做签名用，可以是任何类型。


# 示例函数
#
def my_max(it: Iterable[T]) -> T:
    return reduce(lambda a, b: max(a, b), it)


# “拍平” 一系列列表的成员到单个列表，见下侧示例。
# To flat numerous list[T] to single list[T], in original order.
# Hint: [1] + [2] == [1, 2]
def flatten(it: Iterable[list[T]]) -> list[T]:
    pass


# “捕获”环境变量————实际上 python 一般函数也可以做到一样的事情
# Advanced: capture variable (though python functions can do the same)
def horner_eval_polynomial(x: float, it: Iterable[float]) -> float:
    pass


assert my_max([1, 5, 2, 7, 3, 4]) == 7
assert flatten([[1, 2], [3, 4], [5, 6, 7], [8]]) == [1, 2, 3, 4, 5, 6, 7, 8]

# 霍纳法则，或者说 秦九韶算法
# 2x² + 3x + 4
#   = ((2)x + 3)x + 4
# 留了一个额外的括号，，用来做提示
assert horner_eval_polynomial(3, [2, 3, 4]) == 31
assert horner_eval_polynomial(3, [2, 3, 4, 1]) == 94
print("通过了所有测试！")
