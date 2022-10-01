from flask import Flask, send_from_directory
import flask_caching
import flask_cors
from waitress import serve
from solarwind import get_windspeed

app = Flask(__name__)


@app.route("/<path:path>")
def serve_svelte(path):
    return send_from_directory("svelteapp", path)


@app.route("/api/solarwind")
def solarwind():
    try:
        err, data = get_windspeed()
    except:
        return "Unexpected error"

    if err:
        return {"error": True, "message": err}
    return {"error": False, "data": str(data)}


if __name__ == "__main__":
    dev = True

    if dev:
        app.run(host="0.0.0.0", port=8080, debug=True)

    else:
        serve(app, host="0.0.0.0", port=8080)
