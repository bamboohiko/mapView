function GetMap() {
    var map = new Microsoft.Maps.Map('#myMap', {
        credentials: 'AonZHtr87029fCW4keG_qAIVE_76xXDXPMPyB8a79QHPzM57N9wuRGXVeced35ev',
        center: new Microsoft.Maps.Location(13.495191631943101, 100.41977246667943),
        mapTypeId: Microsoft.Maps.MapTypeId.aerial,
        zoom: 10
    });
    
    var layer = new Microsoft.Maps.Layer();
    var unionLayer = new Microsoft.Maps.Layer();

    map.layers.insert(layer);
    map.layers.insert(unionLayer);

    //Add right click mouse event to the layer.
    Microsoft.Maps.Events.addHandler(layer, 'click', function (e) {
        //Get the shape that the user right clicked on in the layer.
        var shape = e.primitive;
        var locs = shape.getLocations();

        shape.setOptions({
            fillColor: 'rgba(0, 255, 0, 0.5)',
            strokeColor: 'blue',
            strokeThickness: 1
        })

        layer.remove(shape)
        unionLayer.add(shape)
    });

    //Add right click mouse event to the layer.
    Microsoft.Maps.Events.addHandler(unionLayer, 'click', function (e) {
        //Get the shape that the user right clicked on in the layer.
        var shape = e.primitive;
        var locs = shape.getLocations();

        shape.setOptions({
            fillColor: 'rgba(0, 0, 0, 0.5)',
            strokeColor: 'red',
            strokeThickness: 1
        })

        unionLayer.remove(shape)
        layer.add(shape)
    });

    //Load the GeoJson Module.
    Microsoft.Maps.loadModule('Microsoft.Maps.GeoJson', function () {

        //Parse the GeoJson object into a Bing Maps shape.
        var shape = Microsoft.Maps.GeoJson.read(data, {
            polygonOptions: {
                fillColor: 'rgba(0,0,0,0.5)',
                strokeColor: 'red',
                strokeThickness: 0.5
            }
        });

        layer.add(shape);

        //Add the shape to the map.
    });


}
