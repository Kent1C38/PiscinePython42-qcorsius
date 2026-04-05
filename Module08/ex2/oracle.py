import os

if __name__ == "__main__":

    print("ORACLE STATUS: Reading the Matrix...")
    try:
        from dotenv import load_dotenv
    except Exception:
        print("Missing dependency: 'dotenv'\nPlease install it by running"
              " the following command: pip install python-dotenv")
        exit(1)

    load_dotenv()

    def get_env(key: str) -> str:
        value = os.getenv(key)
        if value is None:
            return f"[WARN] {key} key not set in environment!"
        else:
            return value
    print("Configuration loaded...")
    print(f"Mode: {get_env('MATRIX_MODE')}")
    print(f"Database: {get_env('DATABASE_URL')}")
    print(f"API Access: {get_env('API_KEY')}")
    print(f"Log Level: {get_env('LOG_LEVEL')}")
    print(f"Zion Network: {get_env('ZION_ENDPOINT')}")
