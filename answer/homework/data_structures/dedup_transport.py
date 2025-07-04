# 需要: list, for .. in, 一点变量定义

# 你正在和朋友聊天，但是对方喝水突然喷到键盘上，
# 按键开始出现意外的连续
# 你可以假设原始字符并不本身需要重读，每个字符都需要与上个不同才不算多余的重复。
# 读入一句话，，输出处理的结果。
# 大小写不敏感处理

# 输入：
# Bro myyyyy    keyyybbboard iiiis brokkkkkkkkeen
# 输出：
# Bro my keyboard is broken

s = input()

assert len(s) > 0

last_character = s[0]
result = last_character

for character in s:
    if character != last_character:
        last_character = character
        result += last_character

print(result)

