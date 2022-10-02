function updatePlaceList() {
    // Make a fetch() request (GET) to /api/get_locations with query parameter "query" set to
    // the value of the search box, then parse the output as JSON and update the list of searchitems
    fetch("/api/get_locations?query=" + document.getElementById("searchbox").value).then(response => response.json()).then(data => {
        // Clear the list of searchitems
        document.getElementById("searchitems-container").innerHTML = "";

        if (data.error) {
            console.log(data.message)
            return
        }

        window.IDToData = {}

        // For each item in the JSON array, add
        data.data.forEach(item => {
            console.log(item)
            window.IDToData[item.id] = item
            document.getElementById("searchitems-container").innerHTML += `<div class="searcheditem" onclick='goToElement(${item.id})'> ${item.name}, ${item.container} (${item.country}) </div>`
        });

        try {
            setLatLong(data.data[0].latitude, data.data[0].longitude)
        } catch (err) {
            console.log(err)
        }
    });
}

function goToElement(elementID) {
    data = window.IDToData[elementID]
    goTo(data.id, data.latitude, data.longitude, data.name)
}

function goTo(id, lat, lon, name) {
    window.location.href = "/location?id=" + id + "&lat=" + lat + "&lon=" + lon + "&name=" + name
}

window.onload = function () {
    updatePlaceList()
}