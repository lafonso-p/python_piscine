class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = max(0, height)
        self.age = max(0, age)

    def get_height(self) -> int:
        return self.height

    def set_height(self, h: int) -> None:
        if (h < 0):
            print(f"Invalid operation attempted: height {h}cm [REJECTED]")
            print("Security: Negative height rejected\n")
            return
        print(f"Height updated: {h}cm [OK]")
        self.height = h

    def get_age(self) -> int:
        return self.age

    def set_age(self, age: int) -> None:
        if (age < 0):
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")
            return
        if (age > 1):
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Age updated: {age} day [OK]")
        self.age = age

    def grow(self, cm) -> None:
        self.height += cm

    def age_up(self, days) -> None:
        self.age += days

    def get_info(self) -> str:
        return f"{self.name} {self.height}cm, {self.age} days"


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> str:
        self.is_blooming = True
        return f"{self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, points) -> None:
        super().__init__(name, height, age, color)
        self.points = points

    def get_prize_points(self) -> str:
        return f"Prize points : {self.points}"

    def get_info(self) -> str:
        base = super().get_info()
        bloom = self.bloom()
        points = self.get_prize_points()
        return f"{base}, {bloom}, {points}"


class GardenManager:

    gardens: list["GardenManager"] = []

    class GardenStats:

        def __init__(self) -> None:
            self.plants_count = 0
            self.total_growth = 0
            self.type_count = {
                "regular": 0,
                "flowering": 0,
                "prize": 0
            }

        def register(self, plant: Plant) -> None:
            self.plants_count += 1
            if isinstance(plant, PrizeFlower):
                self.type_count["prize"] += 1
            elif isinstance(plant, FloweringPlant):
                self.type_count["flowering"] += 1
            else:
                self.type_count["regular"] += 1

        def register_growth(self, growth) -> None:
            self.total_growth += growth

        def garden_sumary(self) -> str:
            counts = self.type_count
            return (
                f"\nPlants added: {self.plants_count}, "
                f"Total growth: {self.total_growth}cm\n"
                f"Plant types: {counts['regular']} regular, "
                f"{counts['flowering']} flowering, "
                f"{counts['prize']} prize flowers"
            )

    def __init__(self, owner) -> None:
        self.owner = owner
        self.plants: list[Plant] = []
        self.stats = GardenManager.GardenStats()
        GardenManager.gardens.append(self)

    def add_plant(self, plant: Plant) -> None:
        if not GardenManager.validate_height(plant.get_height()):
            print(f"Cannot add {plant.name}: invalid height")
        self.plants.append(plant)
        self.stats.register(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        if not self.plants:
            return
        print(f"{self.owner} is helping all plants grow...")
        growth = 0
        for plant in self.plants:
            plant.grow(1)
            plant.age_up(1)
            growth += 1
            print(f"{plant.name} grew 1cm")
        self.stats.register_growth(growth)

    def report(self) -> None:
        print(f"\n=== {self.owner}'s garden report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.get_info()}")
            elif isinstance(plant, FloweringPlant):
                bloom = plant.bloom()
                print(f"- {plant.name}: {plant.get_height()}CM {bloom}")
            else:
                print(f"- {plant.name}: {plant.get_height()}cm")
        print(self.stats.garden_sumary())

    @classmethod
    def create_garden_network(cls, names) -> list["GardenManager"]:
        return [cls(name) for name in names]

    @classmethod
    def garden_scores(cls) -> dict[str, int]:
        scores: dict[str, int] = {}
        for garden in cls.gardens:
            height_total = sum(plant.get_height() for plant in garden.plants)
            scores[garden.owner] = (
                height_total + garden.stats.plants_count * 7
                + garden.stats.total_growth * 5
            )
        return scores

    @staticmethod
    def validate_height(value) -> bool:
        return value >= 0


def main():
    print("\n=== Garden Management System Demo ===")
    alice, bob = GardenManager.create_garden_network(["Alice", "Bob"])

    oak = Plant("Oak Tree", 100, 365)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 45, "yellow", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    bob.add_plant(Plant("Sprout", 10, 5))

    alice.grow_all()
    bob.grow_all()

    alice.report()
    bob.report()

    print(f"Height validation test: {GardenManager.validate_height(30)}")
    scores = GardenManager.garden_scores()
    pairs = ", ".join(f"{owner}: {score}" for owner, score in scores.items())
    print(f"\nGarden scores - {pairs}")
    print(f"Total gardens managed: {len(GardenManager.gardens)}\n")


if __name__ == "__main__":
    main()
