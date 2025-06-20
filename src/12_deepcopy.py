# 多层复制需要用 deepcopy

from copy import deepcopy

a = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
print(a)

# [:] 只能进行目前操作的列表的复制，但是不会把其中的可变对象一同复制

b = a[:]
b[0][0] = 5

print(a)

c = deepcopy(a)
c[0][1] = 10

print(c)
print(a)