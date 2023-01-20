from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import timezone
from django.conf import settings
from django.utils import timezone
#from AppMaster.models import UserExt

# Create your models here.

class Msg(models.Model):
    userfrom = models.CharField(max_length=15)
    userto = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        #return f'{self.userto} - {self.userfrom} - {self.subject} - {self.text} - {self.published_date}'
        return f'{self.userfrom}'
#---------------------------------------------------------------------------------------------------------------------
# Modelo para mensajeria
class Message(models.Model):
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, null=True)
    content = models.CharField(max_length=10000, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(null = True)
    
    def __str__(self):
        return f"From: {self.sender} to: {self.receiver} {self.date}" 
    
    def view(self):
        return f"De: {self.sender}. Asunto: {self.subject}"
    
    def is_seen(self):
        if self.seen == True:
            return "Leido"
        else:
            return "No leido"