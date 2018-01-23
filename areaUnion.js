
function areaUnionFor2(lista,listb) {
	lista = lista.concat(lista,lista);
	listb = listb.concat(listb,listb);
	listDis = new Array();
	for (var i = 0;i < lista.length; i++) 
		for (var j = 0;j < listb.length; j++) {
			listDis.push()
		}
}

function areaUnion() {
	for (var i = 0;i < unionCnt-1;i++)
		unionList[i+1] = areaUnionFor2(unionList[i],unionList[i+1]);
	rlt = unionCnt-1;
	unionList.clear();
	unionCnt = 0;
	return rlt;
}

