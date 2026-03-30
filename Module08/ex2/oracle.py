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
    print("Configuration loaded...")
    print(f"Mode: {os.getenv('MATRIX_MODE')}")
    print(f"Database: {os.getenv('DATABASE_URL')}")
    print(f"API Access: {os.getenv('API_KEY')}")
    print(f"Log Level: {os.getenv('LOG_LEVEL')}")
    print(f"Zion Network: {os.getenv('ZION_ENDPOINT')}")
