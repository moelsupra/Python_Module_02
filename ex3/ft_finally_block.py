def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not plant:
                raise TypeError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except TypeError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    plant_l: list = ["Tomato", "lettuce", "carrots"]
    water_plants(plant_l)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    plant_l: list = ["tomato", None, "carrots"]
    water_plants(plant_l)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
