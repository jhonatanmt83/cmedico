//Actualizar analisis de acuerdo a la ecografia seleccionada
function obtener_analisis()
{
    var cadena='id_ecografia';
    $.getJSON('/ecografia/obtener_analisis/'+
			document.getElementById(cadena).value,
            function(data){ actualizar_combo_analisis(data);});
}

//Actualiza el combo analisis con los datos obtenidos del ajax
function actualizar_combo_analisis(data)
{
    $('#id_eco_analisis').empty(); //elimino el cotenido actual del combo

    // agrego los tipos obtenidos por ajax
    $.each(data, function(index, analisis){
      $('<option value="' + analisis['id'] + '">' +
                            analisis['nombre'] + '</option>')
      .appendTo('#id_eco_analisis');
   });
}