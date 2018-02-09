function arrCopy(arr) {
	l = arr.length;
	return arr.slice(0,l);
}

function distance(pa,pb) {
	//document.getElementById('output').innerHTML = pa + pb;
	var dx = pa[0] - pb[0];
	var dy = pa[1] - pb[1];
	return Math.sqrt(dx*dx+dy*dy);
}

function areaUnionFor2(polya,polyb) {
	//document.getElementById('output').innerHTML += polya.length + ' '+ polyb.length + ',';

	var EPS = 1e-4;

	polya.pop();
	polyb.pop();

	var la = polya.length;
	var lb = polyb.length;

	var psta = 0;
	
	var maxDis = distance(polya[0],polyb[0]);
	for (var i = 0;i < la; i++)
		for (var j = 0;j < lb; j++) {
			var disab = distance(polya[i],polyb[j])
			if (disab > maxDis) {
				maxDis = disab;
				psta = i;
			}
		}
	polya = polya.slice(psta,la).concat(polya.slice(0,psta));
	

	var listDis = new Array();
	for (var i = 0;i < la; i++)
		for (var j = 0;j < lb; j++) 
			listDis[i*lb+j] = new Array(i,j,distance(polya[i],polyb[j]));
	
 	listDis.sort(function(a,b){return (a[2]-b[2]);});
 	

	var lista = arrCopy(polya);
	var listb = polyb.concat(polyb);

	var stand = listDis[0][2] + EPS;
	var phi = 3.0;

	var kend = listDis.length
	for (var k = 0;k < listDis.length; k++)
		if (listDis[k][2] >= phi*stand) {
			kend = k;
			break;
		}
	
	var listPoint = new Array();
	for (var i = 0;i < kend; i++) {
		listPoint[i] = new Array(listDis[i][0],listDis[i][1]);
	}

	var p = new Array(listPoint[0],listPoint[1]);
	if (p[0][0] > p[1][0]) {
		var t = arrCopy(p[0]);p[0] = arrCopy(p[1]);p[1] = arrCopy(t);
	}
	var mp =  0;
	
	for (var i = 0;i < kend; i++)
		for (var j = i+1;j < kend; j++) {
			var c1 = arrCopy(listPoint[i]);
			var c2 = arrCopy(listPoint[j]);
			if (c1[0] == c2[0] || c1[1] == c2[1]) continue;
			
			if (c1[0] > c2[0]) {
				var t = arrCopy(c1);c1 = arrCopy(c2);c2 = arrCopy(t);
			}
			var figp = (c2[0] - c1[0]) + (c1[1] - c2[1]+lb)%lb;
			if ((c2[0] - c1[0]) + (c1[1] - c2[1]+lb)%lb > mp && (c1[1] - c2[1]+lb)%lb < (c2[1] - c1[1]+lb)%lb) {
				mp = (c2[0] - c1[0]) + (c1[1] - c2[1]+lb)%lb;
				p = new Array(c1,c2);
			}
		}
	var x1 = p[0][0];var y1 = p[0][1];
	var x2 = p[1][0];var y2 = p[1][1];

	var poly = new Array();
	if (y2 > y1) 
		poly = lista.slice(0,x1+1).concat(listb.slice(y1,y2+1),lista.slice(x2,la),new Array(lista[0]));
	else
		poly = lista.slice(0,x1+1).concat(listb.slice(y1,y2+lb+1),lista.slice(x2,la),new Array(lista[0]));
	
	//document.getElementById('output').innerHTML += poly.length + '|';
	
	
	return poly;
	//return polya;
}

function areaUnion(shapes) {;
	var data = arrCopy(shapes.features);
	var unionPoly = data[0];
	for (var i = 1;i < data.length;i++)
		unionPoly.geometry.coordinates[0] = areaUnionFor2(unionPoly.geometry.coordinates[0],data[i].geometry.coordinates[0])
	
	return unionPoly;
}

