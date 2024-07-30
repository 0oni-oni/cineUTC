from django.db import models

# Creando un modelo genero: Terror, Comedia, accion, ciencia ficcion 

class Genero(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25) 
    Descripcion=models.CharField(max_length=150,default='') 
    foto=models.FileField(upload_to='generos',null=True,blank=True)
    def __str__(self):
        fila="{0}: {1} - {2}"
        return fila.format(self.id,self.nombre,self.Descripcion)

class Director(models.Model):
    id=models.AutoField(primary_key=True)
    dni=models.CharField(max_length=15)             
    apellido=models.CharField(max_length=25) 
    nombre=models.CharField(max_length=25) 
    estado=models.BooleanField(default=True)
    foto=models.FileField(upload_to='portadas',null=True,blank=True) 
    def __str__(self):
        fila="{0}: {1} - {2} - {3} - {4}"
        return fila.format(self.id,self.dni,self.apellido,self.nombre,self.estado)
    
class Paises(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    continente=models.CharField(max_length=30) 
    capital=models.CharField(max_length=30)
    def __str__(self):
        fila="{0}: {1} - {2} - {3}"
        return fila.format(self.id,self.nombre,self.continente,self.capital)

class Pelicula(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=50)
    duracion=models.DecimalField(max_digits=3,decimal_places=2)
    sinonimos=models.TextField()
    genero=models.ForeignKey(Genero, on_delete=models.CASCADE) #cascade es un metodo que elimina sin preguntar
    director=models.ForeignKey(Director, on_delete=models.CASCADE)
    pais=models.ForeignKey(Paises, on_delete=models.CASCADE)
    portada=models.FileField(upload_to='portadas',null=True,blank=True)

    def __str__(self): #paradigma de la clase es el self 
        fila="{0}: {1}"
        return fila.format(self.id,self.titulo)
#Creando modelo Cine
class Cine(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25)
    direccion=models.CharField(max_length=150,default='')
    telefono=models.CharField(max_length=150,default='')
    def __str__(self):
        fila="{0}: {1} - {2}"
        return fila.format(self.id,self.nombre,self.direccion) 