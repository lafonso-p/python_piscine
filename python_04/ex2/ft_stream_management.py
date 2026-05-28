import sys
from typing import TextIO


def ft_open_file_read(file_name) -> TextIO | None:
    try:
        file = open(file_name, "r")
        return file
    except FileNotFoundError as e:
        print(f"[STDER]Error opening file '{file_name}': {e}")
    except Exception as e:
        print(f"[STDER]Error opening file '{file_name}': {e}")


def ft_open_file_write(file_name) -> TextIO | None:
    try:
        file = open(file_name, "w")
        return file
    except Exception as e:
        print(f"[STDER]Error opening file '{file_name}': {e}")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python ft_stream_management.py <file>")
        return

    file_name = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    file = ft_open_file_read(file_name)
    if not file:
        return
    print(f"Accessing file '{file_name}'")
    content = file.read()
    print(f"---\n\n{content}\n---")
    file.close()
    print(f"File '{file_name}' closed.")

    print("\nTransform data:")
    old_file = ft_open_file_read(file_name)
    if old_file:
        old_content = old_file.read().split("\n")
        new_content = ""
        for line in old_content:
            if line:
                new_content += line + "#\n"
        print(f"---\n\n{new_content}\n---")
    else:
        print("No data to transform.")

    new_file_name = sys.stdin.readline().strip("\n")
    if new_file_name:
        print(f"Saving data in file '{new_file_name}'")
        new_file = ft_open_file_write(new_file_name)
        if new_file:
            new_file.write(new_content)
            new_file.close()
            print(f"Data saved in file '{new_file_name}'")
    else:
        print("Not saving data.")
    return


if __name__ == "__main__":
    main()
