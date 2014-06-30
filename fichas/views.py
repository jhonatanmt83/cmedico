# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
#from django.utils import simplejson
import json
from django.views.decorators.csrf import csrf_exempt

from fichas.models import Datos, Ecot, Itemeco, Odontograma, DetalleOdontograma, Paciente, Ecografia, Laboratorio
from fichas.models import Fmedica, Fdental, Enfermeria, Tratamiento, Laboratorio, RayosX, Registro, Muestra, Analisis
#from fichas.models import Doctor

#importacion de formularios
from fichas.forms import formingreso, DatosForm, FmedicaForm, FdentalForm, EnfermeriaForm, TratamientoForm, LaboratorioForm, RayosXForm, DatosEnfermeria, RayxForm, EcografiaForm
#from ficha.forms import DoctorForm

import datetime


#logeo
def ingreso(request):
    mensaje = ''
    if request.method == 'POST':
        formu = formingreso(request.POST)
        usuariologin = request.POST['usuario']
        passlogin = request.POST['clave']
        acceso = authenticate(username=usuariologin, password=passlogin)
        if acceso is not None:
            if acceso.is_active:
                login(request, acceso)
                if request.GET:
                    return HttpResponseRedirect(request.GET['next'])
                return HttpResponseRedirect('/')
            else:
                mensaje = 'El usuario a sido desabilitado'
        else:
            mensaje = 'Usuario y/o contraseña incorrectos. Por favor intente otra vez.'
    else:
        formu = formingreso()
    return render_to_response('ingreso.html', {'formu': formu, 'mensaje': mensaje}, context_instance=RequestContext(request))


def salida(request):
    logout(request)
    return HttpResponseRedirect('/')
#end logeo


def operaciones(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/ingreso/')
    return render_to_response('operaciones.html', {}, context_instance=RequestContext(request))


def registrar(request):
    return render_to_response('registrar.html', {}, context_instance=RequestContext(request))


def  medicamentos(request):
    return render_to_response('medicamentos.html', {})


@login_required
def datos(request):
    mensaje = ''
    actualizar = 'no'
    if request.method == 'POST':
        if 'buscado' in request.POST:
            #registros = Registro.objects.filter(datos__nro_historia__contains=request.POST['num_historia'], enfermeria__isnull=True)
            #return render_to_response('enfermeria.html', {'registros': registros, 'buscado': 'yes'}, context_instance=RequestContext(request))
            try:
                instancia = Datos.objects.get(pk=request.POST['buscado'])
                formr = DatosForm(instance=instancia)
                actualizar = 'si'
            except:
                formr = DatosForm()
                mensaje = 'No se encontro dato.'
            return render_to_response('datos.html', {'formr': formr, 'mensaje': mensaje, 'actualizar': actualizar}, context_instance=RequestContext(request))
        try:
            post_act = request.POST['actualizar']
        except:
            post_act = ''
        if post_act != 'si':
            formr = DatosForm(request.POST)
        else:
            instancia = Datos.objects.get(pk=request.POST['nro_historia'])
            formr = DatosForm(request.POST, instance=instancia)
        if formr.is_valid():
            dato = formr.save()
            registro = Registro(datos=dato)
            registro.save()
            return HttpResponseRedirect('/operaciones')
    else:
        formr = DatosForm()
    return render_to_response('datos.html', {'formr': formr}, context_instance=RequestContext(request))


@login_required
def fmedica(request):
    formulario2 = DatosEnfermeria()
    if request.method == 'POST':
        if 'num_historia' in request.POST:
            registros = Registro.objects.filter(datos__nro_historia__contains=request.POST['num_historia'], fmedica__isnull=True, enfermeria__atencion_medica=True)
            return render_to_response('fmedica.html', {'registros': registros, 'buscado': 'yes'}, context_instance=RequestContext(request))
        formrm = FmedicaForm(request.POST)
        if formrm.is_valid():
            formrm.save()
            return HttpResponseRedirect('/operaciones/')
    else:
        formrm = FmedicaForm()
    return render_to_response('fmedica.html', {'formrm': formrm, 'formulario_datos': formulario2}, context_instance=RequestContext(request))


@login_required
def fmedica_buscado(request, historiac):
    registros = Registro.objects.filter(datos__nro_historia=historiac, fmedica__isnull=True)
    registro = registros.order_by('-fecha')[0]
    formulario2 = DatosEnfermeria(instance=registro.enfermeria)
    historia_c = get_object_or_404(Datos, pk=historiac)
    instancia = Fmedica(nro_historia=historia_c)
    formrr = RayxForm()
    if request.method == 'POST':
        formrm = FmedicaForm(request.POST)
        if formrm.is_valid():
            formu_fmed = formrm.save()
            registros = Registro.objects.filter(datos__nro_historia=request.POST['nro_historia'], fmedica__isnull=True)
            registro = registros.order_by('-fecha')[0]
            registro.fmedica = formu_fmed
            registro.save()
            return HttpResponseRedirect('/operaciones/')
    else:
        formrm = FmedicaForm(instance=instancia)
    return render_to_response('fmedica.html', {'formrm': formrm, 'formulario_datos': formulario2, 'formrr': formrr}, context_instance=RequestContext(request))


@login_required
def fdental(request):
    if request.method == 'POST':
        if 'num_historia' in request.POST:
            registros = Registro.objects.filter(datos__nro_historia__contains=request.POST['num_historia'], fdental__isnull=True)
            return render_to_response('fdental.html', {'registros': registros, 'buscado': 'yes'}, context_instance=RequestContext(request))
        formrd = FdentalForm(request.POST)
        if formrd.is_valid():
            formrd.save()
            return HttpResponseRedirect('/operaciones/')
    else:
        formrd = FdentalForm()
    return render_to_response('fdental.html', {'formrd': formrd}, context_instance=RequestContext(request))


@login_required
def fdental_buscado(request, historiac):
    odontograma = ''
    historia_c = get_object_or_404(Datos, pk=historiac)
    odont = Odontograma.objects.filter(nro_historia=historia_c)
    if len(odont) > 0:
        odontograma = odont[0]
    instancia = Fdental(nro_historia=historia_c)
    if request.method == 'POST':
        formrd = FdentalForm(request.POST)
        if formrd.is_valid():
            formu_d = formrd.save()
            registros = Registro.objects.filter(datos__nro_historia=request.POST['nro_historia'], fdental__isnull=True)
            registro = registros.order_by('-fecha')[0]
            registro.fdental = formu_d
            registro.save()
            return HttpResponseRedirect('/operaciones/')
    else:
        formrd = FdentalForm(instance=instancia)
    return render_to_response('fdental.html', {'formrd': formrd, 'odontograma': odontograma, 'historia_c': historia_c}, context_instance=RequestContext(request))


@login_required
def fdental_odontograma(request, historiac):
    historia_c = get_object_or_404(Datos, pk=historiac)
    odont = []
    odont = Odontograma.objects.filter(nro_historia=historia_c)
    acciones = []
    if len(odont) > 0:
        odont = odont[0]
        acciones = DetalleOdontograma.objects.filter(odontograma=odont)
    return render_to_response('odontograma.html', {'odontograma': odont, 'acciones': acciones}, context_instance=RequestContext(request))


@login_required
def fdental_odontograma_crear(request, historiac):

    historia_c = get_object_or_404(Datos, pk=historiac)
    if len(Odontograma.objects.filter(nro_historia=historia_c)) == 0:
        new_odont = Odontograma(nro_historia=historia_c, observaciones='')
        new_odont.save()
        return HttpResponseRedirect('/operaciones/odontograma/' + str(historia_c.pk))
    #return render_to_response('odontograma.html', {'odontograma': odont, 'acciones': acciones}, context_instance=RequestContext(request))


@login_required
def accion_odontograma(request, tipo, odontograma, diente1, seccion, accion, fecha, diente2):
    odont = Odontograma.objects.get(pk=odontograma)
    if int(tipo) == 1:
        new_det = DetalleOdontograma(odontograma=odont, diente=diente1, seccion=seccion, accion=accion, fecha=fecha, diente2=diente2)
        new_det.save()
    elif int(tipo) == 2:
        det = DetalleOdontograma.objects.filter(odontograma=odont, diente=diente1, seccion=seccion, accion=accion, fecha=fecha, diente2=diente2)
        print det
        if len(det) > 0:
            det = det[0]
            det.delete()
            #det.save()
    resultado = [{}]
    return HttpResponse(json.dumps(resultado))


@login_required
def enfermeria(request):
    if request.method == 'POST':
        if 'num_historia' in request.POST:
            registros = Registro.objects.filter(datos__nro_historia__contains=request.POST['num_historia'], enfermeria__isnull=True)
            return render_to_response('enfermeria.html', {'registros': registros, 'buscado': 'yes'}, context_instance=RequestContext(request))
        formre = EnfermeriaForm(request.POST)
        if formre.is_valid():
            formre.save()
            return HttpResponseRedirect('/operaciones/')
    else:
        formre = EnfermeriaForm()
    return render_to_response('enfermeria.html', {'formre': formre}, context_instance=RequestContext(request))


@login_required
def enfermeria_buscado(request, historiac):
    historia_c = get_object_or_404(Datos, pk=historiac)
    instancia = Enfermeria(nro_historia=historia_c)
    if request.method == 'POST':
        formre = EnfermeriaForm(request.POST)
        if formre.is_valid():
            formu_enf = formre.save()
            if 'ingresar2' in request.POST:
                formu_enf.atencion_medica = True
                formu_enf.save()
            registros = Registro.objects.filter(datos__nro_historia=request.POST['nro_historia'], enfermeria__isnull=True)
            registro = registros.order_by('-fecha')[0]
            registro.enfermeria = formu_enf
            registro.save()
            return HttpResponseRedirect('/operaciones/')
    else:
        formre = EnfermeriaForm(instance=instancia)
    return render_to_response('enfermeria.html', {'formre': formre}, context_instance=RequestContext(request))


@login_required
def tratamiento(request):
    if request.method == 'POST':
        formr = TratamientoForm(request.POST)
        if formr.is_valid():
            formr.save()
            return HttpResponseRedirect('/operaciones')
    else:
        formr = TratamientoForm()
    return render_to_response('tratamiento.html', {'formr': formr}, context_instance=RequestContext(request))


@login_required
def laboratorio(request):
    if request.method == 'POST':
        formrl = LaboratorioForm(request.POST)
        if formrl.is_valid():
            formrl.save()
            return HttpResponseRedirect('/operaciones')
    else:
        formrl = LaboratorioForm()
    return render_to_response('laboratorio.html', {'formrl': formrl}, context_instance=RequestContext(request))


@login_required
def reportes(request):
    pacientes = Paciente.objects.all()
    diccio = {'pacientes': pacientes}
    return render_to_response('reportes.html', {'datos': diccio, }, context_instance=RequestContext(request))


@login_required
def reporte_paciente(request, paciente):
    tipo_paciente = Paciente.objects.get(pk=paciente)
    datos_pacientes = Datos.objects.filter(paciente=tipo_paciente)
    diccio = {'pacientes': datos_pacientes}
    return render_to_response('reportes_paciente.html', {'datos': diccio, }, context_instance=RequestContext(request))


@login_required
def reporte_detalle(request, historiac):
    historia_c = Datos.objects.get(pk=historiac)
    fmedica = Fmedica.objects.filter(nro_historia=historia_c)
    fdental = Fdental.objects.filter(nro_historia=historia_c)
    rayosx = RayosX.objects.filter(nro_historia=historia_c)
    ecografia = Ecografia.objects.filter(nro_historia=historia_c)
    laboratorio = Laboratorio.objects.filter(nro_historia=historia_c)
    diccio = {'fmedica': fmedica, 'fdental': fdental, 'rayosx': rayosx, 'ecografia': ecografia, 'laboratorio': laboratorio}
    return render_to_response('reportes_detalle.html', {'datos': diccio, }, context_instance=RequestContext(request))


@login_required
def reporte_detallado(request, ficha, id_ficha):
    ficha_dev = []
    ficha_id = id_ficha
    if ficha == '1':
        ficha_dev = Fmedica.objects.get(pk=ficha_id)
    elif ficha == '2':
        ficha_dev = Fdental.objects.get(pk=ficha_id)
    elif ficha == '3':
        ficha_dev = RayosX.objects.get(pk=ficha_id)
    elif ficha == '4':
        ficha_dev = Ecografia.objects.get(pk=ficha_id)
    elif ficha == '5':
        ficha_dev = Laboratorio.objects.get(pk=ficha_id)
    diccio = {'ficha': ficha, 'ficha_dev': ficha_dev}
    print {'datos': diccio}
    return render_to_response('reportes_detallado.html', {'datos': diccio}, context_instance=RequestContext(request))


@login_required
def reportes_mes(request):
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Setiembre', 'Octubre', 'Noviembre', 'Diciembre']
    mes_actual = datetime.datetime.now().month
    nombre_mes = meses[mes_actual - 1]
    #atenciones = []
    usuarios_atendidos = []
    enf_atn = Enfermeria.objects.filter(fconsulta__month=mes_actual)
    total_atenciones = len(enf_atn)

    diccio = {}
    #print atenciones
    return render_to_response('reportes.html', {'datos': diccio, 'total': total_atenciones, 'nombre_mes': nombre_mes, 'usuarios_atendidos': usuarios_atendidos}, context_instance=RequestContext(request))


@login_required
def detalles(request, historiac):
    mes_actual = datetime.datetime.now().month
    atenciones = []
    ficha1 = Fmedica.objects.filter(fconsulta__month=mes_actual)
    for ficha in ficha1: atenciones.append(ficha)
    ficha1 = Fdental.objects.filter(fconsulta__month=mes_actual)
    for ficha in ficha1: atenciones.append(ficha)
    ficha1 = Enfermeria.objects.filter(fconsulta__month=mes_actual)
    for ficha in ficha1: atenciones.append(ficha)
    ficha1 = Tratamiento.objects.filter(fconsulta__month=mes_actual)
    for ficha in ficha1: atenciones.append(ficha)
    ficha1 = Laboratorio.objects.filter(fconsulta__month=mes_actual)
    for ficha in ficha1: atenciones.append(ficha)
    ficha1 = RayosX.objects.filter(fconsulta__month=mes_actual)
    for ficha in ficha1: atenciones.append(ficha)
    return render_to_response('detalles.html', {'atenciones': atenciones, }, context_instance=RequestContext(request))


def numero_historia(request, tipo):
    largo = 5
    listado_tipo = {'1': 'E', '2': 'D', '3': 'A', '4': 'P'}
    resultado = []
    datos = Datos.objects.filter(paciente__pk=int(tipo)).order_by('-nro_historia')
    if len(datos) > 0:
        nro = datos[0].nro_historia
        nro = int(nro[1:]) + 1
        nro = listado_tipo[tipo] + ("0" * (largo - len(str(nro)))) + str(nro)
    else:
        nro = listado_tipo[tipo] + "0" * (largo - 1) + "1"
    resultado = [{'numero': nro}]
    return HttpResponse(json.dumps(resultado))


def obtener_analisis(request, examen):
    """Devuelve los analisis de un examen determinado para ser utilizados por el js"""
    examen = Muestra.objects.get(pk=int(examen))
    analisis_all = Analisis.objects.filter(examen=examen)
    #analisis_all = analisis_all.order_by('nombre')

    resultado = []
    for analisis in analisis_all:
        datos = {}
        datos['id'] = analisis.pk
        datos['nombre'] = analisis.nombre
        resultado.append(datos)

    return HttpResponse(json.dumps(resultado))


@login_required
def placas(request):
    return render_to_response('placas.html', {}, context_instance=RequestContext(request))


@login_required
def receta(request):
    ficha_dev = ''
    registro = ''
    ficha_enfermeria = ''
    consultado = ''
    historia_c = ''
    if request.method == 'POST':
        historiac = request.POST['num_historia']
        historia_c = get_object_or_404(Datos, pk=historiac)
        registros = Registro.objects.filter(datos=historia_c)
        if registros:
            consultado = 'yes'
            registro = registros.order_by('-fecha')[0]
            ficha_enfermeria = registro.enfermeria
            ficha_medica = registro.fmedica
            ficha_dental = registro.fdental
            if ficha_medica:
                ficha_dev = ficha_medica
            elif ficha_dental:
                ficha_dev = ficha_dental
    return render_to_response('receta.html', {'historia_c': historia_c, 'ficha': ficha_dev, 'enfermeria': ficha_enfermeria, 'consultado': consultado}, context_instance=RequestContext(request))
    #return render_to_response('fdental.html', {'formrd': formrd}, context_instance=RequestContext(request))


@login_required
def rayosx(request):
    if request.method == 'POST':
        formrr = RayxForm(request.POST)
        if formrr.is_valid():
            formrr.save()
            return HttpResponseRedirect('/operaciones')
    else:
        formrr = RayxForm()
    return render_to_response('rayosx.html', {'formrr': formrr}, context_instance=RequestContext(request))


@login_required
def ecografia(request):
    if request.method == 'POST':
        formeco = EcografiaForm(request.POST)
        if formeco.is_valid():
            formeco.save()
            return HttpResponseRedirect('/operaciones')
    else:
        formeco = EcografiaForm()
    return render_to_response('ecografia.html', {'formeco': formeco}, context_instance=RequestContext(request))


def obtener_analisis_ecografia(request, examen):
    """Devuelve los analisis de un examen determinado para ser utilizados por el js"""
    examen = Ecot.objects.get(pk=int(examen))
    analisis_all = Itemeco.objects.filter(codecot=examen)
    #analisis_all = analisis_all.order_by('nombre')

    resultado = []
    for analisis in analisis_all:
        datos = {}
        datos['id'] = analisis.pk
        datos['nombre'] = analisis.nombre
        resultado.append(datos)

    return HttpResponse(json.dumps(resultado))
