from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
# Creacion de modelos para la base de datos

class Usuario(models.Model):
    usuario = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.usuario," ",self.nombre,", ",self.apellido," email:",self.email

class Blog(models.Model):
    usuario = models.CharField(max_length=15)
    cuerpo = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to="blog", null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.usuario ,": " , self.cuerpo , " cargado el:" , self.fecha

class Avatar(models.Model):
    imagen=models.ImageField(upload_to='avatares')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"