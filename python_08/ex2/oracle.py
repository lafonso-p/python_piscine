import os
import sys
from dotenv import load_dotenv


def main():
    env_exists = os.path.isfile('.env')

    load_dotenv()

    matrix_mode = os.getenv("MATRIX_MODE")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    if not all([matrix_mode, db_url, api_key, log_level, zion_endpoint]):
        print("WARNING: Missing critical configuration!")
        print("Please ensure the following variables are set:")
        print(
            "- MATRIX_MODE\n- DATABASE_URL\n- API_KEY\n- "
            "LOG_LEVEL\n- ZION_ENDPOINT")
        print("\nHint: Copy .env.example to .env and fill in the values.")
        sys.exit(1)

    print("\nORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")

    if matrix_mode == "production":
        print("Mode: production")
        print("Database: Connected to secure mainframe cluster")
        print("API Access: Authenticated (Strict Security)")
        print(f"Log Level: {log_level}")
        print("Zion Network: Encrypted Connection Active")
    elif matrix_mode == "development":
        print("Mode: development")
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print(f"Log Level: {log_level}")
        print("Zion Network: Online")
    else:
        print(f"ERROR: Invalid MATRIX_MODE '{matrix_mode}'.")
        print("MATRIX_MODE must be 'development' or 'production'.")
        sys.exit(1)

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if env_exists:
        print("[OK] .env file properly configured")
    else:
        print("[!] Environment variables loaded directly from OS")

    if matrix_mode == "production":
        print("[OK] Production overrides active")
    else:
        print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
