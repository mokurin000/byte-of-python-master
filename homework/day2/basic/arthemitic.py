"""
Given two numbers and an arithmetic operator (the name of it, as a string),
return the result of the two numbers having that operator used on them.

a and b will both be positive integers, and a will always be the first number
in the operation, and b always the second.

The four operators are "add", "subtract", "divide", "multiply".

A few examples:(Input1, Input2, Input3 --> Output)

5, 2, "add"      --> 7
5, 2, "subtract" --> 3
5, 2, "multiply" --> 10
5, 2, "divide"   --> 2.5

给出两个数字和一个运算类型名, 返回两个数进行对应运算的结果。
a 和 b 都是正整数, 且计算结果为 a 操作符 b, 对于不满足交换律的运算

输入代码已经写好, 只需考虑逻辑部分。
"""

# note: type annotations (var: type = ...) here will do nothing to the logic,
# but for the readability of your code.
a: int = int(input())
b: int = int(input())
operator: str = input()
