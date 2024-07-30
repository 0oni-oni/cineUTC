from django.shortcuts import redirect,render
from.models import Genero, Pelicula, Director
from django.contrib import  messages
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
    nuevoGenero=Genero.objects.create(nombre=nom,Descripcion=des)
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
    nuevoDirector = Director.objects.create(dni=dni, apellido=apellido, nombre=nombre)
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

#lstado peliculas
def listadoDirectores(request):
    directoresBdd=Director.objects.all()
    return render(request,"listadoDirectores.html",{'directores':directoresBdd})





