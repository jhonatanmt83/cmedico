//Actualizar provincia segun la region elegida
//al terminar actualiza tambien distrito
function obtener_analisis()
{
    var cadena='id_muestra';
    $.getJSON('/laboratorio/obtener_analisis/'+
			document.getElementById(cadena).value,
            function(data){ actualizar_combo_analisis(data);});
}

//Actualiza el combo distritos con los datos obtenidos del ajax
function actualizar_combo_analisis(data)
{
    $('#id_analisis').empty(); //elimino el cotenido actual del combo

    // agrego los tipos obtenidos por ajax
    $.each(data, function(index, analisis){
      $('<option value="' + analisis['id'] + '">' +
                            analisis['nombre'] + '</option>')
      .appendTo('#id_analisis');
   });
}