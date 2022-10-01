import requests
import json
from dataclasses import dataclass

fakeua = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}


@dataclass
class LocationResult():
    id: int
    name: str
    container: str
    containerId: int
    timezone: str
    country: str
    latitude: float
    longitude: float


def get_locations(query):
    url = "https://locator-service.api.bbci.co.uk/locations?api_key=AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv&stack=aws&locale=en&filter=international&place-types=settlement%2Cairport%2Cdistrict&order=importance&a=true&format=json"

    r = requests.get(url, params={"s": query}, headers=fakeua)

    if r.status_code != 200:
        return "Invalid status code", None

    data = r.json()

    try:
        results = data["response"]["results"]["results"]

    except:
        return "Invalid JSON", None

    output = []

    for location in results:
        output.append(LocationResult(id=location["id"], name=location["name"], container=location["container"],
                                     containerId=location["containerId"],
                                     timezone=location["timezone"], country=location["country"],
                                     latitude=location["latitude"], longitude=location["longitude"]))

    return False, output


@dataclass
class WeatherSample():
    temp: float
    windSpeed: float
    maxGustSpeed: float


def get_weather(locationID):
    url = f"https://weather-broker-cdn.api.bbci.co.uk/en/maps/forecasts-observations?locations={str(locationID)}"

    r = requests.get(url, headers=fakeua)

    if r.status_code != 200:
        return "Invalid status code", None

    data = r.json()

    try:
        print(str(data["features"][0]["properties"]["observations"][0]))
        forecast = data["features"][0]["properties"]["observations"][0]
    except:
        return "Invalid JSON", None

    tempC = forecast.get("temperature")
    if tempC:
        tempC = tempC.get("c")
    else:
        tempK = None

    if tempC:
        tempK = tempC - 273
    else:
        tempK = None

    averageWindSpeed = forecast.get("averageWindSpeed")

    if averageWindSpeed:
        averageWindSpeed = averageWindSpeed.get("kph")
        if not averageWindSpeed:
            averageWindSpeed = None

    maxWindGustSpeed = forecast.get("averageWindSpeed")
    if maxWindGustSpeed:
        maxWindGustSpeed = maxWindGustSpeed.get("kph")

        if not maxWindGustSpeed:
            maxWindGustSpeed = None

    return WeatherSample(tempK, averageWindSpeed, maxWindGustSpeed)


if __name__ == "__main__":
    error, locList = get_locations("te")
    print(str(locList))

    for i in locList:
        print(str(get_weather(i.id)))