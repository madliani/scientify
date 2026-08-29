from os import environ

from dotenv import load_dotenv

from parser import CSVParser

load_dotenv()

csv_path = environ["CSV_PATH"]
csv_parser = CSVParser(path=csv_path)

if __name__ == "__main__":
    csv_parser.parse()
