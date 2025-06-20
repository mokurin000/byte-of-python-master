# s = {1, 2} # 创建有自带数字的集合


s = set()  # {} 会被认为是字典，空集合需要用 set() 创建

# 集合可以用于去重元素，同样是基于散列（能作为 dict key 的类型都可以加入集合。）

s.add(1)
s.add("Hello")

print(s)
s.remove(1)
print(s)

print(s.pop()) # pop 随机取出集合中的一个元素

print("Hello" in s)

another_s = s.copy() # 复制对象后成为独立的两个集合
another_s.add(1)
print(s)