let map;
let heatmapData = []

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: 40.746009, lng: -73.89221575 },
    zoom: 11,
  });
}

function brandClicked(){
  let selectedBrands = [];

  if (document.getElementById("burgerKing").checked){
    selectedBrands.push("Burger King");
  }
  if (document.getElementById("mcDonalds").checked){
    selectedBrands.push("McDonald's");
  }
  if (document.getElementById("shakeShack").checked){
    selectedBrands.push("Shake Shack");
  }
  if (document.getElementById("fiveGuys").checked){
    selectedBrands.push("Five Guys");
  }

  if(selectedBrands.length > 0){
      let filtered_response = [];

      $.ajax({
            type: "GET",
            crossDomain: true,
            url: "https://franchise-filter.herokuapp.com/filter_info",
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            data: {
                selectedBrands: JSON.stringify(selectedBrands)
            },
            success: function (result) {
                for(var i = 0; i< result.length; i++){
                    drawCircle(result[i].location.lat, result[i].location.lng, i);
                }
            },
          error: function(request,status,errorThrown) {

          }
        });


            $.ajax({
            type: "GET",
            crossDomain: true,
            url: "https://franchise-filter.herokuapp.com/show_all",
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            data: {
                selectedBrands: JSON.stringify(selectedBrands)
            },
            success: function (result) {
                createHeatMap(result)
            },
          error: function(request,status,errorThrown) {

          }
        });
  }
}

function createHeatMap(result){
    heatmapData = [];
    result.forEach(element => {
        heatmapData.push(new google.maps.LatLng(element.location.lat, element.location.lng))
    });

    let heatmap = new google.maps.visualization.HeatmapLayer({data: heatmapData});
    heatmap.setMap(map);
}


function drawCircle(lat,lng,index){
        // Create marker
        var colors = ['#AA0000','#FFFF00','#00FF00']
        var marker = new google.maps.Marker({
          map: map,
          position: new google.maps.LatLng(lat,lng),
          title: 'Some location'
        });

        // Add circle overlay and bind to marker
        var circle = new google.maps.Circle({
          map: map,
          radius: 6000,    // 10 miles in metres
          fillColor: colors[index]
        });

        circle.bindTo('center', marker ,'position');
}