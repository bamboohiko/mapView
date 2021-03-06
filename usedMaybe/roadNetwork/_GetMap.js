function GetMap() {
    var map = new Microsoft.Maps.Map('#myMap', {
        credentials: 'AonZHtr87029fCW4keG_qAIVE_76xXDXPMPyB8a79QHPzM57N9wuRGXVeced35ev',
        center: new Microsoft.Maps.Location(13.495191631943101, 100.41977246667943),
        mapTypeId: Microsoft.Maps.MapTypeId.aerial,
        zoom: 10
    });
    
    var layer = new Microsoft.Maps.Layer()
    map.layers.insert(layer)

    //Load the GeoJson Module.
    Microsoft.Maps.loadModule('Microsoft.Maps.GeoJson', function () {    
        //Parse the GeoJson object into a Bing Maps shape.
        var shape = Microsoft.Maps.GeoJson.read(data, {
            PolylineOptions: {
                fillColor: 'rgba(0,0,0,0.5)',
                strokeColor: 'red',
                strokeThickness: 0.5
            }
        });

        layer.add(shape)        
        //Add the shape to the map.
    
    });
    
}
