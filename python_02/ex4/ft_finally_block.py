class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def water_plant(plant_name: str) -> None:
    print("Opening watering system")
    temp = str.capitalize(plant_name)
    try:
        if plant_name != temp:
            raise PlantError(f"Invalid plant name to water: '{plant_name}'")
        print(f"Watering {plant_name} [OK]")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        raise PlantError(e)


def test_watering_system() -> None:
    print("\nTesting valid plants...")
    plants = ["Rose", "Lilly", "Tulip", "Sunflower"]
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError:
        return
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    bad_plants = ["Rose", "lilly", "Tulip", "Sunflower"]
    try:
        for plant in bad_plants:
            water_plant(plant)
    except PlantError:
        return
    finally:
        print("Closing watering system")
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
