from django.shortcuts import redirect,render
from.models import Genero, Pelicula, Director, Paises, Cine
from django.contrib import  messages
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    return render(request,"home.html")

def listadoGeneros(request):
    generosBdd=Genero.objects.all()
    return render(request,"listadoGeneros.html",{'generos':generosBdd})

def eliminarGenero(request,id):
    generoEliminar=Genero.objects.get(id=id)
    generoEliminar.delete()
     #mensajes de confirmacion para sweetalert Y TOCA CON JNJA2 VINCULAR EN LA PLANTILLA
    messages.success(request,"GENERO ELIMINADO EXITOSAMENTE.")
    return redirect('listadoGeneros')

def nuevoGenero(request):
    return render(request,'nuevoGenero.html')

def guardarGenero(request):
    nom=request.POST["nombre"]
    des=request.POST["descripcion"]
    fot=request.FILES.get("foto") #parentesis
    nuevoGenero=Genero.objects.create(nombre=nom,Descripcion=des,foto=fot)
    #mensajes de confirmacion para sweetalert Y TOCA CON JNJA2 VINCULAR EN LA PLANTILLA 
    messages.success(request,"GENERO GUARDADO EXITOSAMENTE.")
    return  redirect('listadoGeneros')

def editarGenero(request,id):
    generoEditar=Genero.objects.get(id=id)
    return render(request,'editarGenero.html',{'generoEditar':generoEditar})

#Actualizando los nuevos datos en la BDD
def procesarActualizarGenero(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    descripcion=request.POST['descripcion']
    generoConsultado=Genero.objects.get(id=id)
    generoConsultado.nombre=nombre
    generoConsultado.descripcion=descripcion
    generoConsultado.save()
    messages.success(request,'Genero actualizado exitosamente.')
    return redirect('listadoGeneros')




#listado director

def listadoDirectores(request):
    directores = Director.objects.all()
    return render(request, "listadoDirectores.html", {'directores': directores})

def eliminarDirector(request, id):
    directorEliminar = Director.objects.get(id=id)
    directorEliminar.delete()
    messages.success(request, "Director eliminado exitosamente.")
    return redirect('listadoDirectores')

def nuevoDirector(request):
    return render(request, 'nuevoDirector.html')

def guardarDirector(request):
    dni = request.POST["dni"]
    apellido = request.POST["apellido"]
    nombre = request.POST["nombre"]
    fot = request.FILES.get("foto")
    nuevoDirector = Director.objects.create(dni=dni, apellido=apellido, nombre=nombre, foto=fot)
    messages.success(request, "Director guardado exitosamente.")
    return redirect('listadoDirectores')

def editarDirector(request, id):
    directorEditar = Director.objects.get(id=id)
    return render(request, 'editarDirector.html', {'directorEditar': directorEditar})

def procesarActualizarDirector(request):
    id = request.POST['id']
    dni = request.POST['dni']
    apellido = request.POST['apellido']
    nombre = request.POST['nombre']
    directorConsultado = Director.objects.get(id=id)
    directorConsultado.dni = dni
    directorConsultado.apellido = apellido
    directorConsultado.nombre = nombre
    directorConsultado.save()
    messages.success(request, 'Director actualizado exitosamente.')
    return redirect('listadoDirectores')

#listado paises
def listadoPaises(request):
    paisesBdd = Paises.objects.all()
    return render(request, "listadoPaises.html", {'paises': paisesBdd})

def eliminarPais(request, id):
    paisEliminar = Paises.objects.get(id=id)
    paisEliminar.delete()
    messages.success(request, "País eliminado exitosamente.")
    return redirect('listadoPaises')

def nuevoPais(request):
    return render(request, 'nuevoPais.html')

def guardarPais(request):
    nombre = request.POST["nombre"]
    continente = request.POST["continente"]
    capital = request.POST["capital"]
    nuevoPais = Paises.objects.create(nombre=nombre, continente=continente, capital=capital)
    messages.success(request, "País guardado exitosamente.")
    return redirect('listadoPaises')

def editarPais(request, id):
    paisEditar = Paises.objects.get(id=id)
    return render(request, 'editarPais.html', {'paisEditar': paisEditar})

def procesarActualizarPais(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    continente = request.POST['continente']
    capital = request.POST['capital']
    paisConsultado = Paises.objects.get(id=id)
    paisConsultado.nombre = nombre
    paisConsultado.continente = continente
    paisConsultado.capital = capital
    paisConsultado.save()
    messages.success(request, 'País actualizado exitosamente.')
    return redirect('listadoPaises')



#lstado peliculas
def listadoPeliculas(request):
    peliculasBdd = Pelicula.objects.all()
    return render(request, "listadoPeliculas.html", {'peliculas': peliculasBdd})

def eliminarPelicula(request, id):
    peliculaEliminar = Pelicula.objects.get(id=id)
    peliculaEliminar.delete()
    messages.success(request, "PELÍCULA ELIMINADA EXITOSAMENTE.")
    return redirect('listadoPeliculas')

def nuevaPelicula(request):
    generos = Genero.objects.all()
    directores = Director.objects.all()
    paises = Paises.objects.all()
    return render(request, 'nuevaPelicula.html', {'generos': generos, 'directores': directores, 'paises': paises})

def guardarPelicula(request):
    titulo = request.POST["titulo"]
    duracion = request.POST["duracion"]
    sinonimos = request.POST["sinonimos"]
    genero_id = request.POST["genero"]
    director_id = request.POST["director"]
    pais_id = request.POST["pais"]

    genero = Genero.objects.get(id=genero_id)
    director = Director.objects.get(id=director_id)
    pais = Paises.objects.get(id=pais_id)

    nuevaPelicula = Pelicula.objects.create(
        titulo=titulo,
        duracion=duracion,
        sinonimos=sinonimos,
        genero=genero,
        director=director,
        pais=pais
    )
    messages.success(request, "PELÍCULA GUARDADA EXITOSAMENTE.")
    return redirect('listadoPeliculas')

def editarPelicula(request, id):
    peliculaEditar = Pelicula.objects.get(id=id)
    generos = Genero.objects.all()
    directores = Director.objects.all()
    paises = Paises.objects.all()
    return render(request, 'editarPelicula.html', {
        'peliculaEditar': peliculaEditar,
        'generos': generos,
        'directores': directores,
        'paises': paises
    })

def procesarActualizarPelicula(request):
    id = request.POST['id']
    titulo = request.POST['titulo']
    duracion = request.POST['duracion']
    sinonimos = request.POST['sinonimos']
    genero_id = request.POST['genero']
    director_id = request.POST['director']
    pais_id = request.POST['pais']

    peliculaConsultada = Pelicula.objects.get(id=id)
    peliculaConsultada.titulo = titulo
    peliculaConsultada.duracion = duracion
    peliculaConsultada.sinonimos = sinonimos
    peliculaConsultada.genero = Genero.objects.get(id=genero_id)
    peliculaConsultada.director = Director.objects.get(id=director_id)
    peliculaConsultada.pais = Paises.objects.get(id=pais_id)

    peliculaConsultada.save()
    messages.success(request, 'PELÍCULA ACTUALIZADA EXITOSAMENTE.')
    return redirect('listadoPeliculas')

#cine

def gestionCines(request):
    return render(request,'gestionCines.html')

#Insertando cines mediante AJAX en la Base de Datos
def guardarCine(request):
    nom=request.POST["nombre"]
    dir=request.POST["direccion"]
    tel=request.POST["telefono"]
    nuevoCine=Cine.objects.create(nombre=nom,direccion=dir,telefono=tel)    
    return JsonResponse({
        'estado': True,
        'mensaje': 'Género registrado exitosamente.',
    })
#renderizado cines
def listadoCines(request):
    cines=Cine.objects.all()
    return render(request,"listadoCines.html",{'cines':cines})

