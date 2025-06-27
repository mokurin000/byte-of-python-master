# basic prerequisite:
#  - slicing
#  - for...in on lists using index

# cleaner code:
#  - sum()
#  - map()
#  - Compression

# 输入：非负整数，表示需要杨辉三角的前多少行。

# 输出：格式任意，
# 但是同一行的多个数字之间，应该用空格等隔开，
# 不要连在一起输出。

# 示例输入
# 4
# 示例输出
"""
    0 1 0
   0 1 1 0
  0 1 2 1 0
 0 1 3 3 1 0
0 1 4 6 4 1 0
"""

# 容易观察到，每个数都可以看作上一列临近位置两个数之和。
# 对于边界，可以看作有两个 0 在前后

# 提示1：
# [0] + [1, 2, 1] + [0] == [0, 1, 2, 1, 0]
# 提示2：
# 遍历时，考虑滑动两个两个访问，注意end确保不会超出数组边界。
# 提示3：
# 可以考虑在列表中存储列表。

n: int = int(input("请输入想要的杨辉三角行数："))

# type annotation/类型标注 不影响实际的数据类型，只作为一个参考
pascal_triangles: list[list[int]] = [[1,], ]

for _ in range(n-1):
    last_line: list[int] = [0] + pascal_triangles[-1] + [0] # -1 下标可以访问出目前的最后一行
    new_line: list[int] = []
    for i in range(len(last_line) - 1):
        new_num: int = last_line[i] + last_line[i+1] # 取两个邻近的数字之和
        new_line.append(new_num)
    pascal_triangles.append(new_line)

for line in pascal_triangles:
    print(*line)