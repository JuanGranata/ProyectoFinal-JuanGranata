from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import PostForm
from django.http import HttpResponse
from AppMaster.forms import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, User
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.utils import timezone


# Create your views here.

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

#Modulo Avatar
def nuevoAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatares/avatarpordefecto.png"
    return imagen

# Modulo de inicio
#@login_required
def inicio(request):
    avatares = AvatarSuper.objects.filter(user=request.user.id)
    print('--ID-->', request.user.id)
    return render (request, "AppMaster/padre.html", {"imagen":avatares[0].imagen.url})

# Modulo about me
def aboutme(request):
    return render (request, "AppMaster/aboutme.html")

# Modulo mensaje exitoso
def exitoso(request):
    return render (request, "AppMaster/exitoso.html")


#---------------------------------------------------------------------------------------------------------------------
# Modulo para registro de usuarios
#@login_required
def register(request):
    if request.method=="POST":
        form=RegExtForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            #aca se podria loguear el usuario, con authenticate y login... pero no lo hago
            return render(request, "AppMaster/exitoso.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "AppMaster/register.html", {"form":form, "mensaje":"Error al crear el usuario"})
        
    else:
        form=RegExtForm()
        return render(request, "AppMaster/register.html", {"form":form})

#@login_required
def usuario(request):
    return render (request, "AppMaster/usuario.html")
    
#@login_required
def buscaruser(request):
    return render(request, "AppMaster/buscaruser.html")

#@login_required
def buscar(request):
    print("--->",request.GET)
    if "user" in request.GET:
        user=request.GET["user"]
        print("2----------->",user)
        users=Usuario.objects.filter(username__icontains=user)
        print("3----------->",users)
        contexto={"user": users}
        return render(request,"AppMaster/resultadosBusqueda.html", contexto)
    else:
        return render(request, "AppMaster/buscaruser.html", {"mensaje":"Por favor ingresa el Usuario"})

#@login_required
def listarusuarios(request):
    users=Usuario.objects.all()
    contexto={"user":users}
    print("contexto--->", contexto)
    return render (request, "AppMaster/listarusuarios.html",contexto)

#@login_required
def eliminarUsuario(request, id):
    usuario=get_object_or_404(Usuario, id=id)
    print('-->', usuario)
    usuario.delete()
    user=Usuario.objects.all()
    print('2--->', user)
    return render(request, "AppMaster/listarusuarios.html", {"mensaje":"Usuario eliminado correctamente", "user":user})

#@login_required
def detalleUsuario(request, id):
	users = get_object_or_404(Usuario, id=id)
	return render(request, 'AppMaster/detalleUsuario.html', {'user': users})

#@login_required   
def editarUsuario(request, id):
    usuario=Usuario.objects.get(id=id)
    if request.method=="POST":
        form=UsuForm(request.POST)
        print(form)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            usuario.id=informacion['id']
            usuario.username=informacion["username"]            
            usuario.name=informacion["name"]
            usuario.lastname=informacion["lastname"]
            usuario.email=informacion["email"]
            usuario.save()
            usuarios=Usuario.objects.get(id=id)
            return render (request, "AppMaster/leerUsuario.html", {"mensaje": "Datos Modificados Correctamente!!", "usuarios":usuarios})
    else:
        form= UsuForm(initial={'id':usuario.id, "username":usuario.username,"name":usuario.name, "lastname":usuario.lastname, "email":usuario.email})
    return render(request, "AppMaster/editarUsuario.html", {"form":form, "usuario":usuario})

#------------------------------------------------------------------------------------------------------------------------
# Modulo de login

def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")

            usuario=authenticate(username=usu, password=clave)
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

#-----------------------------------------------------------------------------------------------------------------------
#Vistas para los posteos

class post_new(CreateView):
    model = Post
    success_url = reverse_lazy('post_list')
    fields=['author', 'title', 'text', 'created_date']

#@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.author
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'AppMaster/post_edit.html', {'form': form})

#@login_required
def post_detail(request, pk):
	posts = get_object_or_404(Post, pk=pk)
	return render(request, 'AppMaster/post_detail.html', {'posts': posts})

#@login_required
def post_delete(request, pk):
    post=get_object_or_404(Post, pk=pk)
    post.delete()
    posts=Post.objects.all()
    return render(request, "AppMaster/post_list.html", {"mensaje":"Post eliminado correctamente", 'posts': posts})

#@login_required
def post_list(request):
	posts = Post.objects.all()
	return render(request, 'AppMaster/post_list.html', {'posts': posts})

#---------------------------------------------------------------------------------------------------------------
#registro de Superuser

def registerSuper(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            return render(request, "AppMaster/exitoso.html", {"mensaje":f"SuperUser {username} creado correctamente"})
        else:
            return render(request, "AppMaster/registerSuper.html", {"form":form, "mensaje":"Error al crear el SuperUser"})
        
    else:
        form=RegExtForm()
        return render(request, "AppMaster/registerSuper.html", {"form":form})