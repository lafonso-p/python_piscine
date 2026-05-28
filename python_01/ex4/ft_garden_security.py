class secure_plant:
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
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main():
    print("=== Garden Security System ===")
    plant = secure_plant("Rose", 25, 30)
    print(f"Plant created: {plant.get_info()}")

    print("Setting negative height:")
    plant.set_height(-10)
    print("Setting negative age:")
    plant.set_age(-5)

    print("Setting valid height:")
    plant.set_height(30)
    print("Setting valid age:")
    plant.set_age(35)
    print(f"Plant updated: {plant.get_info()}")


if __name__ == "__main__":
    main()
