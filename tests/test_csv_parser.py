from app.parser import CSVParser

CSV_PATH = ""


def test_csv_parser():
    csv_parser = CSVParser(path=CSV_PATH)

    assert csv_parser.parse() is None
