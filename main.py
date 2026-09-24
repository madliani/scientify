from os import environ

from dotenv import load_dotenv

from src import app

if __name__ == "__main__":
    load_dotenv()

    csv_path = environ["CSV_PATH"]

    app.run(csv_path=csv_path)
