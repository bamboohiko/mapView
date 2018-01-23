function GetMap()
{
    var map = new Microsoft.Maps.Map('#myMap', {
        credentials: 
        'AonZHtr87029fCW4keG_qAIVE_76xXDXPMPyB8a79QHPzM57N9wuRGXVeced35ev',
        center: new Microsoft.Maps.Location(13.495191631943101, 100.41977246667943),
        mapTypeId: Microsoft.Maps.MapTypeId.aerial,
        zoom: 10
        
    });

    //Add an infobox to the map so that we can display it when a shape is clicked.
    infobox = new Microsoft.Maps.Infobox(map.getCenter(), { visible: false });
    infobox.setMap(map);

    //Create a layer.
    var layer = new Microsoft.Maps.Layer();

    var locs = [];
    
    for (var i = 0;i < data.length; i++) {
        var cd = data[i];
        var exteriorRing = [];
            
        for (var j = 0;j < cd.length; j++) {
            exteriorRing.push(new Microsoft.Maps.Location(cd[j][1],cd[j][0]));
        }

        locs = locs.concat(exteriorRing);

        //Create a polygon
        var polygon = new Microsoft.Maps.Polygon(exteriorRing, {
            fillColor: 'rgba(0, 0, 0, 0.5)',
            strokeColor: 'red',
            strokeThickness: 1
        });

        layer.add(polygon);
        
        //Add the polygon to map
        //map.entities.push(polygon[i]);
    }
    
    /*
    locs = locs.concat(data[0])

    for (var i = 0;i < data[0].length; i++) {
        var cd = data[0][i];

        var pin = new Microsoft.Maps.Pushpin(new Microsoft.Maps.Location(cd[0], cd[1]), {
            text: i
        });


        layer.add(pin);
        
        //Add the polygon to map
        //map.entities.push(polygon[i]);
    }
    */
    map.layers.insert(layer)


    //Add right click mouse event to the layer.
    Microsoft.Maps.Events.addHandler(layer, 'click', function (e) {
        //Get the shape that the user right clicked on in the layer.
        var shape = e.primitive;
        var locs = shape.getLocations();

        var output = new Array()
        for (var i = 0;i < locs.length; i++)
            output[i] = '[' + locs[i].latitude + ', ' + locs[i].longitude + ']'
        document.getElementById('output').innerHTML += '[' + output.join() + '], ';
        //locs[cntUnion++] = shape.getLocations();

        shape.setOptions({
            fillColor: 'rgba(0, 255, 0, 0.5)',
            strokeColor: 'blue',
            strokeThickness: 1
        })
    });

    //Add right click mouse event to the layer.
    Microsoft.Maps.Events.addHandler(layer, 'dblclick', function (e) {
        //Get the shape that the user right clicked on in the layer.
        var shape = e.primitive;
        var locs = shape.getLocations();

        document.getElementById('output').innerHTML = '';

        shape.setOptions({
            fillColor: 'rgba(0, 0, 0, 0.5)',
            strokeColor: 'red',
            strokeThickness: 1
        })
    });

    var rect = Microsoft.Maps.LocationRect.fromLocations(locs);

    map.setView({ 
        bounds: rect,
        padding: 80 

    });
      
}