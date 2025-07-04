"""
Description

Given a number n, you should find a set of numbers for which the sum equals n.
This set must consist exclusively of values that are a power of 2
(eg: 2^0 => 1, 2^1 => 2, 2^2 => 4, ...).
For example, 15 = 8 + 4 + 2 + 1,
We don't know array yet, so we just output each power of 2:

input:
```text
15
```

output:
```text
8
4
2
1
```

给出一个数字 n ，你需要找出一系列2的幂，其和是n，其中不得重复。
如 15 = 8 + 4 + 2 + 1 （1 是 2 的 0次幂）

输入
15
输出
8
4
2
1

"""

num = int(input())
