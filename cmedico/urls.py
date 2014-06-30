# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'fichas.views.operaciones'),
    url(r'^operaciones/$', 'fichas.views.operaciones'),
    url(r'^operaciones/registrar/$', 'fichas.views.datos'),
    url(r'^operaciones/datos/$', 'fichas.views.datos'),
    url(r'^operaciones/fmedica/$', 'fichas.views.fmedica'),
    url(r'^operaciones/fmedica/(?P<historiac>\w+)$', 'fichas.views.fmedica_buscado'),
    url(r'^operaciones/fdental/$', 'fichas.views.fdental'),
    url(r'^operaciones/fdental/(?P<historiac>\w+)$', 'fichas.views.fdental_buscado'),
    url(r'^operaciones/odontograma/(?P<historiac>\w+)$', 'fichas.views.fdental_odontograma'),
    url(r'^operaciones/odontograma/crear/(?P<historiac>\w+)$', 'fichas.views.fdental_odontograma_crear'),
    url(r'^operaciones/enfermeria/$', 'fichas.views.enfermeria'),
    url(r'^operaciones/enfermeria/(?P<historiac>\w+)$', 'fichas.views.enfermeria_buscado'),
    url(r'^operaciones/laboratorio/$', 'fichas.views.laboratorio'),
    url(r'^operaciones/medicamentos/$', 'fichas.views.medicamentos'),
    url(r'^reportes/$', 'fichas.views.reportes'),
    #url(r'^reportes/(?P<historiac>\w+)$', 'fichas.views.detalles'),
    url(r'^reportes/tipo/(?P<paciente>\w+)$', 'fichas.views.reporte_paciente'),
    url(r'^reportes/detalle/(?P<historiac>\w+)$', 'fichas.views.reporte_detalle'),
    url(r'^reportes/detallado/(?P<ficha>\w+)/(?P<id_ficha>\w+)$', 'fichas.views.reporte_detallado'),
    url(r'^numero_historia/(?P<tipo>[1-4])$', 'fichas.views.numero_historia'),
    url(r'^operaciones/placas/$', 'fichas.views.placas'),
    url(r'^operaciones/placas/rayosx/$', 'fichas.views.rayosx'),
    url(r'^operaciones/placas/ecografia/$', 'fichas.views.ecografia'),
    url(r'^receta/$', 'fichas.views.receta'),
    #ajax
    url(r'^laboratorio/obtener_analisis/(\d+)/$', 'fichas.views.obtener_analisis'),
    url(r'^ecografia/obtener_analisis/(\d+)/$', 'fichas.views.obtener_analisis_ecografia'),
    url(r'^odontograma/accion/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)$', 'fichas.views.accion_odontograma'),
    #login urls
    url(r'^ingreso/$', 'fichas.views.ingreso'),
    url(r'^salida/$', 'fichas.views.salida'),

    # Examples:
    # url(r'^$', 'cmedico.views.home', name='home'),
    # url(r'^cmedico/', include('cmedico.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
