a = int(input())
b = int(input())
c = int(input())

triangle_lines = [a, b, c]
triangle_lines.sort()

if triangle_lines[0] > 0 \
        and triangle_lines[1] + triangle_lines[0] > triangle_lines[2]:
    print("true")
else:
    print("false")