from typing import List
import requests
from PIL import Image
from io import BytesIO, StringIO
import math


def fetch_images():
    names = ["0131", "0094", "0335", "0211", "0193",
             "0171", "0304", "1600", "4500", "1700", "HMIIF"]
    print(names)
    for name in names:
        print(
            f"https://sdo.gsfc.nasa.gov/assets/img/latest/latest_4096_{name}.jpg")
        res = requests.get(
            f"https://sdo.gsfc.nasa.gov/assets/img/latest/latest_4096_{name}.jpg")
        image = Image.open(BytesIO(res.content))
        image.save(f"{name}.png")


def deg_to_rad(angle):
    return angle * (math.pi / 180)


def lat_long_to_xy(lat, long):
    theta = (long + 360) % 360
    phi = (lat + 90)
    x = math.sin(deg_to_rad(phi)) * math.sin(deg_to_rad(theta))
    y = math.cos(deg_to_rad(phi))
    return x, y


def get_pixel(image, lat, long):
    x, y = lat_long_to_xy(lat, long)
    x = (x * (image.width / 2)) + (image.width / 2)
    y = (y * (image.width / 2)) + (image.width / 2)
    return image.getpixel((x, y))


if __name__ == "__main__":
    # fetch_images()
    print(get_pixel(
        Image.open("1600.png").crop((
            458,
            458,
            3640,
            3640
        )),
        90,
        90
    ))
