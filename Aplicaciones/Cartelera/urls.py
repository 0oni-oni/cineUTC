# configurando el redireccionamiento

from django.urls import path
from.import views

urlpatterns = [
    path('',views.home), # las comillas simples  significa localhost
    path('listadoGeneros/',views.listadoGeneros, name='listadoGeneros'),   #no recibe parametros
    path('eliminarGenero/<id>', views.eliminarGenero, name='listadoGenero'), #recive parametros
    path('nuevoGenero/',views.nuevoGenero, name='nuevoGenero'),
    path('guardarGenero/',views.guardarGenero, name='guardarGenero'),
    path('editarGenero/<id>',views.editarGenero, name='editarGenero'),
    path('procesarActualizarGenero/',views.procesarActualizarGenero, name='procesarActualizarGenero'),

    path('listadoPeliculas/',views.listadoPeliculas),
    path('listadoDirectores/',views.listadoDirectores),
]