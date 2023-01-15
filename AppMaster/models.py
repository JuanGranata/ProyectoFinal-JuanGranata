from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import timezone
from django.conf import settings
from django.utils import timezone


# Create your models here.
# Creacion de modelos para la base de datos

# class UserExt(User):

#     class Meta:
#         proxy = True
    
#     def __str__(self):
#         return f'{self.username} - {self.first_name} - {self.last_name} - {self.email}'


class Usuario(models.Model):
    username=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return f'{self.username} - {self.name} - {self.lastname} - {self.email}'

class Post(models.Model):
    author = models.ForeignKey(to=Usuario, on_delete=models.CASCADE)
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
    user=models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"



