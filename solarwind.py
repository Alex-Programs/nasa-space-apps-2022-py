import requests
import json


def get_windspeed():
    r = requests.get("https://services.swpc.noaa.gov/products/summary/solar-wind-speed.json")

    if r.status_code != 200:
        return "NOT 200", False

    if r.json().get("WindSpeed"):
        return False, r.json()["WindSpeed"]

    else:
        return "Invalid JSON", False


if __name__ == "__main__":
    print(str(get_windspeed()))
