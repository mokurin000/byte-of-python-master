x = 50



def func(x): # 此处定义的 x 是函数参数
    print('x is', x)
    x = 2 # 此处将 5L 定义的 x 赋值为 2
    print('Changed local x to', x)


func(x) # 把1L定义的”全局“ x 传入 func
print('x is still', x) # 全局 x 仍然是 50