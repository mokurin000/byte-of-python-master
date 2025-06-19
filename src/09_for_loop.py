# 0
# 1
# 2
for i in range(3):
    print(i)

print()

# 1
# 2
for i in range(1, 3):
    print(i)

print()

# 1
# 3
# 5
for i in range(1, 7 + 1, 2): # stop 并不会被包含在 range(start, stop) 循环内
    print(i)