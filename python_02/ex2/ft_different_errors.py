def garden_operations(operation_number: int) -> int | float | str | None:
    if operation_number == 0:
        return int("abc")

    elif operation_number == 1:
        plants = 50
        area = 0
        return (plants / area)

    elif operation_number == 2:
        file = open("/non/existent/file", mode='r', encoding=None)
        return file.read()

    elif operation_number == 3:
        str = "garden" + 5
        return str
    else:
        return None


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    numbers = {0, 1, 2, 3, 4}
    for i in numbers:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully.")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        except (ValueError, KeyError):
            print("Caught an error, but program continues!")

    print("\nAll error types tested successfully")


if __name__ == "__main__":
    test_error_types()
