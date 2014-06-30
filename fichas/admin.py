# -*- coding: utf-8 -*-
from django.contrib import admin
from fichas.models import Facultad
from fichas.models import Semestre
from fichas.models import Paciente
from fichas.models import Datos
from fichas.models import Fmedica
from fichas.models import Fdental
from fichas.models import Enfermeria
from fichas.models import Tratamiento
from fichas.models import Muestra
from fichas.models import Analisis
from fichas.models import Laboratorio
from fichas.models import Rhuesos
from fichas.models import Respecial
from fichas.models import RayosX
from fichas.models import Abceso
from fichas.models import Doctor
from fichas.models import Registro
from fichas.models import Ecografia
from fichas.models import Itemeco
from fichas.models import Ecot
from fichas.models import Odontograma
from fichas.models import DetalleOdontograma


admin.site.register(Facultad)
admin.site.register(Semestre)
admin.site.register(Paciente)
admin.site.register(Datos)
admin.site.register(Fmedica)
admin.site.register(Fdental)
admin.site.register(Enfermeria)
admin.site.register(Tratamiento)
admin.site.register(Muestra)
admin.site.register(Analisis)
admin.site.register(Laboratorio)
admin.site.register(Rhuesos)
admin.site.register(Respecial)
admin.site.register(RayosX)
admin.site.register(Abceso)
admin.site.register(Doctor)
admin.site.register(Registro)
admin.site.register(Ecografia)
admin.site.register(Itemeco)
admin.site.register(Ecot)
admin.site.register(Odontograma)
admin.site.register(DetalleOdontograma)
