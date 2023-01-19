from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.utils import timezone

#-----------------------------------------------------------------------------------------
#Form para Mensajeria
class Message_Form(forms.Form):
    receiver = forms.CharField(max_length=200, label="Para:")
    subject = forms.CharField(max_length=200, label="Asunto:")
    content = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'rows':10, 'cols':50}), label="Mensaje:")

class Respond_Form(forms.Form):
    content = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'rows':10, 'cols':50}), label="Mensaje:")
    
    
class RespondForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sender','receiver','subject','content']
        labels = {
            'sender': 'De:',
            'receiver': 'Para:',
            'subject': 'Asunto:',
            'content': 'Mensaje:',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows':10, 'cols':50})
        }