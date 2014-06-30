from django import template

register = template.Library()


@register.filter(name='reemplaza')
def reemplaza(cadena):
    valores = {'datos':'Registro','fmedica':'Ficha medica','fdental':'Ficha dental','rayosx':'Rayos X'}
    devolver = ''
    try:
        devolver = valores[cadena]
    except:
        devolver = cadena.title()
    return devolver
