import sys
from typing import TextIO


def ft_open_file() -> TextIO | None:
    try:
        file = open(sys.argv[1], "r")
        return file
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    file = ft_open_file()
    if file:
        print(f"Accessing file '{sys.argv[1]}'")
        content = file.read()
        print(f"---\n\n{content}\n---")
        file.close()
        print(f"File '{sys.argv[1]}' closed.")
    return


if __name__ == "__main__":
    main()
