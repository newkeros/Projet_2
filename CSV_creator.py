# File for creating csv file
import csv
from pathlib import Path


def create_csv(product):
    path = Path(".") / "Data" / product["category"]
    path.mkdir(parents=True, exist_ok=True)
    filepath = path / (product["category"] + ".csv")

    with filepath.open("a", newline="", encoding="utf-8") as f:
        csv_writer = csv.DictWriter(f, fieldnames=product.keys(), delimiter=",")
        if filepath.stat().st_size == 0:
            csv_writer.writeheader()
        csv_writer.writerow(product)
