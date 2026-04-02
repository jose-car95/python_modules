def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))

    def recursive(day: int) -> None:
        if day != 1:
            recursive(day - 1)
        print("Day ", day)
    recursive(days)
    print("Harvest time!")
