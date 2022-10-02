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

        document.getElementById("solarWindSpeed").innerText = (data.data * 3600).toLocaleString()
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

function setSunspot() {
    lat = window.location.search.split("&")[1].split("=")[1]
    lon = window.location.search.split("&")[2].split("=")[1]
    //fetch() sunspots from /api/sunspot_regions
    fetch("/api/sunspot_regions?lat=" + lat + "&lon=" + lon/2).then(response => response.json()).then(data => {
        // Set the sunspots
        if (data.error) {
            console.log(data.message)
            if (data.message == "No solar data") {
                document.getElementById("sunspotInfo").innerText = "nowhere near"
                return
            }
            document.getElementById("sunspotInfo").innerText = "ERROR"
            return
        }
        console.log(data)

        if (data.Approximate_Distance_SpaceApps < 6) {
            document.getElementById("sunspotInfo").innerText = "inside"
        } else {
            document.getElementById("sunspotInfo").innerText = "close to"
        }
    });
}

setSunspot()

function setFlare() {
    lat = window.location.search.split("&")[1].split("=")[1]
    lon = window.location.search.split("&")[2].split("=")[1]
    //fetch() flares from /api/solarflare
    fetch("/api/solar_regions?lat=" + lat + "&lon=" + lon/2).then(response => response.json()).then(data => {
        // Set the flares
        if (data.error) {
            console.log(data.message)
            if (data.message == "No solar data") {
                document.getElementById("flareInfo").innerText = "low"
                return
            }
            document.getElementById("flareInfo").innerText = "ERROR"
            return
        }
        console.log(data)

        if (data.Approximate_Distance_SpaceApps < 6) {
            document.getElementById("flareInfo").innerText = "extremely high"
        } else if (data.Approximate_Distance_SpaceApps < 12) {
            document.getElementById("flareInfo").innerText = "very high"
        } else {
            document.getElementById("flareInfo").innerText = "high"
        }
    });
}

setFlare()

function setTemperature() {
    lat = window.location.search.split("&")[1].split("=")[1]
    lon = window.location.search.split("&")[2].split("=")[1]
    //fetch() temperature from /api/temperature
    fetch("/api/get_temperature?lat=" + lat + "&lon=" + lon/2).then(response => response.json()).then(data => {
        // Set the temperature
        if (data.error) {
            console.log(data.message)
            document.getElementById("solTemp").innerText = "5700"
            return
        }
        console.log(data)

        document.getElementById("solTemp").innerText = Math.round(data.data).toLocaleString()

        temperature = data.data
        energyTransfer = ((temperature-273)*1889.1)
        cooking_time_seconds = ((199.2*38)/energyTransfer)
        cooking_time_millis = cooking_time_seconds*1000

        document.getElementById("eggVaporiseTime").innerText = cooking_time_millis.toLocaleString()
    });
}

setTemperature()