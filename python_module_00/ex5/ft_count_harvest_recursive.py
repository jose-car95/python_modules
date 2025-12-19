n = int(input("Days until harvest: "))


def ft_count_harvest_recursive(actual=0):
    if actual > n:
        return
    print(f"Day {actual}")
    ft_count_harvest_recursive(actual + 1)
