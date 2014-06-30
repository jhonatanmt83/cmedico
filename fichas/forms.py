# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, Select, TextInput, CheckboxInput
from fichas.models import Paciente, Facultad, Semestre, Abceso, Datos, Fmedica, Fdental, Doctor, Enfermeria, Tratamiento, Muestra, Analisis, Laboratorio, Rhuesos, Respecial, RayosX
from fichas.models import Ecografia, Itemeco, Rayx, Rayxitem, Ecot


class formingreso(forms.Form):
    usuario = forms.CharField(label='Usuario')
    clave = forms.CharField(label='Clave', widget=forms.PasswordInput(render_value=False))


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente


class FacultadForm(ModelForm):
    class Meta:
        model = Facultad


class SemestreForm(ModelForm):
    class Meta:
        model = Semestre


class AbcesoForm(ModelForm):
    class Meta:
        model = Abceso


class DatosForm(ModelForm):
    class Meta:
        model = Datos
        widgets = {
            'paciente': Select(attrs={'id': 'paciente_select',
                                    'onchange': "numero_historia()"}),
            'nro_historia': TextInput(attrs={'id': 'nro_historia',
                                    'readonly': 'readonly'}),
        }


class FmedicaForm(ModelForm):
    class Meta:
        model = Fmedica
        widgets = {
            'nro_historia': Select(attrs={'disabled': 'disabled'}),
        }


class FdentalForm(ModelForm):
    class Meta:
        model = Fdental
        widgets = {
            'nro_historia': Select(attrs={'disabled': 'disabled'}),
        }


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor


class EnfermeriaForm(ModelForm):
    class Meta:
        exclude = ('atencion_medica')
        model = Enfermeria
        widgets = {
            'nro_historia': Select(attrs={'disabled': 'disabled'}),
        }


class TratamientoForm(ModelForm):
    class Meta:
        model = Tratamiento


class MuestraForm(ModelForm):
    class Meta:
        model = Muestra


class AnalisisForm(ModelForm):
    class Meta:
        model = Analisis


class LaboratorioForm(ModelForm):
    class Meta:
        model = Laboratorio
        widgets = {
            'muestra': Select(attrs={'onchange': 'obtener_analisis()'}),
        }


class RhuesosForm(ModelForm):
    class Meta:
        model = Rhuesos


class RespecialForm(ModelForm):
    class Meta:
        model = Respecial


class RayosXForm(ModelForm):
    class Meta:
        model = RayosX


class DatosEnfermeria(ModelForm):
    class Meta:
        model = Enfermeria
        fields = ('frecuencia_cardiaca',
            'frecuencia_respiratoria',
            'pulso',
            'peso',
            'talla',
            'temperatura',
            'pa',
            'tapon')
        widgets = {
            'frecuencia_cardiaca': TextInput(attrs={'readonly': 'readonly'}),
            'frecuencia_respiratoria': TextInput(attrs={'readonly': 'readonly'}),
            'pulso': TextInput(attrs={'readonly': 'readonly'}),
            'peso': TextInput(attrs={'readonly': 'readonly'}),
            'talla': TextInput(attrs={'readonly': 'readonly'}),
            'temperatura': TextInput(attrs={'readonly': 'readonly'}),
            'pa': TextInput(attrs={'readonly': 'readonly'}),
            'tapon': CheckboxInput(attrs={'disabled': 'disabled'}),
        }


class EcografiaForm(ModelForm):
    class Meta:
        model = Ecografia
        widgets = {
            'ecografia': Select(attrs={'onchange': 'obtener_analisis()'}),
        }


class ItemecoForm(ModelForm):
    class Meta:
        model = Itemeco


class EcotForm(ModelForm):
    class Meta:
        model = Ecot


class RayxForm(ModelForm):
    class Meta:
        model = Rayx


class RayxitemForm(ModelForm):
    class Meta:
        model = Rayxitem
