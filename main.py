from flask import Flask, send_from_directory, request, send_file
from flask_caching import Cache
from waitress import serve
from solarwind import get_windspeed
import json
import definitelymetoffice

app = Flask(__name__)

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
cache.init_app(app)


@app.route("/<path:path>")
def serve_svelte(path):
    return send_from_directory("frontend/public", path)


@app.route("/")
def serve_index():
    return send_file("frontend/public/index.html")


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
@cache.cached(timeout=3000)
def get_locations():
    query = request.args.get("query")

    error, data = definitelymetoffice.get_locations(query)
    if error:
        return {"error": True, "message": error}

    return data


@app.route("/api/get_weather")
@cache.cached(timeout=30)
def get_weather():
    error, data = definitelymetoffice.get_weather(request.args.get("id"))
    if error:
        return {"error": True, "message": error}

    return {"error": False, "data": {"temp": data.temp, "windSpeed": data.windSpeed, "gustSpeed": data.maxGustSpeed}}


if __name__ == "__main__":
    dev = True

    if dev:
        app.run(host="0.0.0.0", port=8080, debug=True)

    else:
        serve(app, host="0.0.0.0", port=8080)
