def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))

    def count(current: int) -> None:
        print(f"Day {current}")
        if current == days:
            print("Harvest time!")
        else:
            count(current + 1)

    count(1)
