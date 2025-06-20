n = int(input())

fibs = [1, 1]
for _ in range(n-2):
    fibs.append(fibs[-1] + fibs[-2])

print(fibs)