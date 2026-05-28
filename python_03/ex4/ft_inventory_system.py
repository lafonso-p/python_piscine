import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = {}
    for arg in sys.argv[1:]:
        items = arg.split(":")
        if len(items) != 2:
            print(f"Error - Invalid parameter: '{arg}'")
            continue
        if items[0] in inventory:
            print(f"Redundant item '{items[0]}' - discarding")
            continue
        try:
            inventory.update({items[0]: int(items[1])})
        except ValueError as e:
            print(f"Quantity error for '{items[0]}': {e}")
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")
    for item in inventory:
        print(f"Item {item} represents {inventory[item] / total:.1%}")
    value = 0
    abundant = ""
    for item in inventory:
        if inventory[item] > value:
            value = inventory[item]
            abundant = item
    print(f"Item most abundant: {abundant} with quantity {value}")
    value = sys.maxsize
    scarce = ""
    for item in inventory:
        if inventory[item] < value:
            value = inventory[item]
            scarce = item
    print(f"Item least abundant: {scarce} with quantity {value}")
    inventory.update({"magic item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
