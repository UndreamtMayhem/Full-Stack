var NeighbourhoodMAP = NeighbourhoodMAP || {};

var NeighbourhoodMAP = (function (w, d, $) {
  // private vars
  var isStorageEnabled = checkStorage();
  // make data retrived public
  var dataFromStorage = retriveFromStorage();

  // private functions 
  // determine is local storage exists
  function checkStorage() {
    console.log("check storage run");
    if (typeof window.Storage !== "undefined") {
      // Code for localStorage/sessionStorage.
      return true;
    } else {
      console.log("fails do nothing");
      // Sorry! No Web Storage support..
      return false;
    }
  }
  // try to get places from storage if exists
  function retriveFromStorage() {
    console.log("retriveFromStorage")
    // return undefined to make it obvious that 
    // local storage return undefined
    if (localStorage['places'] != undefined) {
      return localStorage['places'];

    }
    else {
      return undefined;
    }

  }
  // call to run this 
  function setDataIfLocalStorageAvailable() {
    console.log("setDataIfLocalStorageAvailable")
    // if the data is empty and storage enabled 
    // make json call and store the data in local
    if (dataFromStorage === undefined && isStorageEnabled) {
      $.getJSON("/places/", function (data) {
        // Code for localStorage/sessionStorage.
        // insert code to be run when the composition is fully loaded here
        var placesData = JSON.stringify(data);
        localStorage.setItem("places", placesData);
      });
    }
  }
  function run() {
    this.setDataIfLocalStorageAvailable();
  }
  return {
    // public
    dataFromStorage: dataFromStorage,
    setDataIfLocalStorageAvailable: setDataIfLocalStorageAvailable,
    run: run,
  };
}(window, document, jQuery));

// Dom interactions
NeighbourhoodMAP.domManipulation = (function () {
  // move to dom manipulation
  var changeAsideContentWithDB = function (doc, searchLocation) {
    $('.place-name').html(doc[0]['title']);
    $('#facts-text').html(doc[0]['snippet']);
    $('#secondary-text').html(doc[1]['snippet'] + " <a href='www.wikipedia.com'>Wikipedia</a>");
    $('.place-img').attr('src', '/img/' + searchLocation + '.jpg');
    $('.photos-responsive').attr('src', '/img/' + searchLocation + '1.jpg');
    $('aside').removeClass('menu-hidden');
    $('#autocomplete').attr('placeholder', searchLocation);
  };

  var changeAsideContentWithJSON = function changeAsideContentWithJSON(placeOBJ, searchLocation) {
    console.log("how often am i ran")
    $('.place-name').html(placeOBJ['query']['search'][0]['title']);
    $('#facts-text').html(placeOBJ['query']['search'][0]['snippet']);
    $('#secondary-text').html(placeOBJ['query']['search'][1]['snippet'] + "<a href='www.wikipedia.com'> Wikipedia</a>");
    $('.place-img').attr('src', '/img/' + searchLocation + '.jpg');
    $('.photos-responsive').attr('src', '/img/' + searchLocation + '1.jpg');
    $('aside').removeClass('menu-hidden');
    $('#autocomplete').attr('placeholder', searchLocation);
  };

  return {
    changeAsideContentWithDB: changeAsideContentWithDB,
    changeAsideContentWithJSON: changeAsideContentWithJSON
  }


})();

// get location from search box
// update aside
NeighbourhoodMAP.getLocation = function (locArr, addMarker) {
  var dataFromStorage = NeighbourhoodMAP.dataFromStorage;
  console.log(dataFromStorage);
  var searchLocation = locArr[0].toLowerCase().replace(" ", "");

  // is there data in the storage
  // if so use it
  if (dataFromStorage != undefined) {
    var places = JSON.parse(dataFromStorage);
    // repetitive
    for (var key in places) {
      if (places.hasOwnProperty(key)) {
        var placeOBJ = places[key];
        var locationName = placeOBJ['query']['search'][0]['title'].toLowerCase().replace(" ", "");
        if (locationName === searchLocation) {
          // this is a sepearte task refactor
          NeighbourhoodMAP.domManipulation.changeAsideContentWithJSON(placeOBJ, searchLocation);
        }
      }
    }
  }
  else {
    NeighbourhoodMAP.failedStorage(searchLocation);
  }
};

// deal with possible failure of local storage
NeighbourhoodMAP.failedStorage = function (searchLocation) {
  // new connection
  var db = new zango.Db('localdb', { place: ['a'] });
  // get collection or create it if it dont exist
  var place = db.collection('place');

  // see how many places we have saved
  place.find({}).toArray((error, docs) => {
    // Data is stored in mongo db
    if (docs.length > 0) {
      // go over the documents
      for (var key in docs) {
        if (docs.hasOwnProperty(key)) {
          var doc = docs[key];
          var locationName = doc[0]['title'].toLowerCase().replace(" ", "");
          if (locationName === searchLocation) {
            changeAsideContentWithDB(doc, searchLocation);
          }
        }
      }
    }
    else {
      $.getJSON("/places/", function (places) {
        let docs = [];
        for (var key in places) {
          if (places.hasOwnProperty(key)) {
            var placeOBJ = places[key];
            docs.push(placeOBJ['query']['search']);
            var locationName = placeOBJ['query']['search'][0]['title'].toLowerCase().replace(" ", "");
            if (locationName === searchLocation) {
              changeAsideContentWithJSON(placeOBJ, searchLocation);
            }
          }
        }
        place.insert(docs).then(() => {
          return true;
        }).catch(error => console.error(error));
      });
    }
  }, (error) => {
    if (error) {
      throw error;
    }
  });


};

// move to events
NeighbourhoodMAP.autocompleteSearch = (function ($) {
  console.log("autocompleteSearch bseems to workroke");
  //private
  var tags = ['Sennen', 'Porthcurno', 'Minack Theatre', 'Botallack', 'St Ives', 'Hayle',
    'Gwithan', 'Marazion', 'Penzance', 'Porthgwarra', 'Mousehole', 'Lamorna', 'St Just', 'Newlyn', 'Zennor', 'Porthleven'];

  $('#autocomplete').autocomplete({
    source: function (request, response) {
      var matcher = new RegExp('^' + $.ui.autocomplete.escapeRegex(request.term), 'i');
      response($.grep(tags, function (item) {
        return matcher.test(item);
      }));
    }
  });

})(jQuery);


NeighbourhoodMAP.buttonLogic = (function ($, locationFunc) {
  var locationInfo = locationFunc;

  var dataFromStorage = this.NeighbourhoodMAP.dataFromStorage;


  console.log(dataFromStorage);
  $('.hamburger-btn').click(function () {
    $('.places').toggleClass('places-hidden');
  });
  // add x button to aside
  /*
      $('main').click(function (event) {
        event.stopPropagation();
        $('aside').addClass('menu-hidden');
      });
  */
  $('.search-btn').click(function () {
    // get search input
    var selectedLocation = $('.search-input').val().trim().toLowerCase();
    if (selectedLocation.length > 1) {
      matchSearchTerm(selectedLocation);
    }
    else {
      $('#autocomplete').attr('placeholder', 'no match');
      $('#autocomplete').val('');
    }
    function matchSearchTerm(selectedLocation) {
      for (var i = 0; i < locations.length; i++) {
        // if it is a straight match then great XD
        if (locations[i][0].toLowerCase() == selectedLocation) {
          clearMarkers();
          addMarker(locations[i], "all");
          locationInfo(locations[i]);
          return;
        }

        else if (locations[i][0].toLowerCase().startsWith(selectedLocation) && selectedLocation.length > 1) {
          clearMarkers();
          addMarker(locations[i], "all");
          locationInfo(locations[i]);
          return;
        }

        else if (locations[i][0].toLowerCase().endsWith(selectedLocation) && selectedLocation.length > 1) {
          clearMarkers();
          addMarker(locations[i], "all");
          locationInfo(locations[i]);
          return;
        }
      }
      for (var j = 0; j < locations.length; j++) {
        var start = 0;
        var mid = 0;
        var end = selectedLocation.length;
        var midForEnd = 0;
        var endForEnds = selectedLocation.length;
        // binary search string
        while (start != end) {
          // zero to midpoint 
          mid = Math.floor(start + end / 2);
          // midpoint to end of string
          midForEnd = Math.ceil((midForEnd += endForEnds) / 2);
          var editedStr = selectedLocation.substring(start, mid);

          var seceditedStr = selectedLocation.substring(midForEnd, endForEnds);

          if (locations[j][0].toLowerCase().startsWith(editedStr) && end >= 1 && editedStr.length > 1) {
            clearMarkers();
            addMarker(locations[j], "all");
            locationInfo(locations[j]);
            end = 0;
            return;
          }
          else if (locations[j][0].toLowerCase().endsWith(seceditedStr) && seceditedStr.length > 1) {
            clearMarkers();
            addMarker(locations[j], "all");
            locationInfo(locations[j]);
            return;
          }
          end = mid;
        }
      }
      $('#autocomplete').attr('placeholder', 'no match');
      $('#autocomplete').val('');
    }
  });
})(jQuery, NeighbourhoodMAP.getLocation);


NeighbourhoodMAP.runKnockout = (function(){
     // Knockout
    // populate this better
    var PlacesModel = function () {
      this.places = ko.observableArray([
        { name: 'Hayle', type: 'visited' },
        { name: 'St ives', type: 'visited' },
        { name: 'Sennen', type: 'visited' },
        { name: 'Porthgwarra', type: 'visited' },
        { name: 'Penzance', type: 'notvisited' },
        { name: 'Bottallack', type: 'visited' },
        { name: 'St Buryan', type: 'visited' },
        { name: 'Gwithian', type: 'visited' },
        { name: 'Porthcurno', type: 'visited' },
        { name: 'Mousehole', type: 'notvisited' },
        { name: 'Lamorna', type: 'notvisited' },
        { name: 'Saint-Just', type: 'notvisited' },
        { name: 'Newlyn', type: 'notvisited' },
        { name: 'Zennor', type: 'notvisited' },
        { name: 'Marazion', type: 'notvisited' },
        { name: 'Porthleven', type: 'visited' },
        { name: 'Minack Theatre', type: 'visited' }
      ]);
      this.typeToShow = ko.observable('all');
      this.displayAdvancedOptions = ko.observable(false);
      this.placesToShow = ko.computed(function () {
        // Represents a filtered list of places
        var desiredType = this.typeToShow();
        if (desiredType == 'all' && deselected) {
          deleteMarkers();
          addMarkers(locations);
          return this.places();
        }
        if (desiredType == 'all') {
          return this.places();
        }
        return ko.utils.arrayFilter(this.places(), function (place) {
          // if place is notvisited add a marker as notvisited
          if (desiredType == 'notvisited') {
            deselected = true;
            deleteMarkers();
            addMarkers(locations, 'notvisited');
          }
          if (desiredType == 'visited') {
            deselected = true;
            deleteMarkers();
            addMarkers(locations, 'visited');
          }
          return place.type == desiredType;
        });
      }, this);
      // Animation callbacks for the places list
      this.showPlacesElement = function (elem) { if (elem.nodeType === 1) $(elem).hide().slideDown(); };
      this.hidePlacesElement = function (elem) { if (elem.nodeType === 1) $(elem).slideUp(function () { $(elem).remove(); }); };
    };
    // Here's a custom Knockout binding that makes elements shown/hidden via jQuery's fadeIn()/fadeOut() methods
    // Could be stored in a separate utility library
    ko.bindingHandlers.fadeVisible = {
      init: function (element, valueAccessor) {
        // Initially set the element to be instantly visible/hidden depending on the value
        var value = valueAccessor();
        $(element).toggle(ko.utils.unwrapObservable(value));
        // Use "unwrapObservable" so we can handle values that may or may not be observable
      },
      update: function (element, valueAccessor) {
        // Whenever the value subsequently changes, slowly fade the element in or out
        var value = valueAccessor();
        ko.utils.unwrapObservable(value) ? $(element).fadeIn() : $(element).fadeOut();
      }
    }

    ko.applyBindings(new PlacesModel());


})();


$(document).ready(function () {
  NeighbourhoodMAP.run();
});