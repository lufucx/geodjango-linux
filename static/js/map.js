var map = L.map('map').setView([-22.8932366, -42.1567423], 11);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

googleStreets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{
        maxZoom: 20,
        subdomains:['mt0','mt1','mt2','mt3']
});

googleSat = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',{
        maxZoom: 20,
        subdomains:['mt0','mt1','mt2','mt3']
});

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

const markers = JSON.parse(document.getElementById('markers-data').textContent);

const markerClusters = L.markerClusterGroup(); // Create a marker cluster group
markers.features.forEach(function(feature) {
    const iconChoice = feature.properties.icon_choice; // Choose the appropriate icon based on the icon choice
    var icon = iconMapping[iconChoice] || greenIcon; // Default to greenIcon if icon choice not found
    var marker = L.marker([feature.geometry.coordinates[1], feature.geometry.coordinates[0]], { icon: icon });    
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
    if (feature.properties.post) {
        var postUrl = `/posts/p/${feature.properties.post}/`; // Construa a URL para a página do post vinculado
        popupContent += '<br><a href="' + postUrl + '">Ver Mais</a>';
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
        const iconChoice = feature.properties.icon_choice; // Choose the appropriate icon based on the icon choice
        var icon = iconMapping[iconChoice] || greenIcon; // Default to greenIcon if icon choice not found
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
            var postUrl = `/posts/p/${feature.properties.post}/`; // Construa a URL para a página do post vinculado
            popupContent += '<br><a href="' + postUrl + '">Ver Mais</a>';
        }
        
        marker.bindPopup(popupContent);
        markerClusters.addLayer(marker); // Add marker to the cluster group
    });
}

// Layer Control
const baseLayers = {
    "OpenStreetMap": L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png'),
    "Google Maps": googleStreets,
    "Google Satellite": googleSat,
};

L.control.layers(baseLayers, null, { collapsed: false, position: 'topright' }).addTo(map);
map.on("moveend", render_markers);

//Full screen map view
var mapId = document.getElementById('map');
function fullScreenView() {
    if (document.fullscreenElement) {
        document.exitFullscreen()
    } else {
        mapId.requestFullscreen();
    }
}

// Reset view
$('.zoom-to-layer').click(function () {map.setView([-22.8932366, -42.1567423], 11)});

// Print map
L.control.browserPrint({ position: 'topright' }).addTo(map);


// Search function
L.Control.geocoder().addTo(map);

// Legenda
let CollapsibleTextbox = L.Control.extend({
    onAdd: function() {
        // Create a container for the control
        var container = L.DomUtil.create('div', 'leaflet-control-collapsible-textbox');
        
        // Create a button to toggle the text box visibility
        var button = L.DomUtil.create('button', 'leaflet-control-collapsible-textbox-button', container);
        button.innerHTML = '<span class="material-symbols-outlined">share_location</span>';
        button.title = 'Toggle Info Box'; // Tooltip
        // Apply CSS styles to the button to make it larger
        button.style.fontSize = '16px'; // Adjust the font size as desired
        button.style.padding = '3.5px'; // Adjust padding as desired
        button.style.cursor = 'pointer'; // Change cursor to pointer when hovering
        button.style.backgroundColor = 'white'; // Set button background color to white

        
        
        // Create the text box
        var textBox = L.DomUtil.create('div', 'leaflet-control-collapsible-textbox-content', container);
        textBox.innerHTML = `
            <img src="https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png" alt="Perigo" style="width:10px; height:auto; display:inline; margin-right:10px;">
            <span style="display:inline; vertical-align:top;">Vermelho</span><br>
            <img src="https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png" alt="Perigo" style="width:10px; height:auto; display:inline; margin-right:10px;">
            <span style="display:inline; vertical-align:top;">Verde</span><br>
            <img src="https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-orange.png" alt="Perigo" style="width:10px; height:auto; display:inline; margin-right:10px;">
            <span style="display:inline; vertical-align:top;">Laranja</span><br>
            <img src="https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-yellow.png" alt="Perigo" style="width:10px; height:auto; display:inline; margin-right:10px;">
            <span style="display:inline; vertical-align:top;">Amarelo</span><br>
            <img src="https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-blue.png" alt="Perigo" style="width:10px; height:auto; display:inline; margin-right:10px;">
            <span style="display:inline; vertical-align:top;">Azul</span><br>
            <img src="https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-violet.png" alt="Perigo" style="width:10px; height:auto; display:inline; margin-right:10px;">
            <span style="display:inline; vertical-align:top;">Roxo</span><br>
        `;
        
        // Add styles to the text box
        textBox.style.backgroundColor = 'white';
        textBox.style.color = 'black';
        textBox.style.padding = '10px';
        textBox.style.borderRadius = '5px';
        textBox.style.boxShadow = '2px 2px 5px rgba(0, 0, 0, 0.3)';
        
        // Initially hide the text box
        textBox.style.display = 'none';
        
        // Add click event listener to the button
        button.addEventListener('click', function() {
            // Toggle the display of the text box
            if (textBox.style.display === 'none') {
                textBox.style.display = 'block';
            } else {
                textBox.style.display = 'none';
            }
        });
        
        // Return the container element
        return container;
    }
});

// Create and add the collapsible text box control to the map
new CollapsibleTextbox({ position: 'topleft' }).addTo(map);
