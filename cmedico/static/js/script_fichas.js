$(function(){
$("#formulario").submit( function () {
    $('#id_nro_historia').removeAttr('disabled');
    return true;
    
});
});