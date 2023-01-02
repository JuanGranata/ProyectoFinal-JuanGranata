from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

# Creacion de los formatos para las tablas dinamicas a ser usadas en los HTMLs

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña")
    password2= forms.CharField(label="Repita Contraseña")

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]
        help_texts = {k:"" for k in fields}#para cada uno de los campos del formulario, le asigna un valor vacio
#agregue email y personalice el mensaje de contrasenia

class BlogForm(forms.Form):
    fecha = forms.DateField()
    #usuario = forms.CharField(max_length=15)
    cuerpo = forms.CharField(max_length=255)
    #imagen = forms.ImageField()
    

class UsuForm(forms.Form):
    usuario = forms.CharField(max_length=15)
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')