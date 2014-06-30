from django.contrib import admin
from farmacia.models import Doctor
from farmacia.models import Venta
from farmacia.models import Laboratorio
from farmacia.models import Presentacion
from farmacia.models import Grupo
from farmacia.models import Proveedor
from farmacia.models import Producto
from farmacia.models import Compra
from farmacia.models import CompraProducto
from farmacia.models import Almacen
from farmacia.models import BajaProductos



admin.site.register(Doctor)
admin.site.register(Venta)
admin.site.register(Laboratorio)
admin.site.register(Presentacion)
admin.site.register(Grupo)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(CompraProducto)
admin.site.register(Almacen)
admin.site.register(BajaProductos)

