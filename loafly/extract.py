import csv
from .config import RAW_FILE


def extract_orders():

    with open(RAW_FILE, "r") as file:
        data = list(csv.DictReader(file))

    return data