from typing import List
import requests
from PIL import Image
from io import BytesIO, StringIO
import math

BRIGHTNESS_CUTOFF = 190

names = ["0131", "0094", "0335", "0211", "0193",
         "0171", "0304", "1600", "1700", "HMIIF"]

temps = [10000000, 6000000, 2500000, 2000000,
         1000000, 600000, 50000, 10000, 4500, 3000, 2000]


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

def rad_to_deg(angle):
    return angle * (180 / math.pi)

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


def get_temperature(lat, long):
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
            return temp


def get_distance(lat1, lat2, long1, long2):
    lat1 = deg_to_rad(lat1)
    lat2 = deg_to_rad(lat2)
    long1 = deg_to_rad(long1)
    long2 = deg_to_rad(long2)
    angle = rad_to_deg(math.acos(math.sin(lat1)*math.sin(lat2)+math.cos(lat1)*math.cos(lat2)*math.cos(long1 - long2)))/360
    return 696000 * angle

if __name__ == "__main__":
    # fetch_images()
    print(get_temperature(-89, 10))
    print(get_distance(0, 0, 62, 90))
