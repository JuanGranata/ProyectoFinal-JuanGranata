from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import timezone
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Msg(models.Model):
    userfrom = models.CharField(max_length=15)
    userto = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.userto} - {self.userfrom} - {self.subject} - {self.text} - {self.published_date}'