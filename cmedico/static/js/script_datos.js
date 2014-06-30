function numero_historia(){
	var tipo=$('#paciente_select').val();
	$.getJSON('/numero_historia/'+tipo,function(data){
		$.each(data, function(index, nros){
            $('#nro_historia').val(nros["numero"]);
		});
	});
}