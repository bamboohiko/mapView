function GetMap() {
    var map = new Microsoft.Maps.Map('#myMap', {
        credentials: 'AonZHtr87029fCW4keG_qAIVE_76xXDXPMPyB8a79QHPzM57N9wuRGXVeced35ev',
        center: new Microsoft.Maps.Location(13.495191631943101, 100.41977246667943),
        mapTypeId: Microsoft.Maps.MapTypeId.aerial,
        zoom: 10
    });
    
    var k = 7;

    //Load the GeoJson Module.
    Microsoft.Maps.loadModule('Microsoft.Maps.GeoJson', function () {


        for (var i = 0;i < k; i++) {
            //Parse the GeoJson object into a Bing Maps shape.
            var shape = Microsoft.Maps.GeoJson.read(data[i], {
                PolylineOptions: {
                    fillColor: 'rgba(0,0,0,0.5)',
                    strokeColor: 'red',
                    strokeThickness: 0.5
                }
            });

            var layer = new Microsoft.Maps.Layer();
            layer.add(shape)
            layer.setVisible(true)
            map.layers.insert(layer);
            
            //Add the shape to the map.
        }
    });
    
    //Create an infobox that will render in the center of the map.
    var infobox = new Microsoft.Maps.Infobox(new Microsoft.Maps.Location(13.395191631943101, 100.51977246667943), {
        //title: 'Union Options',
        description: 'Optional',
        showPointer: false, 
        showCloseButton: false,
        maxHeight: 2000,
        actions: [{
            label: 'highway4',
            eventHandler: function () {
                var sta =  map.layers[1].getVisible();
                 map.layers[1].setVisible(!sta);
            }
        },{
            label: 'tertiary',
            eventHandler: function () {
                var sta =  map.layers[2].getVisible();
                 map.layers[2].setVisible(!sta);
            }
        },{
            label: 'stream',
            eventHandler: function () {
                var sta =  map.layers[3].getVisible();
                 map.layers[3].setVisible(!sta);
            }
        },{
            label: 'canal',
            eventHandler: function () {
                var sta =  map.layers[4].getVisible();
                 map.layers[4].setVisible(!sta);
            }
        },{
            label: 'river',
            eventHandler: function () {
                var sta =  map.layers[5].getVisible();
                 map.layers[5].setVisible(!sta);
            }
        },{
            label: 'rail',
            eventHandler: function () {
                var sta =  map.layers[6].getVisible();
                 map.layers[6].setVisible(!sta);
            }
        }]
    });

    //Assign the infobox to a map instance.
    infobox.setMap(map);
    
}
