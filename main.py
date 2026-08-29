from os import environ

from dotenv import load_dotenv

from app import run

if __name__ == "__main__":
    load_dotenv()

    csv_path = environ["CSV_PATH"]

    run(csv_path=csv_path)
