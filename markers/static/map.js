var map = L.map('map').setView([-22.8932366, -42.1567423], 11);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

const markers = JSON.parse(document.getElementById('markers-data').textContent);

const markerClusters = L.markerClusterGroup(); // Create a marker cluster group

markers.features.forEach(function(feature) {
    var marker = L.marker([feature.geometry.coordinates[1], feature.geometry.coordinates[0]]);
    
    var popupContent = '<b>' + feature.properties.name + '</b>';
    if (feature.properties.description) {
        popupContent += '<br>' + feature.properties.description;
    }
    if (feature.properties.hyperlink) {
        popupContent += '<br><a href="' + feature.properties.hyperlink + '">Ver Mais</a>';
    }
    
    marker.bindPopup(popupContent);
    markerClusters.addLayer(marker); // Add marker to the cluster group
});

map.addLayer(markerClusters); // Add the marker cluster group to the map

map.locate().on("locationfound", (e) => map.setView([-22.8932366, -42.1567423], 11));

async function load_markers() {
    const markers_url = `/api/markers/?in_bbox=${map.getBounds().toBBoxString()}`;
    const response = await fetch(markers_url);
    const geojson = await response.json();
    return geojson;
}

async function render_markers() {
    const markers = await load_markers();
    markerClusters.clearLayers(); // Clear existing markers before adding new ones
    
    markers.features.forEach(function(feature) {
        var marker = L.marker([feature.geometry.coordinates[1], feature.geometry.coordinates[0]]);
        
        var popupContent = '<b>' + feature.properties.name + '</b>';
        if (feature.properties.description) {
            popupContent += '<br>' + feature.properties.description;
        }
        if (feature.properties.hyperlink) {
            popupContent += '<br><a href="' + feature.properties.hyperlink + '">Ver Mais</a>';
        }
        
        marker.bindPopup(popupContent);
        markerClusters.addLayer(marker); // Add marker to the cluster group
    });
}

map.on("moveend", render_markers);
