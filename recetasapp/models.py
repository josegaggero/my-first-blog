from django.db import models

# Create your models here.
class Receta(models.Model):
    titulo = models.TextField(max_length=50)
    advertencia = models.TextField(max_length=40)
    ingrdientes = models.TextField(max_length=400)
    intrucciones = models.TextField(max_length=1050)
    imagen = models.ImageField(null=True ,blank=True)  
    def __str__(self) :
        return self.titulo + " " + self.advertencia+ " ------  "+ self.ingrdientes +"  ----->  " + self.intrucciones 

  


class Persona(models.Model):
    nombre = models.TextField(max_length=30)
    apellido = models.TextField(max_length=30)
    email = models.TextField(max_length=25)
    pais = models.TextField(max_length=15)

    def __str__(self) :
        return self.nombre + " " + self.apellido + " ------  "+ self.email +"  ----->  " + self.pais



class Usuarios(models.Model):
    nombre_usuario = models.TextField(max_length=30)
    clave = models.TextField(max_length=20)
    def __str__(self) :
        return self.nombre_usuario + " " + self.clave 



class Iniciar(models.Model):
    mail = models.TextField(max_length=30)
    clave = models.TextField(max_length=20)
    def __str__(self) :
        return self.mail + " " + self.clave 


class Contraseña(models.Model):
    contraseña1 = models.TextField(max_length=20)
    contraseña2 = models.TextField(max_length=20)
    def __str__(self) :
        return "| Contraseña = "+self.contraseña1 + " | Confirmacion de la contraseña = " + self.contraseña2 



