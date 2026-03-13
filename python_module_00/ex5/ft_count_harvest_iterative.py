def ft_count_harvest_iterative() -> None:
    days: int = int(input("Days until harvest: "))
    for day in range(days + 1):
        print("Day ", day)
