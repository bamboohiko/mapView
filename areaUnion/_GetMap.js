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

    var cacheLayer = new Array();
    var cacheShape = new Array();
    var cnt = 0

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

    //Create an infobox that will render in the center of the map.
    var infobox = new Microsoft.Maps.Infobox(new Microsoft.Maps.Location(13.395191631943101, 100.51977246667943), {
        //title: 'Union Options',
        description: '-------------Union Options-----------',
        maxHeight: 10000 ,
        maxWidth: 1024,
        showPointer: false, 
        showCloseButton: false,
        actions: [{
            label: 'union',
            eventHandler: function () {
                var shapes1 = unionLayer.getPrimitives();

                var newShapes1 = Microsoft.Maps.GeoJson.read(areaUnion(Microsoft.Maps.GeoJson.write(shapes1)), {
                    polygonOptions: {
                        fillColor: 'rgba(0,127,0,0.5)',
                        strokeColor: 'blue',
                        strokeThickness: 1
                    }
                });

                cacheLayer[cnt] = shapes1;
                cacheShape[cnt] = newShapes1;
                cnt += 1;

                unionLayer.clear();
                layer.add(newShapes1);
            }
        }, {
            label: 'back',
            eventHandler: function () {
                if (cnt > 0) {
                    cnt -= 1;
                    var shapes1 = cacheLayer[cnt];
                    var newshapes1 = cacheShape[cnt];
                    
                    layer.remove(newshapes1);
                    for (i in shapes1) {
                        shapes1[i].setOptions({
                            fillColor: 'rgba(0, 0, 0, 0.5)',
                            strokeColor: 'red',
                            strokeThickness: 1
                        });
                    }
                    layer.add(shapes1);

                
                }
            }
        }, {
            label: 'clear',
            eventHandler: function () {
                unionLayer.clear();
                layer.clear();

                var shape = Microsoft.Maps.GeoJson.read(data, {
                    polygonOptions: {
                        fillColor: 'rgba(0,0,0,0.5)',
                        strokeColor: 'red',
                        strokeThickness: 0.5
                    }
                });

                layer.add(shape);                
            }
        }, {
            label: 'output',
            eventHandler: function () {
                var shapes = layer.getPrimitives();
                
                var geoJson = JSON.stringify(Microsoft.Maps.GeoJson.write(shapes));

                var myWindow = window.open('', '_blank', 'scrollbars=yes, resizable=yes, width=400, height=100');
                myWindow.document.write(geoJson);
                myWindow.document.close();
            }
        }]
    });

    //Assign the infobox to a map instance.
    infobox.setMap(map);

}
