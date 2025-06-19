pascal_triangles = [[1]]

n = int(input())

for _ in range(n - 1):
    last_line = [0] + pascal_triangles[-1] + [0]
    new_line = [sum(last_line[i : i + 2]) for i in range(len(last_line) - 1)]
    pascal_triangles.append(new_line)

print(
    *map(
        lambda nums: (n - len(nums)) * " " + " ".join(map(str, nums)),
        pascal_triangles,
    ),
    sep="\n",
)
