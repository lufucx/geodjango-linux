var map = L.map('map').setView([-22.87976527566221, -42.139631566232666], 11);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var iconMapping = {
    'red': L.icon({
        iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
        shadowSize: [41, 41]
    }),
    'blue': L.icon({
        iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-blue.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
        shadowSize: [41, 41]
    }),
    'green': L.icon({
        iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
        shadowSize: [41, 41]
    }),
    'yellow': L.icon({
        iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-yellow.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
        shadowSize: [41, 41]
    }),
    'orange': L.icon({
        iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-orange.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
        shadowSize: [41, 41]
    }),
    'violet': L.icon({
        iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-violet.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
        shadowSize: [41, 41]
    }),
    // Add more icons as needed
};

// Initialize overlay layer groups
// Initialize overlay layer groups
const categoryLayers = {};
const cityLayers = {};

// Fetch marker data
const markers = JSON.parse(document.getElementById('markers-data').textContent);

// Create layer groups for each category and city
markers.features.forEach(function (feature) {
    const category = feature.properties.categories;
    const city = feature.properties.city;

    // Initialize layers if they don't exist
    if (!categoryLayers[category]) {
        categoryLayers[category] = L.layerGroup();
    }
    if (!cityLayers[city]) {
        cityLayers[city] = L.layerGroup();
    }
});

// Create a marker cluster group
const markerClusters = L.markerClusterGroup();

// Function to add markers to the appropriate layer groups
function addMarkersToLayers() {
    markers.features.forEach(function (feature) {
        const iconChoice = feature.properties.icon_choice;
        var icon = iconMapping[iconChoice] || iconMapping['green']; // Default to greenIcon if icon choice not found
        var marker = L.marker([feature.geometry.coordinates[1], feature.geometry.coordinates[0]], { icon: icon });
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
        if (feature.properties.post) {
            var postUrl = `/posts/p/${feature.properties.post}/`;
            popupContent += '<br><a href="' + postUrl + '">Ver Mais</a>';
        }

        marker.bindPopup(popupContent);

        // Add marker to the appropriate category and city layers
        if (categoryLayers[feature.properties.categories]) {
            categoryLayers[feature.properties.categories].addLayer(marker);
        }
        if (cityLayers[feature.properties.city]) {
            cityLayers[feature.properties.city].addLayer(marker);
        }

        // Add marker to the marker cluster group
        markerClusters.addLayer(marker);
    });
}

// Add markers to the layers
addMarkersToLayers();

// Add the marker cluster group to the map
map.addLayer(markerClusters);

// Combine the overlays into one object for controls
const cityLayer = {
    ...cityLayers
};

const categoryLayer = {
    ...categoryLayers
};

// Function to update markers based on selected layer
function updateMarkersOnSelection(selectedLayer) {
    markerClusters.clearLayers(); // Clear all markers
    selectedLayer.eachLayer(layer => markerClusters.addLayer(layer)); // Add only the selected markers
}

// Event listener for layer add and remove events
map.on('overlayadd', function (e) {
    if (cityLayers[e.name]) {
        updateMarkersOnSelection(cityLayers[e.name]);
    } else if (categoryLayers[e.name]) {
        updateMarkersOnSelection(categoryLayers[e.name]);
    }
});

map.on('overlayremove', function (e) {
    // When a layer is removed, re-add all markers to ensure visibility
    markerClusters.clearLayers();
    addMarkersToLayers();
});

// Add the base layers and overlay layers to the map
L.control.layers(null, categoryLayer, { collapsed: false, position: 'topright' }).addTo(map);
L.control.layers(null, cityLayer, { collapsed: false, position: 'topright' }).addTo(map);

// Function to render markers dynamically as the map moves
async function render_markers() {
    const markers = await load_markers();
    markerClusters.clearLayers(); // Clear existing markers before adding new ones

    // Add markers to layers and map
    addMarkersToLayers();
}

// Listen to map movement and render markers accordingly
map.on("moveend", render_markers);

// Full screen map view
var mapId = document.getElementById('map');
function fullScreenView() {
    if (document.fullscreenElement) {
        document.exitFullscreen()
    } else {
        mapId.requestFullscreen();
    }
}

// Reset view
$('.zoom-to-layer').click(function () { map.setView([-22.87976527566221, -42.139631566232666], 11) });

// Print map
L.control.browserPrint({ position: 'topright' }).addTo(map);

// Search function
L.Control.geocoder().addTo(map);

// Button to resize map
let resizeButton = L.Control.extend({
    onAdd: function () {
        var container = L.DomUtil.create('div', 'leaflet-control leaflet-resize-control leaflet-bar');
        var button = L.DomUtil.create('a', 'leaflet-control-zoom-in leaflet-bar-part', container);
        button.innerHTML = '<i class="fa-solid fa-repeat"></i>';
        button.title = 'Resize Map'; // Tooltip

        L.DomEvent.disableClickPropagation(container);

        button.addEventListener('click', function () {
            map.setView([-22.87976527566221, -42.139631566232666], 11);
        });

        button.style.cursor = 'pointer';

        return container;
    }
});

new resizeButton({ position: 'topright' }).addTo(map);

// Button to toggle full-screen
let fullScreenButton = L.Control.extend({
    onAdd: function () {
        var container = L.DomUtil.create('div', 'leaflet-control leaflet-fullscreen-control leaflet-bar');
        var button = L.DomUtil.create('a', 'leaflet-control-zoom-in leaflet-bar-part', container);
        button.innerHTML = '<i class="fa-solid fa-expand"></i>';       
        button.title = 'Toggle Full Screen'; // Tooltip

        L.DomEvent.disableClickPropagation(container);

        button.addEventListener('click', function () {
            if (document.fullscreenElement) {
                document.exitFullscreen();
            } else {
                mapId.requestFullscreen();
            }
        });

        button.style.cursor = 'pointer';

        return container;
    }
});

new fullScreenButton({ position: 'topright' }).addTo(map);
