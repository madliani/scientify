from app.parser import CSVParser


def run(csv_path: str):
    csv_parser = CSVParser(path=csv_path)

    csv_parser.parse()
