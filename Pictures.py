import requests
from pathlib import Path


def get_picture(product):
    response = requests.get(product["image_url"])

    path = Path(".") / "Data" / product["category"] / "Image"
    path.mkdir(parents=True, exist_ok=True)
    filepath = path / (product["product_upc"] + ".jpg")

    with filepath.open("wb") as file:
        file.write(response.content)
