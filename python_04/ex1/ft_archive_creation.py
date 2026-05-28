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
        print("Usage: python ft_archive_creation.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation===")
    file = ft_open_file()
    if file:
        print(f"Accessing file '{sys.argv[1]}'")
        content = file.read()
        print(f"---\n\n{content}\n---")
        file.close()
        print(f"File '{sys.argv[1]}' closed.")

    print("\nTransform data:")
    old_file = ft_open_file()
    old_content = old_file.read().split("\n")
    new_content = ""
    for line in old_content:
        if line:
            new_content += line + "#\n"
    print(f"---\n\n{new_content}\n---")

    new_file_name = input("Enter new file name (or empty): ")
    if new_file_name:
        print(f"Saving data in file '{new_file_name}'")
        new_file = open(new_file_name, "w")
        new_file.write(new_content)
        new_file.close()
        print(f"Data saved in file '{new_file_name}'")
    else:
        print("Not saving data.")
    return


if __name__ == "__main__":
    main()
