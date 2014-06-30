# -*- coding: utf-8 -*-
from django.db import models
import datetime
# Create your models here.

#estudiantes administrativos docentes y proyeccion social


class Paciente(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='Tipo de paciente')

    def __unicode__(self):
        return self.nombre


class Facultad(models.Model):
    nombre = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nombre


class Semestre(models.Model):
    nombre = models.CharField(max_length=4)

    def __unicode__(self):
        return self.nombre


class Abceso(models.Model):
    nombre = models.CharField(max_length=13)

    def __unicode__(self):
        return self.nombre


class Datos(models.Model):
    paciente = models.ForeignKey(Paciente, verbose_name='Ocupacion')
    nro_historia = models.CharField(max_length=10, verbose_name='Numero de Historia Clinica', primary_key=True)
    codigo = models.CharField(max_length=11, verbose_name='Codigo de Matricula / DNI')
    apellidos = models.CharField(max_length=50, verbose_name='Apellidos')
    nombres = models.CharField(max_length=50, verbose_name='Nombres')
    genero = models.CharField(max_length=1, choices=(('M', 'Masculino'), ('F', 'Femenino')))
    edad = models.CharField(max_length=2, verbose_name='Edad')
    cargo = models.CharField(max_length=20, null=True, blank=True)
    facultad = models.ForeignKey(Facultad, verbose_name='Facultad')
    semestre = models.ForeignKey(Semestre, verbose_name='Semestre')
    anio = models.IntegerField(verbose_name='Año de ingreso a la UNCP')
    estadocivil = models.CharField(max_length=50, verbose_name='Estado civil')
    fnacimiento = models.DateField(verbose_name='Fecha nacimiento', auto_now_add=False)
    lnacimiento = models.CharField(max_length=20, verbose_name='Lugar de nacimiento')
    domicilio = models.CharField(max_length=20, verbose_name='Domicilio')
    fecha = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nro_historia


class Fmedica(models.Model):
    nro_historia = models.ForeignKey(Datos, verbose_name='Numero de Historia Clinica')
    fconsulta = models.DateTimeField(auto_now_add=True)
    antefam = models.TextField(verbose_name='Antecedentes Familiares', blank=True)
    anteper = models.TextField(verbose_name='Antecedentes Personales(Fisiologicos)', blank=True)
    patologico = models.CharField(max_length=50, verbose_name='Patologicos', blank=True)
    operaciones = models.CharField(max_length=50, verbose_name='Operaciones', blank=True)
    tabaco = models.CharField(max_length=1, choices=(('S', 'Si'), ('N', 'No'), ('O', 'Ocacionalmente')),  verbose_name='Tabaco', blank=True)
    alcohol = models.CharField(max_length=1, choices=(('S', 'Si'), ('N', 'No'), ('O', 'Ocacionalmente')),  verbose_name='Alcohol', blank=True)
    coca = models.CharField(max_length=1, choices=(('S', 'Si'), ('N', 'No'), ('O', 'Ocacionalmente')),  verbose_name='Coca', blank=True)
    cafe = models.CharField(max_length=1, choices=(('S', 'Si'), ('N', 'No'), ('O', 'Ocacionalmente')),  verbose_name='Cafe', blank=True)
    enfermedad = models.CharField(max_length=20, verbose_name='Tiempo de enfermedad actual', blank=True)
    forma_inicio = models.CharField(max_length=20, verbose_name='Forma de inicio', blank=True)
    anamnesis = models.CharField(max_length=20, verbose_name='Anamnesis', blank=True)
    # frecuencia_cardiaca = models.CharField(max_length=20, verbose_name='Frecuencia Cardiaca')
    # frecuencia_respiratoria = models.CharField(max_length=20, verbose_name='Frecuencia Respiratoria')
    # pulso = models.CharField(max_length=20, verbose_name='Pulso')
    # peso = models.CharField(max_length=20, verbose_name='Peso')
    # talla = models.CharField(max_length=20, verbose_name='Talla')
    # temperatura = models.CharField(max_length=20, verbose_name='Temperatura')
    # pa = models.CharField(max_length=20, verbose_name='P.A')
    general = models.TextField(verbose_name='Inspeccion General', blank=True)
    cabeza = models.TextField(verbose_name='Cabeza/cara', blank=True)
    cuello = models.TextField(verbose_name='Cuello', blank=True)
    torax = models.TextField(verbose_name='Torax', blank=True)
    pulmones = models.TextField(verbose_name='Pulmones', blank=True)
    corazon = models.TextField(verbose_name='Corazon', blank=True)
    abdomen = models.TextField(verbose_name='Abdomen', blank=True)
    bazo = models.TextField(verbose_name='Bazo', blank=True)
    colvertebral = models.TextField(verbose_name='Columna vertebral', blank=True)
    extremidad = models.TextField(verbose_name='Extremidades', blank=True)
    ugenital = models.TextField(verbose_name='Uro-Genital', blank=True)
    nervioso = models.TextField(verbose_name='Sistema Nervioso', blank=True)
    otro = models.TextField(verbose_name='Otros examenes', blank=True)
    diagnostico = models.TextField(verbose_name='Diagnostico', blank=True)
    tratamiento = models.TextField(verbose_name='Tratamiento', blank=True)
    especial = models.TextField(verbose_name='Examenes Especiales', blank=True)

    def __unicode__(self):
        return str(self.nro_historia)

    def tipo(self):
        return "medica"


class Fdental(models.Model):
    nro_historia = models.ForeignKey(Datos, verbose_name='Numero de Historia Clinica')
    fconsulta = models.DateTimeField(auto_now_add=True)
    higiene = models.CharField(max_length=1, verbose_name='Higiene Bucal', choices=(('B', 'Bueno'), ('R', 'Regular'), ('MA', 'Malo')))
    hiperemia = models.CharField(max_length=1, choices=(('A', 'Activa'), ('B', 'Pasiva')), blank=True)
    expo = models.BooleanField(verbose_name='Exposicion')
    calificacion = models.BooleanField(verbose_name='Calsificacion')
    muerta = models.CharField(max_length=1, choices=(('S', 'Supurada'), ('N', 'No supuruda')))
    condensacion = models.BooleanField(verbose_name='Condensacion')
    rarefaccion = models.BooleanField(verbose_name='Rarefaccion')
    quiste = models.BooleanField(verbose_name='Quiste')
    abceso = models.ForeignKey(Abceso, verbose_name='Abceso', blank=True)
    oclusion = models.BooleanField(verbose_name='Oclusion')
    limpia = models.CharField(max_length=1, choices=(('S', 'Si'), ('N', 'No')), blank=True)
    gingivitis = models.BooleanField(verbose_name='gingivitis')
    bolsas = models.BooleanField(verbose_name='Pericementoclacia')
    movilidad = models.BooleanField(verbose_name='Alveoclacia')
    estado = models.BooleanField(verbose_name='Estado Periapical')
    pronostico = models.BooleanField(verbose_name='Pronostico')
    perico = models.BooleanField(verbose_name='Pericoronaritis')
    atm = models.CharField(max_length=20, verbose_name='ATM', blank=True)
    otros = models.CharField(max_length=20, verbose_name='Otros', blank=True)
    protesis = models.CharField(max_length=20, verbose_name='Protesis', blank=True)
    tratamiento = models.TextField(verbose_name='Tratamiento')

    def __unicode__(self):
        return str(self.nro_historia)

    def tipo(self):
        return "dental"


class Doctor(models.Model):
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=1, choices=(('O', 'Odontologo'), ('M', 'Medico')))

    def __unicode__(self):
        return self.nombres


class Enfermeria(models.Model):
    nro_historia = models.ForeignKey(Datos, verbose_name='Numero de Historia Clinica')
    doctor = models.ForeignKey(Doctor, verbose_name='Doctor')
    fconsulta = models.DateTimeField(auto_now_add=True)
    #Intervenciones
    curacion = models.BooleanField('Curacion de heridas')
    puntos = models.BooleanField('Retiro de puntos')
    cirugia = models.BooleanField('Cirugia menor')
    venda = models.BooleanField('Vendajes')
    oxi = models.BooleanField('Terapia con Oxigeno')
    #Administracion de Farmacos por via parenteral
    intramuscular = models.BooleanField()
    endovenoso = models.BooleanField()
    subcutanea = models.BooleanField()
    #Administracion de medicamentos por via local
    #local = models.CharField(max_length=30, verbose_name='via Local')
    #Administracion de medicamentos por via oral
    oral = models.CharField(max_length=30, verbose_name='via Oral', blank=True)
    #Administracion de medicamentos por via nasal
    tapon = models.BooleanField(verbose_name='Taponamiento nasal')
    #Tisioneumologia al paciente y seguimiento.
    tisio = models.TextField(verbose_name='Tisioneumologia (Sintomatico Respiatorio TBC)', blank=True)
    #Lectura de opto tipo
    opto = models.TextField(verbose_name='Opto Tipo', blank=True)
    ref = models.CharField(max_length=20, verbose_name='Referencia Hospitales', blank=True)
    #Datos para Ficha Medica
    frecuencia_cardiaca = models.CharField(max_length=20, verbose_name='Frecuencia Cardiaca', blank=True)
    frecuencia_respiratoria = models.CharField(max_length=20, verbose_name='Frecuencia Respiratoria', blank=True)
    pulso = models.CharField(max_length=20, verbose_name='Pulso', blank=True)
    peso = models.CharField(max_length=20, verbose_name='Peso', blank=True)
    talla = models.CharField(max_length=20, verbose_name='Talla', blank=True)
    temperatura = models.CharField(max_length=20, verbose_name='Temperatura', blank=True)
    pa = models.CharField(max_length=20, verbose_name='P.A', blank=True)
    #otros datos pedidos
    atenciones_emergencia = models.CharField(max_length=20, verbose_name='Atenciones de emergencia', blank=True)
    atencion_medica = models.BooleanField('Atencion medica')

    def __unicode__(self):
        return str(self.nro_historia)

    def tipo(self):
        return "enfermeria"


class Tratamiento(models.Model):
    nro_historia = models.ForeignKey(Datos, verbose_name='Numero de Historia Clinica')
    fconsulta = models.DateTimeField(auto_now_add=True)
    operador = models.CharField(max_length=20)
    duracion = models.TimeField()
    profilaxia = models.BooleanField(verbose_name='Profilaxia')
    anestesia = models.CharField(max_length=1, choices=(('L', 'Local'), ('T', 'Troncal'), ('G', 'General')))
    extraccion = models.CharField(max_length=1, choices=(('D', 'Diente'), ('R', 'Raiz'), ('I', 'Impac')))
    amalgamas = models.BooleanField(verbose_name='Amalgamas')
    base = models.BooleanField(verbose_name='Base Cemento')
    radio = models.CharField(max_length=10, verbose_name='Nro de Radiografia')
    tras = models.BooleanField(verbose_name='Diente Trasero')
    otro = models.BooleanField(verbose_name='Otros')
    observaciones = models.TextField(verbose_name='Observaciones')

    def __unicode__(self):
        return str(self.cita)

    def tipo(self):
        return "tratamiento"


class Muestra(models.Model):
    nombre = models.CharField(max_length=25, verbose_name='Tipo de muestra')

    def __unicode__(self):
        return self.nombre


class Analisis(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Tipo de analisis')
    examen = models.ForeignKey(Muestra, verbose_name='Tipo de examen')

    def __unicode__(self):
        return self.nombre


class Laboratorio(models.Model):
    nro_historia = models.ForeignKey(Datos, verbose_name='Numero de Historia Clinica')
    fconsulta = models.DateTimeField(auto_now_add=True)
    muestra = models.ForeignKey(Muestra, verbose_name='Tipo de examen')
    analisis = models.ManyToManyField(Analisis)
    resultado = models.TextField(max_length=20, verbose_name='Resultado del examen')
    #nombre = models.CharField(max_length=20, verbose_name='Especificacion')

    def __unicode__(self):
        return str(self.nro_historia)

    def tipo(self):
        return "laboratorio"


class Rhuesos(models.Model):
    nombre = models.CharField(max_length=20)

    def __unicode__(self):
        return self.nombre


class Respecial(models.Model):
    nombre = models.CharField(max_length=10)

    def __unicode__(self):
        return self.nombre


class RayosX(models.Model):
    nro_historia = models.ForeignKey(Datos, verbose_name='Numero de Historia Clinica')
    fconsulta = models.DateTimeField(auto_now_add=True)
    huesos = models.ForeignKey(Rhuesos, verbose_name='RX Huesos')
    especiales = models.ForeignKey(Respecial, verbose_name='RX Especiales')
    nombre = models.CharField(max_length=20, verbose_name='Especificacion')

    def __unicode__(self):
        return str(self.cita)

    def tipo(self):
        return "rayos x"


class Registro(models.Model):
    datos = models.ForeignKey(Datos, verbose_name='Datos', related_name='fdatos')
    enfermeria = models.ForeignKey(Enfermeria, verbose_name='Enfermeria', null=True, blank=True, related_name='fenfermeria')
    fmedica = models.ForeignKey(Fmedica, verbose_name='Ficha Medica', null=True, blank=True, related_name='fmedica')
    fdental = models.ForeignKey(Fdental, verbose_name='Ficha Dental', null=True, blank=True, related_name='fdental')
    fecha = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.datos) + " -> " + str(self.fecha)


#otros de nuevo

#RAYOS X

class Rayxitem(models.Model):

    codigo = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=25)

    def __unicode__(self):
        return self.nombre


NROplacas = (
    ('a', '1'),
    ('b', '2'),
    ('c', '3'),
    ('d', '4'),
)


class Rayx(models.Model):
    nro_historia = models.ForeignKey(Datos, verbose_name='Numero de Historia Clinica')
    codigo = models.ForeignKey(Rayxitem, verbose_name=u'Hueso')
    paci_tip = models.CharField(max_length=1, choices=(('N', 'Niño'), ('J', 'Joven'), ('A', 'Adulto')), default='J')
    nroplacas = models.CharField(max_length=1, choices=NROplacas, default='a')
    derecho = models.BooleanField(default=False)
    izquierdo = models.BooleanField(default=False)
    otro = models.CharField(max_length=25, verbose_name=u'Examenes especiales')
    resultado = models.TextField()

    def __unicode__(self):
        return self.nombre


#ECOGRAFIA

class Ecot(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=25)

    def __unicode__(self):
        return self.nombre


class Itemeco(models.Model):
    codecot = models.ForeignKey(Ecot)
    codigo = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=25)

    def __unicode__(self):
        return self.nombre


class Ecografia(models.Model):
    nro_historia = models.ForeignKey(Datos, verbose_name='Numero de Historia Clinica')
    fconsulta = models.DateTimeField(auto_now_add=True)
    ecografia = models.ForeignKey(Ecot, verbose_name='Tipo de Ecografia', blank=True)
    eco_analisis = models.ManyToManyField(Itemeco)
    resultado = models.TextField(max_length=20, verbose_name='Resultado de la Ecografia')

    def __unicode__(self):
        return self.nombre


class Odontograma(models.Model):
    nro_historia = models.ForeignKey(Datos, verbose_name='Numero de Historia Clinica')
    fconsulta = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(verbose_name='Observaciones')

    def __unicode__(self):
        return str(self.nro_historia)


class DetalleOdontograma(models.Model):
    """
    Seccion:
    Ninguna 0
    Arriba 1
    Derecha 2
    Abajo 3
    Izquierda 4
    Medio 5
    --------------------------
    Accion:
    Ninguna 0
    Fractura 1
    Restauracion 2
    Extraccion 3
    Puente 4
    """
    odontograma = models.ForeignKey(Odontograma, verbose_name='Odontograma')
    diente = models.IntegerField(verbose_name='Numero de diente')
    seccion = models.IntegerField(verbose_name='Seccion')
    accion = models.IntegerField(verbose_name='Codigo de la accion')
    fecha = models.IntegerField(verbose_name='Fecha')
    diente2 = models.IntegerField(verbose_name='Numero del diente2')

    def __unicode__(self):
        return str(self.odontograma)
