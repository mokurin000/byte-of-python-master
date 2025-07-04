def normalize_names(names: list[str]) -> list[str]:
    new_list = []
    for name in names:
        new_list.append(name.title())
    return new_list


if __name__ == "__main__":
    assert normalize_names(['']) == [''], "should return empty string"
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
