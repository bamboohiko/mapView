function GetMap()
{
    var map = new Microsoft.Maps.Map('#myMap', {
        credentials: 
        'AonZHtr87029fCW4keG_qAIVE_76xXDXPMPyB8a79QHPzM57N9wuRGXVeced35ev',
        center: new Microsoft.Maps.Location(13.495191631943101, 100.41977246667943),
        mapTypeId: Microsoft.Maps.MapTypeId.aerial,
        
    });


    for (var i = 0;i < data.features.length; i++) {
        if (data.features[i].geometry != null) {
            var cd = data.features[i].geometry.coordinates[0];
            var exteriorRing = [];
                
            for (var j = 0;j < cd.length; j++) {
                exteriorRing.push(new Microsoft.Maps.Location(cd[j][1],cd[j][0]));
            }

            //Create a polygon
            var polygon = new Microsoft.Maps.Polygon(exteriorRing, {
                fillColor: 'rgba(0, 255, 0, 0.5)',
                strokeColor: 'red',
                strokeThickness: 2
            });

            //Add the polygon to map
            map.entities.push(polygon);            
        }
    }
    /*
    //Add your post map load code here.
    $.ajax({
        type: "GET",
        url: "th2.json",
        dataType: "json",
        success: function (data) {
            for (var i = 0; i < data.length; i++) {
                if (item.geometry != null) {
                    var exteriorRing = item.geometry;

                    //Create a polygon
                    var polygon = new Microsoft.Maps.Polygon(exteriorRing, {
                        fillColor: 'rgba(0, 255, 0, 0.5)',
                        strokeColor: 'red',
                        strokeThickness: 2
                    });

                    //Add the polygon to map
                    map.entities.push(polygon);
                }
            }
        }
    });
    */

    /*
    $.getJSON('th2.json',function(data) {
        $.each(data.features, function(i, item) {
            if (item.geometry != null) {
                var exteriorRing = item.geometry;

                //Create a polygon
                var polygon = new Microsoft.Maps.Polygon(exteriorRing, {
                    fillColor: 'rgba(0, 255, 0, 0.5)',
                    strokeColor: 'red',
                    strokeThickness: 2
                });

                //Add the polygon to map
                map.entities.push(polygon);
            }
        })
    })
    */


    /*
    var center = map.getCenter();
    
    //Create array of locations to form a ring.
    var exteriorRing = [
        center,
        new Microsoft.Maps.Location(center.latitude - 0.5, center.longitude - 1),
        new Microsoft.Maps.Location(center.latitude - 0.5, center.longitude + 1),
        center
    ];

    //Create a polygon
    var polygon = new Microsoft.Maps.Polygon(exteriorRing, {
        fillColor: 'rgba(0, 255, 0, 0.5)',
        strokeColor: 'red',
        strokeThickness: 2
    });

    //Add the polygon to map
    map.entities.push(polygon);
    */
}