# Imagine we have numerous ill-formed names in a list
# >>> names = ["CeCiLIa", "lINUs", "HoWArd"]
# And we want convert the list into:
# ["Cecilia", "Linus", "Howard"]

names = ["CeCiLIa", "lINUs", "HoWArd"]
cleaned_names = []

for name in names:
    cleaned_names.append(name.title())

print(cleaned_names)