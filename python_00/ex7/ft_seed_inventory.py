def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == 'packets':
        print(seed_type, ' seeds: ', quantity, 'packets available')
    elif unit == 'grams':
        print(seed_type, ' seeds: ', quantity, 'grams')
    elif unit == 'area':
        print(seed_type, ' seeds: ', quantity, 'area')
    else:
        print('Unknown unit type')
