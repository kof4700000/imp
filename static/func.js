/*<script>		//jQuery get data
	$(document).ready(function(){
		$.get("get_address", function(data,status){
			var test1 = data.address;
			});
		});
		</script> */
function get_data(url){	//��ȡ�û������˵�
	//���ﱻ����һ����ģ�jquery��.get����Ĭ��ʹ�õ����첽ajax������ֻ���ں����ڲ�ʹ��data
	//���return dataʱ���ⲿ��ȡ��ֵΪ��
	//�����ⲿ��ȡdata�Ļ���������ajax�����
	//ͬ��ajax����һ�����ִ����ɺ��ִ����һ��
	//�첽ajax��������һ�����ִ����ֱ��ִ����һ��
	/*var resp = 
	  $.get(url, function(data, status){
			return data.address;
		});
	alert(resp);	//ע��������Ϊ���첽ajax������ʲô��ȡ����
	*/
	//�����븴�����get_data��������ʱ��һ�£�֮��ͨ��ͬ��ajaxʵ��
  return "test";
}
