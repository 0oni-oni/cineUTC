# configurando el redireccionamiento

from django.urls import path
from.import views

urlpatterns = [
    path('',views.home), # las comillas simples  significa localhost
    path('listadoGeneros/',views.listadoGeneros, name='listadoGeneros'),   #no recibe parametros
    path('eliminarGenero/<id>', views.eliminarGenero, name='eliminarGenero'), #recive parametros
    path('nuevoGenero/',views.nuevoGenero, name='nuevoGenero'),
    path('guardarGenero/',views.guardarGenero, name='guardarGenero'),
    path('editarGenero/<id>',views.editarGenero, name='editarGenero'),
    path('procesarActualizarGenero/',views.procesarActualizarGenero, name='procesarActualizarGenero'),

    path('listadoDirectores/',views.listadoDirectores, name='listadoDirectores'),   #no recibe parametros
    path('eliminarDirector/<id>', views.eliminarDirector, name='eliminarDirector'), #recive parametros
    path('nuevoDirector/',views.nuevoDirector, name='nuevoDirector'),
    path('guardarDirector/',views.guardarDirector, name='guardarDirector'),
    path('editarDirector/<int:id>/', views.editarDirector, name='editarDirector'),
    path('procesarActualizarDirector/',views.procesarActualizarDirector, name='procesarActualizarDirector'),

    path('listadoPaises/', views.listadoPaises, name='listadoPaises'),
    path('eliminarPais/<int:id>/', views.eliminarPais, name='eliminarPais'),
    path('nuevoPais/', views.nuevoPais, name='nuevoPais'),
    path('guardarPais/', views.guardarPais, name='guardarPais'),
    path('editarPais/', views.editarPais, name='editarPais'),
    path('procesarActualizarPais/', views.procesarActualizarPais, name='procesarActualizarPais'),

    path('listadoPeliculas/', views.listadoPeliculas, name='listadoPeliculas'),
    path('eliminarPelicula/<id>',views.eliminarPelicula, name='eliminarPelicula'),
    path('nuevaPelicula/',views.nuevaPelicula, name='nuevaPelicula'),
    path('guardarPelicula/',views.guardarPelicula, name='guardarPelicula'),
    path('editarPelicula/<id>',views.editarPelicula, name='editarPelicula'),
    path('procesarActualizarPelicula/',views.procesarActualizarPelicula, name='procesarActualizarPelicula'),


    path('gestionCines/',views.gestionCines, name='gestionCines'),
    path('guardarCine/',views.guardarCine, name='guardarCine'), 
    path('listadoCines/',views.listadoCines, name='listadoCines'), 

    

]