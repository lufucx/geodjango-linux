var map = L.map('map').setView([-22.8932366, -42.1567423], 11);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

googleStreets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{
        maxZoom: 20,
        subdomains:['mt0','mt1','mt2','mt3']
});

googleSat = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',{
        maxZoom: 20,
        subdomains:['mt0','mt1','mt2','mt3']
});

var greenIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
  });


const markers = JSON.parse(document.getElementById('markers-data').textContent);

const markerClusters = L.markerClusterGroup(); // Create a marker cluster group
markers.features.forEach(function(feature) {
    var marker = L.marker([feature.geometry.coordinates[1], feature.geometry.coordinates[0]], {icon: greenIcon});    
    var popupContent = '<b>' + feature.properties.name + '</b>';
    
    // Add city and category with a hyphen between them if they exist
    if (feature.properties.city && feature.properties.categories) {
        popupContent += '<br><i>' + feature.properties.city + ' - ' + feature.properties.categories + '</i><br>';
    } else if (feature.properties.city) {
        popupContent += '<br>' + feature.properties.city;
    } else if (feature.properties.categories) {
        popupContent += '<br>' + feature.properties.categories;
    }
    
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
        var marker = L.marker([feature.geometry.coordinates[1], feature.geometry.coordinates[0]], {icon: greenIcon});        
        var popupContent = '<b>' + feature.properties.name + '</b>';
        
        // Add city and category with a hyphen between them if they exist
        if (feature.properties.city && feature.properties.categories) {
            popupContent += '<br><i>' + feature.properties.city + ' - ' + feature.properties.categories + '</i>';
        } else if (feature.properties.city) {
            popupContent += '<br>' + feature.properties.city;
        } else if (feature.properties.categories) {
            popupContent += '<br>' + feature.properties.categories;
        }
        
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
// Layer Control
const baseLayers = {
    "OpenStreetMap": L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png'),
    "Google Maps": googleStreets,
    "Google Sattelite": googleSat,
};

L.control.layers(baseLayers).addTo(map);

map.on("moveend", render_markers);
