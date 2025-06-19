# 非零的数字都认为是 True
print(bool(1.0)) # True
print(bool(-10)) # True
print(bool(0.0)) # False

# 非空的字符串认为是 True
print(bool("False")) # True
print(bool("")) # False

# 布尔值本身被 bool() 转换无任何影响
bool(True) # True