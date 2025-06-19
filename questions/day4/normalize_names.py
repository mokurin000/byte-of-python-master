# Imagine we have numerous ill-formed names in a list
# >>> names = ["CeCiLIa", "lINUs", "HoWArd"]
# And we want convert the list into:
# ["Cecilia", "Linus", "Howard"]

# Implement a function that accepts a `list[str]` and returns the same type
# Your input might be empty list.


def normalize_names(names: list[str]) -> list[str]:
    pass


if __name__ == "__main__":
    assert normalize_names(
        [
            "CeCiLIa",
            "lINUs",
            "HoWArd",
        ]
    ) == [
        "Cecilia",
        "Linus",
        "Howard",
    ], "incorrect implementation!"
