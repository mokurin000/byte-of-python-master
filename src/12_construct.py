nums = [1] * 10
print(nums)

lists = [[]] * 10 # 错误：这些列表全都指向同一个列表对象
lists[0].append(1)
print(lists)

lists = []
for _ in range(10):
    lists.append([]) # 正确：每次重新创建空列表 []
lists[0].append(1)
print(lists)
