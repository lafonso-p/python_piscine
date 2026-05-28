def ft_count_harvest_recursive():
    day = int(input('Days until harvest: '))
    if day != 0:
        aux_recursive(day)
    print("Harvest time!")


def aux_recursive(day):
    if day == 1:
        print("Day ", day)
    else:
        aux_recursive(day - 1)
        print("Day ", day)
