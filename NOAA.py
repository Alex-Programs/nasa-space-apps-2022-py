import requests
import time
import datetime
from cachetools import cached, LRUCache, TTLCache
import math


class SolarRegionsData():
    def __init__(self):
        print("Initialising solar regions...")
        data = self.__get_solar_regions__()
        if not data:
            print("INVALID SOLAR REGIONS DATA")
            import sys
            sys.exit()

        self.data = data
        print("Done!")

    def __get_solar_regions__(self):
        r = requests.get("https://services.swpc.noaa.gov/json/solar_regions.json")

        if r.status_code != 200:
            return False

        data = r.json()

        return data

    def get_region_data(self, lat, lon, daysbacklim):
        def filter_func(x):
            daysback = abs(
                (datetime.datetime.now() - datetime.datetime.strptime(x.get("observed_date"), "%Y-%m-%d")).days)
            return daysback <= daysbacklim and x.get("latitude") and x.get("longitude") and abs(
                lat - x["latitude"]) < 6 and abs(lon - x["longitude"]) < 6

        closeRegions = list(filter(filter_func, self.data))

        if len(closeRegions) == 0:
            return None

        else:
            # Find closest one. Simple pythagoras
            closestDist = 5 * (10 ** 10)
            closestVal = None
            for region in closeRegions:
                # Not completing pythag by sqrting because we're ordering only
                distance = (abs(lat - region["latitude"]) * abs(lat - region["latitude"])) + (
                        abs(lon - region["longitude"]) * abs(lon - region["longitude"]))

                if distance < closestDist:
                    closestDist = distance
                    closestVal = region
                    closestVal["Approximate_Distance_SpaceApps"] = distance

            return closestVal


class SunspotData():
    def __init__(self):
        print("Initialising sunspot data...")
        data = self.__get_sunspot_data__()
        if not data:
            print("INVALID SUNSPOT DATA")
            import sys
            sys.exit()

        self.data = data
        print("Done!")

    def __get_sunspot_data__(self):
        r = requests.get("https://services.swpc.noaa.gov/json/sunspot_report.json")

        if r.status_code != 200:
            return False

        data = r.json()

        return data

    def get_close_sunspots(self, lat, lon, daysbacklim):
        def filter_func(x):
            daysback = abs(
                (datetime.datetime.now() - datetime.datetime.strptime(x.get("Obsdate").split("T")[0], "%Y-%m-%d")).days)

            return daysback <= daysbacklim and x.get("Latitude") and x.get("Longitude") and abs(
                lat - x["Latitude"]) < 6 and abs(lon - x["Longitude"]) < 6

        closeRegions = list(filter(filter_func, self.data))

        if len(closeRegions) == 0:
            return None

        # Find closest one. Simple pythagoras
        closestDist = 5 * (10 ** 10)
        closestVal = None
        for region in closeRegions:
            # Not completing pythag by sqrting because we're ordering only
            distance = (abs(lat - region["Latitude"]) * abs(lat - region["Latitude"])) + (
                    abs(lon - region["Longitude"]) * abs(lon - region["Longitude"]))

            if distance < closestDist:
                closestDist = distance
                closestVal = region
                closestVal["Approximate_Distance_SpaceApps"] = distance

        return closestVal


if __name__ == "__main__":
    solarRegions = SolarRegionsData()

    print(str(solarRegions.get_region_data(-25, -68, 2)))

    sunspotData = SunspotData()

    print(str(sunspotData.get_close_sunspots(-26, -73, 2)))
