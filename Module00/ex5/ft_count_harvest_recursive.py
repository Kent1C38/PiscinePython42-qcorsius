def __count(days: int, current: int) -> None:
    print(f"Day {current}")
    if current == days:
        print("Harvest time!")
    else:
        __count(days, current + 1)


def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))
    __count(days, 1)
