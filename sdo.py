from typing import List
import requests
from PIL import Image
from io import BytesIO, StringIO
import math
from cachetools import cached, LRUCache, TTLCache

BRIGHTNESS_CUTOFF = 190

names = ["0131", "0094", "0335", "0211", "0193",
         "0171", "0304", "1600", "1700", "HMIIF"]

temps = [10000000, 6000000, 2500000, 2000000, 1000000, 600000, 50000, 10000, 4500, 3000, 2000]


def fetch_images():
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


@cached(cache=TTLCache(maxsize=8192, ttl=3600))
def get_temperature(lat, long):
    last = {"temp": None, "brightness": None}
    final = {"temp": None, "brightness": None}

    for (name, temp) in zip(names, temps):
        image = Image.open(f"{name}.png").crop((
            458,
            458,
            3640,
            3640
        ))
        (r, g, b) = get_pixel(image, lat, long)
        brightness = max([r, g, b])
        if brightness >= BRIGHTNESS_CUTOFF:
            final = {"temp": temp, "brightness": brightness}
            break

        last = {"temp": temp, "brightness": brightness}

    lastWeight = last["brightness"] / (last["brightness"] + final["brightness"])
    finalWeight = final["brightness"] / (last["brightness"] + final["brightness"])

    avg = ((lastWeight * last["temp"]) + (finalWeight * final["temp"])) / (lastWeight + finalWeight)

    return avg


if __name__ == "__main__":
    # fetch_images()
    print(get_temperature(-89, 10))
