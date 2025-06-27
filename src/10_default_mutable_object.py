def foo(nums: list[int] = [1, 2, 3]): # nums 默认参数始终是同一个列表对象。
    for i in range(len(nums)):
        nums[i] *= 2
    return nums

print(foo([1,1,1])) # [2,2,2]
print(foo()) # [2, 4, 6]
print(foo()) # [4, 8, 12]


# 解决方法1
def foo1(nums: list[int] = None): # nums 默认参数始终是同一个列表对象。
    if nums is None:
        nums = [1,2,3]
    for i in range(len(nums)):
        nums[i] *= 2
    return nums

# 解决方法2
def foo2(nums: list[int] = [1,2,3]): # nums 默认参数始终是同一个列表对象。
    nums = nums.copy() # 会引入不必要的内存复制开销
    for i in range(len(nums)):
        nums[i] *= 2
    return nums