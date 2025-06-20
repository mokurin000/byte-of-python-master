a = [1, 2, 3]
b = a # a 和 b 现在指向同一个列表
a.append(4)
print(b) # [1, 2, 3, 4]

# 切片可以创造一层复制
c = a[:]
c.append(111)

print(a)