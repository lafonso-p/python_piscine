class plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = max(0, height)
        self.age = max(0, age)

    def set_height(self, h: int):
        if (h < 0):
            print(f"Invalid operation attempted: height {h}cm [REJECTED]")
            print("Security: Negative height rejected\n")
            return
        print(f"Height updated: {h}cm [OK]")
        self.height = h

    def set_age(self, age: int):
        if (age < 0):
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")
            return
        if (age > 1):
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Age updated: {age} day [OK]")
        self.age = age

    def get_info(self):
        return f"{self.name} {self.height}cm, {self.age} days"


class Flower(plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        return f"{self.name} is blooming beaultifully!"


class Tree(plant):
    def __init__(self, name, height, age, diameter):
        super().__init__(name, height, age)
        self.diameter = diameter

    def produce_shade(self):
        shade = self.diameter * 1.56
        return f"{self.name} provides {shade: .0f} square meters of shade"


class Vegetable(plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutrution = nutritional_value

    def display_nutrition(self):
        return f"{self.name} is rich in {self.nutrution}"


def main():
    print("=== Garden Plant Types===\n")
    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Lily", 90, 130, "white")
    ]
    for flower in flowers:
        print(
            f"{flower.name} (Flower): {flower.get_info()}, "
            f"{flower.color} color\n"
            f"{flower.bloom()}\n"
        )

    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Sequoia", 830, 839500, 1100)
    ]
    for tree in trees:
        print(
            f"{tree.name} (Tree): {tree.get_info()}, "
            f"{tree.diameter}cm diameter\n"
            f"{tree.produce_shade()}\n"
        )

    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin c"),
        Vegetable("Potato", 12, 120, "autumn", "carbohydrates")
    ]
    for vegetable in vegetables:
        print(
            f"{vegetable.name} (Vegetable): {vegetable.get_info()}, "
            f"{vegetable.harvest_season} harvest\n"
            f"{vegetable.display_nutrition()}\n"
        )


if __name__ == "__main__":
    main()
