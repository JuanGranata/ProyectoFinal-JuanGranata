from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppMaster.forms import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy

# Create your views here.

#Modulo Avatar
def nuevoAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatares/avatarpordefecto.png"
    return imagen

# Modulo de inicio
@login_required
def inicio(request):
    #lista=Avatar.objects.filter(user=request.user)
    
    return render (request, "AppMaster/inicio.html")

# Modulo about me
def aboutme(request):
    return render (request, "AppMaster/aboutme.html")

# Modulo pagina usuario
#@login_required
def usuario(request):
    return render (request, "AppMaster/usuario.html",context)

# Modulo mensaje exitoso
def exitoso(request):
    return render (request, "AppMaster/exitoso.html")

# Modulo carga de blog
def blog_form(request):
    if request.method=="POST":
        form=BlogForm(request.POST)
        if form.is_valid():
            art=form.cleaned_data
            blog = Blog(usuario=(request.user), cuerpo=art["cuerpo"], fecha=art["fecha"])
            blog.save()
            return render (request, "AppMaster/exitoso.html", {"mensaje": "Blog creado Correctamente!!"})
    else:
        form=BlogForm()
    
    return render (request, "AppMaster/blog.html", {"form":form})


#def blog_form(request):
#    if request.method=="POST":
#        form=BlogForm(request.POST)
#        if form.is_valid():
#            art=form.cleaned_data
#            blog = Blog(usuario=art["usuario"], cuerpo=art["cuerpo"], fecha=art["fecha"])
#            blog.save()
#            return render (request, "AppMaster/exitoso.html", {"mensaje": "Blog creado Correctamente!!"})
#    else:
#        form=BlogForm()
    
#    return render (request, "AppMaster/blog.html", {"form":form})

# Modulo carga de usuarios
@login_required
def usu_form(request):
    if request.method=="POST":
        form=UsuForm(request.POST)
        if form.is_valid():
            usu = form.cleaned_data
            user = Usuario(usuario=usu["usuario"], nombre=usu["nombre"], apellido=usu["apellido"], email=usu["email"])
            user.save()
            return render (request, "AppMaster/exitoso.html", {"mensaje": "Usuario CREADO CORRECTAMENTE!!"})#, "imagen":nuevoAvatar(request)})
    else:
        formulario=UsuForm()
    
    return render (request, "AppMaster/crearuser.html", {"form":formulario})

#modulo para registro de usuarios con privilegios
@login_required
def register(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            #aca se podria loguear el usuario, con authenticate y login... pero no lo hago
            return render(request, "AppMaster/exitoso.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "AppMaster/register.html", {"form":form, "mensaje":"Error al crear el usuario"})
        
    else:
        form=RegistroUsuarioForm()

    return render(request, "AppMaster/register.html", {"form":form})

# Modulos de buquedas de clinetes en la base de datos
@login_required
def buscaruser(request):
    return render(request, "AppMaster/buscaruser.html")

# Modulos para editar usuarios
@login_required
def editarUsuario(request):
    return render(request, "AppMaster/editarUsuario.html")
# Algoritmo de busqueda de usuario

@login_required
def buscar(request):
    if request.GET["user"]:
        user=request.GET["user"]
        users=Usuario.objects.filter(usuario__icontains=user)
        return render(request,"AppMaster/resultadosBusqueda.html", {"usuario":users} )
    else:
        return render(request, "AppMaster/buscaruser.html", {"mensaje":"Por favor ingresa el Usuario"})

def addAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)#ademas del post, como trae archivos (yo se que trae archivos xq conozco el form, tengo q usar request.files)
        if form.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)!=0:
                avatarViejo[0].delete()
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatar.save()
            return render(request, "AppMaster/inicio.html", {"mensaje":"Avatar agregado correctamente"})
        else:
            return render(request, "AppMaster/addAvatar.html", {"formulario": form, "usuario": request.user})
    else:
        form=AvatarForm()
        return render(request , "AppMaster/addAvatar.html", {"formulario": form, "usuario": request.user})

@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "AppMaster/exitoso.html", {"mensaje":"Perfil editado correctamente"})
        else:
            return render(request, "AppMaster/editarUsuario.html", {"form":form, "nombreusuario":usuario.username, "mensaje":"Error al editar el perfil"})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "AppMaster/editarUsuario.html", {"form":form, "nombreusuario":usuario.username})


#----- seccion de login ------

def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")

            usuario=authenticate(username=usu, password=clave)#trae un usuario de la base, que tenga ese usuario y ese pass, si existe, lo trae y si no None
            if usuario is not None:    
                login(request, usuario)
                return render(request, 'AppMaster/inicio.html', {'mensaje':f"Bienvenido {usuario}" })
            else:
                return render(request, 'AppMaster/login.html', {'mensaje':"Usuario o contraseña incorrectos", 'form':form})

        else:
            return render(request, 'AppMaster/login.html', {'mensaje':"Usuario o contraseña incorrectos", 'form':form})

    else:
        form = AuthenticationForm()
    return render(request, "AppMaster/login.html", {"form":form})

# CRUD basado en clases
class UsuarioList(LoginRequiredMixin, ListView):
    model=Usuario
    template_name="AppMaster/leerUsuario.html"

#class UsuarioCreacion(LoginRequiredMixin, CreateView):
#    model = Usuario
#    success_url = reverse_lazy('usuario_listar')
#    fields=['nombre', 'apellido', 'email']

class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    model = Usuario
    success_url = reverse_lazy('usuario_listar')
    fields=['nombre', 'apellido', 'email']

class UsuarioDelete(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuario_listar')

class UsuarioDetalle(LoginRequiredMixin, DetailView):
    model= Usuario
    template_name="AppMaster/usuario_detalle.html"

