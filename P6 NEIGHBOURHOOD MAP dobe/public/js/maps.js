var deselected = false;
var markers = [];

var locations = [['Sennen', 50.0722231, -5.6989485, 4, 'visited'],
['Porthcurno', 50.0452198, -5.6652907, 5, 'visited'],
['Minack Theatre', 50.040004, -5.6611024, 3, 'notvisited'],
['Botallack', 50.1326477, -5.6927381, 2, 'visited'],
['St Ives', 50.2106736, -5.5054389, 1, 'visited'],
['Hayle', 50.1849164, -5.4455896, 6, 'visited'],
['Gwithian', 50.219449, -5.388760, 7, 'visited'],
['Marazion', 50.1277873, -5.4836227, 8, 'notvisited'],
['Penzance', 50.1196207, -5.5781513, 9, 'notvisited'],
['Porthgwarra', 50.0371557, -5.6743855, 10, 'visited'],
['Mousehole', 50.082786, -5.5493099, 11, 'notvisited'],
['Lamorna', 50.0672073, -5.5727157, 12, 'notvisited'],
['Saint-Just', 50.126777, -5.695046, 13, 'notvisited'],
['Newlyn', 50.1020977, -5.5698346, 14, 'notvisited'],
['Zennor', 50.1910438, -5.5734626, 15, 'notvisited'],
['Porthleven', 50.0872088, -5.334227, 17, 'visited']
];

// Adds specified markers to the map and push to the marker array.
function addMarkers(locations, selectedtype = "all") {

  // go over every location
  for (i = 0; i < locations.length; i++) {
    // fetch all the selected types from locations and add a marker
    if (locations[i][4] == selectedtype || selectedtype == 'all') {
      var marker = new google.maps.Marker({
        position: { lat: locations[i][1], lng: locations[i][2] },
        map: map
      });

      google.maps.event.addListener(marker, 'click', (function (marker, i) {
        return function () {
          infowindow.setContent(locations[i][0]);
          infowindow.open(map, marker);
          $('.list-menu').click(function () {
            infowindow.setContent(locations[i][0]);
            infowindow.open(map, marker);
          })
          $('aside').removeClass('menu-hidden');
          console.log();
          NeighbourhoodMAP.getLocation(locations[i]);
        }
      })(marker, i));
      markers.push(marker);
    }
  }
}

function addMarker(location, type = "all") {
    
  if (location[4] == type || type == 'all') {
    var marker = new google.maps.Marker({
      position: { lat: location[1], lng: location[2] },
      map: map
    });
    google.maps.event.addListener(marker, 'click', (function (marker, i) {
      return function () {
        infowindow.setContent(location[0]);
        infowindow.open(map, marker);
        $('.list-menu').click(function () {
          infowindow.setContent(location[0])
          infowindow.open(map, marker);
        });
        $('aside').removeClass('menu-hidden');
        NeighbourhoodMAP.getLocation(location);
      }
    })(marker));
    markers.push(marker);
  }
}
// Sets the map on all markers in the array.
function setMapOnAll(map) {
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(map);
  }
}


// Removes the markers from the map, but keeps them in the array.
function clearMarkers() {
  setMapOnAll(null);
}

// Shows any markers currently in the array.
function showMarkers() {
  setMapOnAll(map);
}

// Deletes all markers in the array by removing references to them.
function deleteMarkers() {
  clearMarkers();
  markers = [];
}



function initMap() {
  // Create a map object and specify the DOM element for display.
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 11,
    center: new google.maps.LatLng(50.085871, -5.7108391),
    mapTypeId: 'terrain'
  });
  //on start add info windows and set all markers
  infowindow = new google.maps.InfoWindow();
  addMarkers(locations);
}