from flask import Flask, send_from_directory, Response, request, render_template
from flask_caching import Cache
from waitress import serve
from solarwind import get_windspeed
import json
import definitelymetoffice
import solarstatus
import NOAA
import sdo

solarRegions = NOAA.SolarRegionsData()
sunspotData = NOAA.SunspotData()

app = Flask(__name__)

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
cache.init_app(app)


@app.route("/assets/<path:path>")
def serve_assets(path):
    return send_from_directory("assets/", path)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/location")
def location():
    lat = float(request.args.get("lat"))
    lon = float(request.args.get("lon"))
    placeName = request.args.get("name")

    print(lat, lon, placeName)

    latAdjusted = lat
    lonAdjusted = lon / 2

    return render_template("location.html", lat=lat, lon=lon, latAdjusted=round(latAdjusted, 3),
                           lonAdjusted=round(lonAdjusted, 3), placeName=placeName, placeNameCaps=placeName.upper())


@app.route("/api/solarwind")
@cache.cached(timeout=30)
def solarwind():
    try:
        err, data = get_windspeed()
    except:
        return "Unexpected error"

    if err:
        return {"error": True, "message": err}
    return {"error": False, "data": str(data)}


@app.route("/api/get_locations")
def get_locations():
    query = request.args.get("query")

    error, data = definitelymetoffice.get_locations(query)
    if error:
        return {"error": True, "message": error}

    return {"error": False, "data": data}


@app.route("/api/get_weather")
def get_weather():
    error, data = definitelymetoffice.get_weather(request.args.get("id"))
    if error:
        return {"error": True, "message": error}

    return {"error": False, "data": {"temp": data.temp, "windSpeed": data.windSpeed, "gustSpeed": data.maxGustSpeed,
                                     "humidity": data.humidity, "windDescription": data.windDescription,
                                     "description": data.description}}


@app.route("/api/solarstatus/xray")
@cache.cached(timeout=360)
def solar_status_xray():
    error, data = solarstatus.get_xray_status()
    if error:
        return {"error": True, "message": error}

    return {"error": False, "data": data}


@app.route("/api/solarstatus/magneto")
@cache.cached(timeout=360)
def solar_status_magneto():
    error, data = solarstatus.get_magneto_status()
    if error:
        return {"error": True, "message": error}

    return {"error": False, "data": data}


@app.route("/api/solar_regions")
def solar_regions():
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    if not lat or not lon:
        return {"error": True, "message": "Lat/Lon not supplied"}

    lat, lon = float(lat), float(lon)

    print(lat, lon)

    data = solarRegions.get_region_data(lat, lon, 2)
    if not data:
        return {"error": True, "message": "No solar data"}

    return Response(json.dumps(data), mimetype="application/json")


@app.route("/api/sunspot_regions")
def sunspot_regions():
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    print(lat, lon)

    if not lat or not lon:
        return {"error": True, "message": "Lat/lon not supplied"}

    lat, lon = float(lat), float(lon)

    print(lat, lon)

    data = sunspotData.get_close_sunspots(lat, lon, 2)

    if not data:
        return {"error": True, "message": "No solar data"}

    return Response(json.dumps(data), mimetype="application/json")


@app.route("/api/get_temperature")
def get_temperature():
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    if not lat or not lon:
        return {"error": True, "message": "Lat/lon not supplied"}

    lat, lon = float(lat), float(lon)

    print(lat, lon)

    data = sdo.get_temperature(lat, lon)

    return {"error": False, "data": data}


if __name__ == "__main__":
    from os.path import exists as file_exists

    if not file_exists("config.json"):
        print("No config file found, writing. Default: dev=true")
        with open("config.json", "w") as f:
            f.write(json.dumps({"dev": True}))

    with open("config.json") as f:
        config = json.load(f)

    if config["dev"]:
        app.run(host="0.0.0.0", port=8080, debug=True)

    else:
        serve(app, host="0.0.0.0", port=8080, threads=8)
