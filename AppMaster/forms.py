from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.utils import timezone

# Creacion de los formatos para las tablas dinamicas a ser usadas en los HTMLs

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")

class UserEditForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'Repetir contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'website']
        labels = {
            'bio': 'Biografia',
            'avatar': 'Avatar',
            'website': 'Sitio web',
        }
#nuevo form para los posteos
		
class PostForm(forms.ModelForm):
    date = forms.DateTimeField(initial=timezone.now)
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'created_date']


