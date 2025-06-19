def normalize_names(names: list[str]) -> list[str]:
    return list(map(str.title, names))


if __name__ == "__main__":
    assert normalize_names([]) == [], "should return empty list"
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
    ], "should normalize names"
    print("passed check!")
