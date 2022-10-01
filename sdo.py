from typing import List
import requests
from PIL import Image
from io import BytesIO, StringIO

def fetch_images():
    names = ["0131", "0094", "0335", "0211", "0193", "0171", "0304", "1600", "4500", "1700", "HMIIF"]
    print(names)
    for name in names:
        print(f"https://sdo.gsfc.nasa.gov/assets/img/latest/latest_4096_{name}.jpg")
        res = requests.get(f"https://sdo.gsfc.nasa.gov/assets/img/latest/latest_4096_{name}.jpg")
        image = Image.open(BytesIO(res.content))
        image.save(f"{name}.png")

if __name__ == "__main__":
    fetch_images()