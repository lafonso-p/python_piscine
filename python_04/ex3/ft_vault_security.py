def secure_archive(
        file_name: str,
        mode: str,
        content: str) -> tuple[bool, str]:
    try:
        if mode == "read":
            with open(file_name, "r") as file:
                data = file.read()
            return [True, data]
        elif mode == "write":
            with open(file_name, "w") as file:
                file.write(content)
            return [True, "Content written successfully."]
        else:
            return [False, "Invalid mode. Use 'read' or 'write'."]
    except Exception as e:
        return [False, str(e)]


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    file_name = "nonexistent_file.txt"
    success, message = secure_archive(file_name, "read", "")
    print(f"{success}, {message}\n")

    print("Using 'secure_archive' to read from an inaccessible file:")
    file_name = "master_passwd.txt"
    success, message = secure_archive(file_name, "read", "")
    print(f"{success}, {message}\n")

    print("Using 'secure_archive' to read from a regular file:")
    file_name = "ancient_file.txt"
    success, message = secure_archive(file_name, "read", "")
    print(f"{success}, {message}\n")

    print("Using 'secure_archive' to write previous content to a new file:")
    if success:
        new_file_name = "new_ancient_file.txt"
        success, message = secure_archive(new_file_name, "write", message)
        print(f"({success}, {message})\n")


if __name__ == "__main__":
    main()
