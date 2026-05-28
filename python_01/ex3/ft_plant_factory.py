class plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.name} ({self.height}cm, {self.age} days)"


def main():
    plants = [
        ('Rose', 25, 30), ('Oak', 200, 365), ('Cactus', 5, 90),
        ('Sunflower', 80, 45), ('Fern', 15, 120)

    ]
    garden = []
    for i in range(len(plants)):
        name = plants[i][0]
        height = plants[i][1]
        age = plants[i][2]
        garden.append(plant(name, height, age))
    print("=== Plant Factory Output ===")
    for i in range(len(garden)):
        print(f"Created: {garden[i].get_info()}")
    print(f"\nTotal plants created: {i + 1}")


if __name__ == "__main__":
    main()
