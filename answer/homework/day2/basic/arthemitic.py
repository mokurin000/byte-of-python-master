# note: type annotations (var: type = ...) here will do nothing to the logic,
# but for the readability of your code.
a: int = int(input())
b: int = int(input())
operator: str = input()

if operator == "add":
    print(a+b)
elif operator == "subtract":
    print(a-b)
elif operator == "multiply":
    print(a*b)
elif operator == "divide":
    print(a/b)