function setEarthWeather() {
    // fetch() the weather from /api/get_weather with arg id set to the id of the location
    fetch("/api/get_weather?id=" + window.location.search.split("&")[0].split("=")[1]).then(response => response.json()).then(data => {
        // Set the weather
        if (data.error) {
            console.log(data.message)
            document.getElementById("weatherSummary").innerText = "ERROR"
            document.getElementById("earthWindSpeed").innerText = "ERROR"
            document.getElementById("earthGustSpeed").innerText = "ERROR"
            document.getElementById("earthTemp").innerText = "ERROR"
            return
        }
        console.log(data)

        data = data.data

        document.getElementById("weatherSummary").innerText = data.description
        document.getElementById("earthWindSpeed").innerText = data.windSpeed
        document.getElementById("earthGustSpeed").innerText = data.gustSpeed
        document.getElementById("earthTemp").innerText = data.temp
    });
}

setEarthWeather()

function setSolarWind() {
    // fetch() the solar wind from /api/solarwind
    fetch("/api/solarwind").then(response => response.json()).then(data => {
        // Set the solar wind
        if (data.error) {
            console.log(data.message)
            document.getElementById("solarWindSpeed").innerText = "ERROR"
            return
        }
        console.log(data)

        document.getElementById("solarWindSpeed").innerText = data.data * 3600
    });
}

setSolarWind()

function setXRay() {
    //fetch() the xray from /api/solarstatus/xray
    fetch("/api/solarstatus/xray").then(response => response.json()).then(data => {
        // Set the xray
        if (data.error) {
            console.log(data.message)
            document.getElementById("xRayStatus").innerText = "ERROR"
            return
        }
        console.log(data)

        document.getElementById("xRayStatus").innerText = data.data.toLowerCase()
    });
}

setXRay()

function setMagnetosphere() {
    //fetch() the magnetosphere from /api/solarstatus/magneto
    fetch("/api/solarstatus/magneto").then(response => response.json()).then(data => {
        // Set the magnetosphere
        if (data.error) {
            console.log(data.message)
            document.getElementById("magnetoStatus").innerText = "ERROR"
            return
        }
        console.log(data)

        document.getElementById("magnetoStatus").innerText = data.data.toLowerCase()
    });
}

setMagnetosphere()