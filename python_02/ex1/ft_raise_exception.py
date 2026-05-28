def input_temperature(temp_str: str) -> int:
    nbr = int(temp_str)
    if nbr < 0:
        raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C)")
    elif nbr > 40:
        raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C)")
    return nbr


def test_temperature() -> None:
    temp = [
        '25', 'abc', '100', '-50'
    ]
    print("=== Garden Temperature Checker ===")
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
