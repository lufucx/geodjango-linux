var map = L.map('map').setView([-22.8932366, -42.1567423], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

const markers = JSON.parse(document.getElementById('markers-data').textContent);

const features = L.geoJSON(markers, {
    onEachFeature: function (feature, layer) {
        var popupContent = '<b>' + feature.properties.name + '</b>';
        if (feature.properties.description) {
            popupContent += '<br>' + feature.properties.description;
        }
        if (feature.properties.hyperlink) {
            popupContent += '<br><a href="' + feature.properties.hyperlink + '">Ver Mais</a>';
        }
        layer.bindPopup(popupContent);
    }
});

map.locate().on("locationfound", (e) => map.setView(e.latlng, 8)).on("locationerror", () => map.setView([0, 0], 5));

map.addLayer(features).fitBounds(features.getBounds());

async function load_markers() {
    const markers_url = `/api/markers/?in_bbox=${map.getBounds().toBBoxString()}`;
    const response = await fetch(markers_url);
    const geojson = await response.json();
    return geojson;
}

async function render_markers() {
    const markers = await load_markers();
    features.clearLayers(); // Clear existing markers before adding new ones
    features.addData(markers); // Add new markers
}

map.on("moveend", render_markers);