from app import run


def test_app():
    csv_path = ""

    assert run(csv_path=csv_path) is None
