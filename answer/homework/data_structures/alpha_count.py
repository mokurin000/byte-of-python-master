s = input().lower()
d = {}

for ch in s:
    if not ch.isalpha():
        continue
    d[ch] = d.get(ch, 0) + 1

for alpha, times in d.items():
    if times >= 2:
        print(f"{alpha}: {times}")
