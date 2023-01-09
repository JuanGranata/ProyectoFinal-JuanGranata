from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.utils import timezone

# Creacion de los formatos para las tablas dinamicas a ser usadas en los HTMLs
 
class RegistroUsuarioForm(UserCreationForm):
    #agregue email y personalice el mensaje de contrasenia
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]
        help_texts = {k:"" for k in fields} #para cada uno de los campos del formulario, le asigna un valor vacio

class RegExtForm(UserCreationForm):
    #agregue email y personalice el mensaje de contrasenia
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

class UsuForm(forms.Form):
    usuario = forms.CharField(max_length=15)
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")

class UserEditForm(UserCreationForm):
    username = forms.CharField(label='Usuario')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)


#nuevo form para los posteos
		
class PostForm(forms.ModelForm):
    date = forms.DateTimeField(initial=timezone.now)
	
    class Meta:
        model = Post
        fields = ('author', 'title', 'text')
