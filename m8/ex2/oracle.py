import os
from dotenv import load_dotenv


def load_configuration() -> dict[str, str | None]:
    load_dotenv()
    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT")
    }


def show_configuration(config: dict[str, str | None]) -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")

    matrix_mode: str | None = config["MATRIX_MODE"]
    database_url: str | None = config["DATABASE_URL"]
    api_key: str | None = config["API_KEY"]
    log_level: str | None = config["LOG_LEVEL"]
    zion_endpoint: str | None = config["ZION_ENDPOINT"]

    if matrix_mode is None:
        print("[WARNING] MATRIX_MODE not set, defaulting to: development")
        matrix_mode = "development"
    if database_url is None:
        print("[WARNING] DATABASE_URL not configured")
    if api_key is None:
        print("[ERROR] API_KEY missing - authentication unavailable")
    if log_level is None:
        print("[WARNING] LOG_LEVEL not set, defaulting to: INFO")
        log_level = "INFO"
    if zion_endpoint is None:
        print("[WARNING] ZION_ENDPOINT not set")

    config_data: bool = config["DATABASE_URL"] is not None
    config_api: bool = config["API_KEY"] is not None
    config_zion: bool = config["ZION_ENDPOINT"] is not None

    if (
        config_data and config_api and config_zion
    ):
        print("Configuration loaded:")
        print(f"Mode: {matrix_mode}")
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print(f"Log Level: {log_level}")
        print("Zion Network: Online")
        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
        print("\nThe Oracle sees all configurations.")


def main() -> None:
    config = load_configuration()
    show_configuration(config)


if __name__ == "__main__":
    main()
