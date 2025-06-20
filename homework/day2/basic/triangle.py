"""
分别输入三角形三条边，判断是否能构成三角形
最短的两条边，边长之和大于第三边

提示：列表的 .sort()
提示：[a, b, c] 构造列表

```text
Input -> Output
1,2,2 -> true
4,2,3 -> true
2,2,2 -> true
1,2,3 -> false
-5,1,3 -> false
0,2,3 -> false
1,2,9 -> false 
```
"""

a = int(input())
b = int(input())
c = int(input())

# start your code here