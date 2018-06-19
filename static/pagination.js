//This is for paging.
//�Ӻ�̨ȡ���е����ݣ�Ȼ����JS������ҳ
//���ַ��������ں�̨�������ݽ���ʱ
//�ŵ������̨�����С
function InitPage(){
	var table = document.getElementById("address_table");
	var num = table.rows.length;
	var total_page = 0;
	var current_page = 1;
	var pageSize = 20;
	if (num/pageSize > parseInt(num/pageSize)){	
		//��ʹ��parseInt��num/pageSize���������õ�С����ʹ��parseInt��num/pageSizeΪ����
		total_page = parseInt(num/pageSize) + 1;
	}
	else{
		total_page = parseInt(num/pageSize);
	}
	for (var i = 1;i <= total_page; i++)
	{
		var li = document.createElement("li");
		//li.innerHTML = "<a href=\"" + i +"\">" + i + "</a>";
		li.innerHTML = "<a onclick=\"" + "toPage(" + i + ")" +"\">" + i + "</a>";
		//alert(li.innerHTML)
		document.getElementById("pagination1").appendChild(li);
	}
	toPage(1);
}

function toPage(page_num){
	var table = document.getElementById("address_table");
	var num = table.rows.length;
	var total_page = 0;
	var current_page = 1;
	var pageSize = 20;
	var start_row = (page_num - 1)* pageSize + 1;
	var end_row = start_row + pageSize - 1;
	for (var i = 1; i <= num; i ++)
	{
		var table_row = table.rows[i];
		if ((i >= start_row) && (i <= end_row)){
			table_row.style.display="table-row";
		}
		else{
			table_row.style.display="none";
		}
	}
	
}

function showAll(){
	var table = document.getElementById("address_table");
	for (var i = 1; i <= table.rows.length;i++)
	{
		var table_row = table.rows[i];
		table_row.style.display="table-row";
	}
}

//�����Ǻ�̨��ҳ��ȡ���ݷ���
//��ʼ����ҳ��������,urlΪȡ����url, element_idΪ��ҳ��ťID, max_countΪ���ݸ���
function InitialPage(url, element_id, table_id, max_count, page_size){
	var num = max_count;
	var total_page = 0;
	//var current_page = page_num;
	var pageSize = page_size;
	if (num/pageSize > parseInt(num/pageSize)){	
		//��ʹ��parseInt��num/pageSize���������õ�С����ʹ��parseInt��num/pageSizeΪ����
		total_page = parseInt(num/pageSize) + 1;
	}
	else{
		total_page = parseInt(num/pageSize);
	}
	for (var i = 1;i <= total_page; i++)
	{
		var li = document.createElement("li");
		//li.innerHTML = "<a href=\"" + i +"\">" + i + "</a>";
		li.innerHTML = "<a onclick=\""+ "To_Page('" + url + "','" + table_id + "'," + i + "," + page_size + "," + 1 + ")" +"\">" + i + "</a>";
		document.getElementById(element_id).appendChild(li);
	}
	To_Page(url, table_id, 1, page_size, "test");
}

//��ҳ��������
//code_blockΪ������ݲ��ֵ�html�飬���벻ͬhtml���Ը���
function To_Page(url, element_id, page_num, page_size, code_block){
	//ͨ�����̨�����������Ʒ��ص�����
	//���ַ��������ں�̨�������ݽ϶�ʱ
	  $.get(url, {"page_num":page_num, "page_size":page_size},function(data, status){
	  	var table_size = document.getElementById(element_id).rows.length;
	  	for (var i = table_size - 1;i > 0; i--){
	  		//ɾ������ͷ������ԭ������
	  		document.getElementById(element_id).deleteRow(i);
	  	}
	  	for (var i = 0;i < data.length; i++){
				var tr = document.createElement("tr");
				tr.innerHTML = "<td>" + data[i].full_name + "</td>";
				tr.innerHTML += "<td>" + data[i].short_name + "</td>";
				tr.innerHTML += "<td>" + data[i].A_role + "</td>";
				tr.innerHTML += "<td>" + data[i].B_role + "</td>";
				var IP_selection = "";
				for (var j = 0;j < data[i].ip.length; j++){
					IP_selection += "<li>" + data[i].ip[j] + "</li>"
				}
				tr.innerHTML += "<td><div class=\"btn-group-vertical\"><div class=\"btn-group\"><button type=\"button\" class=\"btn btn-default dropdown-toggle\" data-toggle=\"dropdown\"><span class=\"caret\"></span></button><ul class=\"dropdown-menu\">" + IP_selection; //"<li><a href=\"#\">Dropdown link</a></li>"
				tr.innerHTML += "</ul></div></div></td>";
				//tr.innerHTML += "<td>" + "<button onclick=\"get_sys_detail('"+ data[i].full_name + "')\">detail" + "</td>";
				tr.innerHTML += "<td>" + "<a href=\"/system/edit/" + data[i].short_name + "\">EDIT</a>" + "</td>";
				document.getElementById(element_id).appendChild(tr);
			};
		});
}