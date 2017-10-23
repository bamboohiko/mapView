function GetMap()
{
    var map = new Microsoft.Maps.Map('#myMap', {
        credentials: 
        'AonZHtr87029fCW4keG_qAIVE_76xXDXPMPyB8a79QHPzM57N9wuRGXVeced35ev',
        center: new Microsoft.Maps.Location(13.495191631943101, 100.41977246667943),
        mapTypeId: Microsoft.Maps.MapTypeId.aerial,
        zoom: 10
        
    });

    var locs = [];

    for (var i = 0;i < data.features.length; i++) {
        if (data.features[i].geometry != null) {
            var cd = data.features[i].geometry.coordinates[0];
            var exteriorRing = [];
                
            for (var j = 0;j < cd.length; j++) {
                exteriorRing.push(new Microsoft.Maps.Location(cd[j][1],cd[j][0]));
            }

            locs = locs.concat(exteriorRing);

            //Create a polygon
            var polygon = new Microsoft.Maps.Polygon(exteriorRing, {
                //fillColor: 'rgba(0, 255, 0, 0.5)',
                strokeColor: 'red',
                strokeThickness: 2
            });

            //Add the polygon to map
            map.entities.push(polygon);

            /*
            Microsoft.Maps.Events.addHandler(polygon, 'click', function(e) {
                document.getElementById('output').innerHTML += ',' + i;

                setTimeout(function () { document.getElementById('output').innerHTML = null; }, 1000);
            });
            */  
        }
    }

    var rect = Microsoft.Maps.LocationRect.fromLocations(locs);

    map.setView({ 
        bounds: rect,
        padding: 80 

    });
    
}