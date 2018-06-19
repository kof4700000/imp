function get_address_for_sys(url, element_id){	//��ȡ�û������˵�
	  $.get(url, function(data, status){
	  	//alert(data[0].user)
	  	for (var i = 0;i < data.length; i++){
				var opt = document.createElement("option");
				opt.innerHTML = data[i].display_name;
				document.getElementById(element_id).appendChild(opt);
			};
		});
}

/*function get_system(url, page_num, page_size){	//��ȡ�û�ϵͳ
	//ͨ�����̨�����������Ʒ��ص�����
	//���ַ��������ں�̨�������ݽ϶�ʱ
	  $.get(url, {"page_num":page_num, "page_size":page_size},function(data, status){
	  	for (var i = 0;i < data.length; i++){
				var tr = document.createElement("tr");
				tr.innerHTML = "<td>" + data[i].short_name + "</td>";
				document.getElementById("system_table").appendChild(tr);
			};
		});
}*/

//��ȡ�û�ϵͳ
function InitialSysPage(url, page_size){
	$.get(url ,function(data, status){
		InitialPage("/system/get_system/", "pagination1", "system_table", data.max_count, page_size)
		})
	}

function add_ip_text(element_id){	//����IP
	  var opt = "";
	  opt = "<div class=\"input-group col-xs-8\">";
	  opt = opt + "<div class=\"input-group-addon\"><i class=\"fa fa-laptop\"></i></div>";
	  opt = opt + "<input type=\"text\" name=\"IP\" class=\"form-control\" data-inputmask=\"\'alias\': \'ip\'\" data-mask>";
	  opt = opt + "<div class=\"input-group-btn\">";
	  opt = opt + "<button type=\"button\" class=\"btn btn-danger\" onclick=\"delete_ip_text(this)\">DELETE</button></div>";
	  opt = opt + "</div>";
		//document.getElementById("IP_group").innerHTML+=opt;//ʹ��innerHTMLʱ��ÿ�ε����ťTEXT�е����ݶ�����ʧ
		//$("#IP_group").append(opt);		//ʹ��jq��append�򲻻�
		$(element_id).append(opt);		//ʹ��jq��append�򲻻�
}

function delete_ip_text(dom){	//ɾ��IP
		//���ô˺�����HTML��<button type="button" class="btn btn-danger" onclick="delete_ip_text(this)">DELETE</button>
		//delete_ip_text(this)�е�this���������ǵ�ǰԪ�أ���˽��䴫�뺯����
		//�ں�����ʹ��$(this)�Ϳ���ѡȡ�����Ԫ�أ�������onclick��Ԫ�أ�
		$(dom).parent().parent().remove();
}

function add_system(url){
	var hosts = []
	//jquery�������Ľ�������飬�����е�Ԫ����HTMLElement
	//��ÿ������Ԫ��ʹ�ö�HTMLElement�ķ������в���
	for (var i=0;i<$("#IP_group").find("input").length;i++)
	{
		hosts[i] = $("#IP_group").find("input")[i].value
		}

	var sys_detail = {
		"full_name":$("#full_name").val(),
		"short_name":$("#short_name").val(),
		"A":$("#A_role_for_sys").val(),
		"B":$("#B_role_for_sys").val(),
		"hosts":hosts
		}
	$.post(url, sys_detail, function(data,status){
		})
}

function edit_system(url){
	var hosts = []
	//jquery�������Ľ�������飬�����е�Ԫ����HTMLElement
	//��ÿ������Ԫ��ʹ�ö�HTMLElement�ķ������в���
	for (var i=0;i<$("#IP_group").find("input").length;i++)
	{
		hosts[i] = $("#IP_group").find("input")[i].value
		}

	var sys_detail = {
		"action":"EDIT",
		"full_name":$("#full_name").val(),
		"short_name":$("#short_name").val(),
		"A":$("#A_role_for_sys").val(),
		"B":$("#B_role_for_sys").val(),
		"hosts":hosts
		}
	
	//$.postʱ�����غ�������ִ��
	/*ʹ��$.ajax������POST���������غ���������error��
	��error��alert(XMLHttpRequest.status)������statusΪ0
	��error��alert(XMLHttpRequest.readyState)������readyStateΪ0
	��ʱ����ajaxΪ�첽���󣬽����Ϊͬ�����󣬸�Ϊͬ��������ȷ����success*/
	/*$.post(url, sys_detail, function(data,status){
		alert(data)
		});*/
	$.ajax({
		url:url,
		data:sys_detail,
		dataType:'json',
		type:'POST',
		async:false,
		success:function(data){
			if (data.success == 1){
		window.location.replace("/system/");
		/*window.location.replace("/system/")ʱ��Ҫע��ǰ���ύbutton��type
		��������ʹ�õ���ͬ��ajax�����button��type="submit"�����������ǵ����
		submit��ť��Ȼ��ajaxִ�У���ajaxͬ��ִ�лص�������ִ����ת��ʵ�ʽ�����
		��ת��Ȼ��ajax����ˣ���֮�������submit���ύ������ʱҳ���ִ���ת
		���ҳ������ִ��submit��ҳ�档������������һ�ַ��������ǲ��ڻص�������
		������ת������form��������ת��ַ��<form action=url>
		����submit��ɺ�Ϳ�����ת����Ҫ��ҳ�棬�������ַ�������Զ��ת��ָ����ַ
		�ص�������ʹ��return true/false������ת�����ã�������*/
		/*�����ajax��ͬ�������У�ʹ��django����render���ؿ�����ajax������
		���ص����ݽ��д�������������һ�ɲ�����������*/
		/*����һ�ַ������ǽ�button��type���button����submit�������ڻص�������
		�Ϳ���������ʹ����ת��*/
		//return false;
		}
		},
		error:function(XMLHttpRequest, textStatus, errorThrown){
			//alert(XMLHttpRequest.status)
			//alert(XMLHttpRequest.readyState)
		},/*
		complete:function(data){
			alert(data)
		},*/

	});

}

function get_ip_for_sys(){
	
}