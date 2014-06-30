from django.db import models
import datetime
from django import forms
from django.forms import ModelForm,Select,TextInput
from fichas.models import Datos
# Create your models here.


class Doctor(models.Model):
    nombres = models.CharField(max_length=50, verbose_name = 'Nombres')
    apellidos = models.CharField(max_length=50, verbose_name = 'Apellidos')
    vigente = models.BooleanField(verbose_name='Vigente')
    
    def __unicode__(self):
        return self.nombres+" "+self.apellidos

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        
class Venta(models.Model):
    numero_venta = models.IntegerField(verbose_name = 'Numero de Venta')
    costo = models.DecimalField(max_digits=8, decimal_places=2, verbose_name = 'Monto S/.')
    fecha = models.DateTimeField( auto_now_add=True)
    doctor = models.ForeignKey(Doctor,verbose_name = 'Doctor')
    paciente = models.ForeignKey(Datos,verbose_name = 'Paciente')
    
    def __unicode__(self):
        return self.numero_venta

class VentaForm(ModelForm):
    class Meta:
        model = Venta
        
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=50, verbose_name = 'Nombres')
    
    def __unicode__(self):
        return self.nombre

class LaboratorioForm(ModelForm):
    class Meta:
        model = Laboratorio

class Presentacion(Laboratorio):
    
    def __unicode__(self):
        return self.nombre

class PresentacionForm(ModelForm):
    class Meta:
        model = Presentacion

class Grupo(Laboratorio):
    def __unicode__(self):
        return self.nombre

class GrupoForm(ModelForm):
    class Meta:
        model = Grupo

class Proveedor(models.Model):
    ruc = models.IntegerField(verbose_name='RUC', primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name = 'Nombre')
    direccion = models.CharField(max_length=20,verbose_name='Direccion')
    celular = models.CharField(max_length=10,verbose_name='Celular')
    telefono = models.CharField(max_length=10,verbose_name='Telefono')
    provincia = models.CharField(max_length=20,verbose_name='Provincia')
    
    def __unicode__(self):
        return self.ruc

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor

class Producto(models.Model):
    codigo = models.IntegerField(verbose_name='RUC', primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name = 'Nombre')
    dosis = models.IntegerField(verbose_name='Dosis')
    grupo = models.ForeignKey(Grupo,verbose_name = 'Grupo')
    presentacion = models.ForeignKey(Presentacion,verbose_name = 'Presentacion')
    
    def __unicode__(self):
        return str(self.codigo)

class ProductoForm(ModelForm):
    class Meta:
        model = Producto

class Compra(models.Model):
    numero_compra = models.IntegerField(verbose_name='Numero de compra', primary_key=True)
    fecha = models.DateTimeField( auto_now_add=True)
    costo = models.DecimalField(max_digits=8, decimal_places=2, verbose_name = 'Monto S/.')
    proveedor = models.ForeignKey(Proveedor,verbose_name = 'Proveedor')
    
    def __unicode__(self):
        return self.numero_compra

class CompraForm(ModelForm):
    class Meta:
        model = Compra

class CompraProducto(models.Model):
    producto = models.ForeignKey(Producto,verbose_name='Producto')
    cantidad = models.CharField(max_length=50, verbose_name = 'Cantidad')
    fecha_vencimiento = models.DateField( auto_now_add=False,verbose_name='Fecha Vencimiento')
    lote = models.IntegerField(verbose_name='Lote')
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2, verbose_name = 'Precio Unitario S/.')
    compra = models.ForeignKey(Compra,verbose_name='Numero de compra')
    
    def __unicode__(self):
        return self.producto

class CompraProductoForm(ModelForm):
    class Meta:
        model = CompraProducto

class Almacen(models.Model):
    producto = models.ForeignKey(Producto,verbose_name='Producto')
    precio = models.DecimalField(max_digits=8, decimal_places=2, verbose_name = 'Precio S/.')
    laboratorio = models.ForeignKey(Laboratorio,verbose_name='Laboratorio')
    stock = models.IntegerField(verbose_name='Stock')
    fecha_vencimiento = models.DateField( auto_now_add=False,verbose_name='Fecha Vencimiento')
    #lote = 

class AlmacenForm(ModelForm):
    class Meta:
        model = Almacen

class BajaProductos(models.Model):
    #lote = 
    almacen = models.ForeignKey(Almacen,verbose_name='Almacen')
    fecha = models.DateField( auto_now_add=True)
    cantidad = models.CharField(max_length=50, verbose_name = 'Cantidad')
    precio_estimado = models.DecimalField(max_digits=8, decimal_places=2, verbose_name = 'Precio Estimado S/.')
    
    def __unicode__(self):
        return self.almacen
        
class BajaProductosForm(ModelForm):
    class Meta:
        model = BajaProductos
