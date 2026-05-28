import sys
import os
import site


def is_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    if is_virtual_env():
        env_path = sys.prefix
        env_name = os.path.basename(env_path)

        print(
            "\nMATRIX STATUS: Welcome to the construct\n"
            f"\nCurrent Python: {sys.executable}\n"
            f"Virtual Environment: {env_name}\n"
            f"Environment Path: {env_path}\n"
            )
        print(
            "SUCCESS: You're in an isolated enviroment!\nSafe to "
            "install packages without affecting the global system.\n"
            f"\nPackage instalation path: {site.getsitepackages()[0]}\n"
            )
    else:
        print(
            "\nMATRIX STATUS: You're still plugged in\n"
            f"Current Python: {sys.executable}\n"
            "Virtual Environment: None detected\n\n"
            "WARNING: You're in a global environment!\n"
            "The machines can see everything you install\n\n"
            "To enter construct , run: python -m venv matrix_venv\n"
            "source matrix_venv/bin/activate # On Unix\n"
            "matrix_venv\\Scripts\\activate # On Windows\n\n"
            "Then run this program again."
            )
    return


if __name__ == "__main__":
    main()
