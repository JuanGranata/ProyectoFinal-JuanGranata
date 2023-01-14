from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
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
    avatares=Avatar.objects.filter(user=request.user.id)
    return render (request, "AppMaster/inicio.html", {"imagen":avatares[0].image.url})
    #return render (request, "AppMaster/inicio.html")


# Modulo about me
def aboutme(request):
    return render (request, "AppMaster/aboutme.html")

# Modulo pagina usuario
#@login_required
def usuario(request):
    return render (request, "AppMaster/usuario.html")

# Modulo mensaje exitoso
def exitoso(request):
    return render (request, "AppMaster/exitoso.html")

    return render (request, "AppMaster/crearuser.html", {"form":formulario})

#modulo para registro de usuarios
#@login_required
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
#@login_required
def buscaruser(request):
    return render(request, "AppMaster/buscaruser.html")

# Algoritmo de busqueda de usuario
#@login_required
def buscar(request):
    print("--->",request.GET)
    if "user" in request.GET:
        user=request.GET["user"]
        print("2----------->",user)
        users=UserExt.objects.filter(username__icontains=user)
        print("3----------->",users)
        contexto={"user": users}
        return render(request,"AppMaster/resultadosBusqueda.html", contexto)
    else:
        return render(request, "AppMaster/buscaruser.html", {"mensaje":"Por favor ingresa el Usuario"})

#@login_required
def listarusuarios(request):
    users=UserExt.objects.all()
    contexto={"user":users}
    print("contexto--->", contexto)
    return render (request, "AppMaster/listarusuarios.html",contexto)

#@login_required
def eliminarUsuario(request, id):
    usuario=get_object_or_404(UserExt, id=id)
    print('-->', usuario)
    usuario.delete()
    user=UserExt.objects.all()
    print('2--->', user)
    return render(request, "AppMaster/listarusuarios.html", {"mensaje":"Usuario eliminado correctamente", "user":user})

#@login_required
def detalleUsuario(request, id):
    users = UserExt.objects.filter(id=id)
    return render(request, 'AppMaster/detalleUsuario.html', {'user': users})

#class editarUsuario(UpdateView):
#    model = UserExt
#    success_url = reverse_lazy('AppMaster/usuarios_listar')
#    fields=['usuario','nombre', 'apellido', 'email']

#@login_required
def editarUsuario(request, id):
    print("--->", id)
    #usu = UserExt.objects.get(id=id)
    usu=get_object_or_404(UserExt, id=id)
    print("2--->", usu)
    if request.method=="POST":
        #form=RegistroUsuarioForm(request.POST)
        form=RegExtForm(request.POST)
        f=RegExtForm(request.POST)
        f.errors
        print('--form error-->', f)
        if form.is_valid():
            info=form.save(commit=False)
            usu.first_name=info("first_name")
            usu.last_name=info("last_name")
            usu.email=info("email")
            #usu.password1=info("password1")
            #usu.password2=info("password1")
            usu.save()
            print("3--->", usu)
            print('--4-->', usu.id)
            #form.save()
            return redirect("AppMaster/exitoso", {'mensaje': f'cambio realizado con exito para {usu.username}'})
            
        else:
            print("---> error en el form")
            form=RegExtForm(instance = usu)
            print('-5-->', usu)
            return render(request, "AppMaster/editarUsuario.html", {'mensaje': 'hay un error en formulario', "form":form, 'id':usu.id})
    else:
        print("--GET-->", usu)
        form=RegExtForm(instance = usu)
    return render(request, "AppMaster/editarUsuario.html", {'mensaje': 'entra por GET', "form":form, 'id':usu.id})

#----- seccion de login ------
#@login_required()
def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")

            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:    
                login(request, usuario)
                return render(request, 'AppMaster/inicio.html', {'mensaje':f"Bienvenido {usu}" })
            else:
                return render(request, 'AppMaster/login.html', {'mensaje':"Usuario o contraseña incorrectos", 'form':form})

        else:
            return render(request, 'AppMaster/login.html', {'mensaje':"Usuario o contraseña incorrectos", 'form':form})

    else:
        form = AuthenticationForm()
        return render(request, "AppMaster/login.html", {"form":form})

#Vistas para los posteos

#@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.authenticate
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'AppMaster/post_edit.html', {'form': form})

#@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
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

 