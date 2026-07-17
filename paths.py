from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"


def data_path(filename):
    return DATA_DIR / filename
