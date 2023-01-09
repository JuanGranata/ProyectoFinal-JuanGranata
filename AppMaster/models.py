from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import timezone
from django.conf import settings
from django.utils import timezone


# Create your models here.
# Creacion de modelos para la base de datos

class UserExt(User):

    class Meta:
        proxy = True
    
    def __str__(self):
        return f'{self.username} - {self.first_name} - {self.last_name} - {self.email} - {self.password}'

#hago una copia de los users que se generan en User en mi modelo Usuario

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.author, self.title

class Avatar(models.Model):
    imagen=models.ImageField(upload_to='avatares')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

class Mensaje(models.Model):
    usuario1 = models.CharField(max_length=15)
    usuario2 = models.CharField(max_length=15)
    titulo = models.CharField(max_length=15)
    cuerpo = models.CharField(max_length=255)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario1} - {self.usuario2} - {self.titulo} - {self.cuerpo} - {self.fecha}"

class Msg(models.Model):
    userfrom = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    userto = models.CharField(max_length=15)
    subject = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.userto, self.subject
