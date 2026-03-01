def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not plant:
                raise TypeError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except TypeError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()

    try:
        print("Testing normal watering...")
        plant_list: list = ["Tomato", "lettuce", "carrots"]
        water_plants(plant_list)
        print("Watering completed successfully!\n")

        print("Testing with error...")
        plant_list_with_errors: list = ["tomato", None, "carrots"]
        water_plants(plant_list_with_errors)
    except Exception as e:
        print(e)
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    try:
        test_watering_system()
    except Exception as e:
        print(f"caught error{e}")
