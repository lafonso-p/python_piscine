class plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main():
    plant1 = plant('Rose', 25, 30)
    plant2 = plant('Sunflower', 80, 45)
    plant3 = plant('Cactus', 15, 120)
    garden = [plant1, plant2, plant3]
    print("=== Garden Plant Registry ===")
    for i in range(len(garden)):
        print(garden[i].get_info())


if __name__ == "__main__":
    main()
