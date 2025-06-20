arr = [1, 1, 1, 2]

print(2 in arr) # True
print(3 in arr) # False

arr.remove(1)
print(arr) # [1, 1, 2]

while 1 in arr:
    arr.remove(1)

# arr = [2]
print(arr)