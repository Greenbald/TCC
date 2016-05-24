var map;
var ajaxRequest;
var plotlist;
var plotlayers=[];


L.Map = L.Map.extend({
    openPopup: function(popup) {
        //        this.closePopup();  // just comment this
        this._popup = popup;

        return this.addLayer(popup).fire('popupopen', {
            popup: this._popup
        });
    }
}); /***  end of hack ***/

function initmap() {
	// set up the map
	map = new L.Map('map', {zoomControl:false});

	// create the tile layer with correct attribution
	var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
	var osmAttrib='Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
	var osm = new L.TileLayer(osmUrl, {minZoom: 8, maxZoom: 30, attribution: osmAttrib});		

	// start the map in Niteroi
	map.setView(new L.LatLng(-22.9029100, -43.1105500),15);
	map.addLayer(osm);
	L.control.zoom({
	     position:'bottomright'
	}).addTo(map);
}		