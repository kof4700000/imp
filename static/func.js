/*<script>		//jQuery get data
	$(document).ready(function(){
		$.get("get_address", function(data,status){
			var test1 = data.address;
			});
		});
		</script> */
function get_data(url){	//获取用户下拉菜单
	//这里被坑了一个大的，jquery的.get方法默认使用的是异步ajax，所以只能在函数内部使用data
	//因此return data时，外部获取的值为空
	//想在外部获取data的话，还是用ajax请求吧
	//同步ajax：上一条语句执行完成后才执行下一句
	//异步ajax：不等上一条语句执行完直接执行下一句
	/*var resp = 
	  $.get(url, function(data, status){
			return data.address;
		});
	alert(resp);	//注意这里因为是异步ajax，所以什么都取不到
	*/
	//本来想复用这个get_data方法，暂时放一下，之后通过同步ajax实现
  return "test";
}

