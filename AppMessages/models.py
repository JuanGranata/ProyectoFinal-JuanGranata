from django.db import models

# Create your models here.
class Mensaje(models.Model):
    origen = models.CharField(max_length=15)
    destino = models.CharField(max_length=15)
    mensaje = models.CharField(max_length=255)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return self.origen+" le envio un mensaje a: "+self.destino