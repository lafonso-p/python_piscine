class plant:
    def __init__(self, name, height, age_days):
        self.name = name
        self.height = height
        self.age_days = age_days

    def growth(self):
        self.height += (self.height / self.age_days)

    def age(self):
        self.age_days += 1

    def get_info(self):
        return f"{self.name}: {self.height: .2f}cm, {self.age_days} days old"


def simulate_week(garden):
    print("=== Day 1 ===")
    for i in range(len(garden)):
        print(garden[i].get_info())

    initial_heights = [plant.height for plant in garden]

    for day in range(7):
        for plant in garden:
            plant.growth()
            plant.age()

        if day == 6:
            print("\n=== Day 7 ===")
            for plant in garden:
                print(plant.get_info())

    print("\nGrowth this week:")
    for i in range(len(garden)):
        growth = garden[i].height - initial_heights[i]
        print(f"{garden[i].name}: +{growth: .2f}cm")


def main():
    plant1 = plant('Rose', 25, 30)
    plant2 = plant('Sunflower', 80, 45)
    plant3 = plant('Cactus', 15, 120)
    garden = [plant1, plant2, plant3]
    simulate_week(garden)


if __name__ == "__main__":
    main()
