from django.db import models

# Create your models here.
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


