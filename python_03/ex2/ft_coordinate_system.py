import math


def get_player_pos() -> tuple[float, ...]:
    coordinates = []
    valid = False
    while not valid:
        temp = input("Enter new coordinates as floats in format 'x,y,z': ")
        array = temp.split(',')
        for i in range(len(array)):
            if len(array) != 3:
                print("Invalid syntax")
                break
            try:
                float(array[i])
                coordinates.append(round(float(array[i]), 1))
            except ValueError:
                print(f"Error on parameter '{array[i]}': could not "
                      f"convert string to float: '{array[i]}'")
                coordinates.clear()
                break
        for i in range(len(coordinates)):
            try:
                coordinates[i] = float(coordinates[i])
            except ValueError:
                print(f"Error on parameter '{coordinates[i]}': could not "
                      f"convert string to float: '{coordinates[i]}'")
                coordinates.clear()
                break
            else:
                valid = True
    return tuple(coordinates)


def main() -> None:
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    coord_1 = get_player_pos()
    print(f"Got first tuple: {coord_1}")
    print(f"It includes: x={coord_1[0]}, y={coord_1[1]}, z={coord_1[2]}")
    dist_1 = math.sqrt(coord_1[0] ** 2 + coord_1[1] ** 2 + coord_1[2] ** 2)
    print(f"Distance to center: {dist_1:.4f}")
    print("\nGet a second set of coordinates")
    coord_2 = get_player_pos()
    dist_2 = math.sqrt((coord_2[0] - coord_1[0]) ** 2 + (coord_2[1]
                       - coord_1[1]) ** 2 + (coord_2[2] - coord_1[2]) ** 2)
    print(f"Distance between the 2 sets of coordinates: {dist_2:.4f}")


if __name__ == "__main__":
    main()
