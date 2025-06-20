# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist.pop(0) # pop() 取出对应下标的元素，同时从列表中移除
print('I bought the', olditem)
print('My shopping list is now', shoplist)

# insert 使用的index如果大于 len(shoplist) 只会等价于 append()
shoplist.insert(10, "z")
# insert 使用的index 小于等于 len(shoplist) 时，插入后该index即为新元素的下标
shoplist.insert(2, "d")

print(shoplist)
