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

        window.nameToID = {}

        // For each item in the JSON array, add
        data.data.forEach(item => {
            console.log(item)
            window.nameToID[item.name] = item.id
            document.getElementById("searchitems-container").innerHTML += "<div class=\"searcheditem\" onclick='goToElement(this)'>" + item.name + ", " + item.container + "</div>";
        });
    });
}

function goToElement(element) {
    goToID(window.nameToID[element.innerHTML.split(", ")[0]])
}

function goToID(id) {
    window.location.href = "/location?id=" + id
}

window.onload = function() {
    updatePlaceList()
}