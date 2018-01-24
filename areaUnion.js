function distance(pa,pb) {
	var dx = pa[0] - pb[0];
	var dy = pa[1] - pb[1];
	return Math.sqrt(dx*dx+dy*dy);
}

function areaUnionFor2(polya,polyb) {
	var EPS = 1e-13;

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
 	

	var lista = polya;
	var listb = polyb.concat(polyb);

	var stand = listDis[0][2] + EPS;
	var phi = 2.0;

	var kend = listDis.length
	for (var k = 0;k < listDis.length; k++)
		if (listDis[k][2] >= phi*stand) {
			kend = k;
			break;
		}
	var listPoint = new Array();
	//document.getElementById('output').innerHTML = kend;
	for (var i = 0;i < kend; i++) {
		listPoint[i] = new Array(listDis[i][0],listDis[i][1]);
		//document.getElementById('output').innerHTML += '[' +  listPoint[i] + ']';
	}


	var p = new Array(listPoint[0],listPoint[1]);
	var mp =  (listDis[1][0]-listDis[0][0]) + (listDis[0][1]-listDis[1][1]+lb)%lb;
	
	for (var i = 0;i < kend; i++)
		for (var j = i+1;j < kend; j++) {
			var c1 = new Array(listPoint[i]);
			var c2 = new Array(listPoint[j]);
			
			if (c1[0] < c2[0]) {
				var t = new Array(c1);c1 = c2;c2 = t;
			}
			if ((c2[0] - c1[0]) + (c1[1] - c2[1]+lb)%lb > mp) {
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
	
	return poly;
}

function areaUnion() {
	var str = String(unionCnt);
    for (var i = 0;i < unionCnt;i++) {
        str += '[' + '[' + unionList[i][0][0] + ', ' + unionList[i][0][1] + ']'
        for (var j = 1;j < unionList[i].length; j++)
            str += ', [' + unionList[i][j][0] + ', ' + unionList[i][j][1] + ']'
        str += '],'
    }
    document.getElementById('output').innerHTML = str ;
	var unionPoly = areaUnionFor2(unionList[0],unionList[1])
	//for (var i = 1;i < unionCnt;i++)
	//	unionPoly = areaUnionFor2(unionPoly,unionList[i]);
	
	/*
	var str = '';
	for (var i = 0;i < unionPoly.length; i++)
		str += '[' + unionPoly[i][0] + ', ' + unionPoly[i][1] + '], '
	document.getElementById('output').innerHTML = '[' + str + '],';
	*/
}

