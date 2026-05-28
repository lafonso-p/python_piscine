def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    temp = [
        '25', 'abc'
    ]
    print("=== Garden Temperature ===")
    for t in temp:
        print(f"\nInput data is: '{t}'")
        try:
            input_temperature(t)
            print(f"Temperature is now {t}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
