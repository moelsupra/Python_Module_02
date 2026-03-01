class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants: list = []

    def add_plant(self, plant_name: str) -> None:
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        self.plants += [plant_name]
        print(f"Added {plant_name} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        except Exception as e:
            print(f"Error watering plant: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, plant_name: str,
                     water_level: int,
                     sunlight_hours: int) -> None:
        if water_level > 10:
            raise WaterError(
                f"Water level {water_level} is too high (max 10)"
            )
        if water_level < 1:
            raise WaterError(
                f"Water level {water_level} is too low (min 1)"
            )
        if sunlight_hours < 2:
            raise PlantError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        if sunlight_hours > 12:
            raise PlantError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )
        print(f"{plant_name}: healthy "
              f"(water: {water_level}, sun: {sunlight_hours})")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    print()

    manager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
        manager.add_plant("")
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")

    try:
        manager.check_health("tomato", 5, 8)
    except GardenError as e:
        print(f"Error checking tomato: {e}")

    try:
        manager.check_health("lettuce", 15, 8)
    except GardenError as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    try:
        test_garden_management()
    except Exception as e:
        print(e)
