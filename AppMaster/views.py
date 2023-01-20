from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import PostForm, ProfileEditForm, UserRegisterForm
from AppMaster.forms import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.edit import UpdateView

# Create your views here.

@login_required(login_url='login')
def agregarAvatarSuper(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)#ademas del post, como trae archivos (yo se que trae archivos xq conozco el form, tengo q usar request.files)
        if form.is_valid():
            print('-- user-->', request.user)
            avatarViejo=AvatarSuper.objects.filter(user=request.user)
            if len(avatarViejo)!=0:
                avatarViejo[0].delete()
            avatar=AvatarSuper(user=request.user, imagen=request.FILES["imagen"])
            avatar.save()
            return render(request, "AppMaster/inicio.html", {"mensaje":"Avatar agregado correctamente"})
        else:
            return render(request, "AppMaster/AgregarAvatarSuper.html", {"form": form, "user": request.user})
    else:
        form=AvatarForm()
        return render(request , "AppMaster/AgregarAvatarSuper.html", {"form": form, "user": request.user})


# Modulo de inicio
#@login_required
def inicio(request):
    #usuario = (request.user)
    #print('--usuario-->', usuario.profile.user)
    #imagen=Profile.objects.filter(user=usuario)
    #print('--imagen-->', imagen)
    # if usuario != None:
    #     imagen=Profile.objects.filter(user=usuario)
    #     avatar=imagen[0].avatar

    # else:
    #     avatar = "media/avatares/avatarpordefecto.png"
    return render (request, "AppMaster/inicio.html")#, {"avatar":avatar})

# Modulo about me
def aboutme(request):
    return render (request, "AppMaster/aboutme.html")

# Modulo mensaje exitoso
def exitoso(request):
    return render (request, "AppMaster/exitoso.html")


#---------------------------------------------------------------------------------------------------------------------
# Modulo para registro de usuarios

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            print("--form valido--")
            username=form.cleaned_data.get("username")
            form.save()
            usuario = User.objects.get(username=username)
            profile = Profile.objects.create(user = usuario)
            profile.save()

            form2 = AuthenticationForm()
            print('--> sale a login_request')
            return render(request,"AppMaster/login_request.html", {'mensaje2': "Usuario creado correctamente", 'form': form2 })
        else:
            print('--error de form--')
            form = UserRegisterForm()
            mensaje = "Los datos ingresados no son validos"
        
        
    else:
        print('--form x GET--')
        form=UserRegisterForm()
    return render(request, "AppMaster/register.html", {"form":form})

@login_required(login_url='login')
def usuario(request):
    return render (request, "AppMaster/usuario.html")
    
@login_required(login_url='login')
def buscaruser(request):
    return render(request, "AppMaster/buscaruser.html")

@login_required(login_url='login')
def buscar(request):
    print("--->",request.GET)
    if "user" in request.GET:
        usu=request.GET["user"]
        print("2----------->",usu)
        users=UserExt.objects.filter(username__icontains=usu)
        #print("3----------->",users)
        contexto={"user": users}
        return render(request,"AppMaster/resultadosBusqueda.html", contexto)
    else:
        return render(request, "AppMaster/buscaruser.html", {"mensaje":"Por favor ingresa el Usuario"})

@login_required(login_url='login')
def listarusuarios(request):
    users=UserExt.objects.all()
    contexto={"user":users}
    # print("contexto--->", contexto)
    return render (request, "AppMaster/listarusuarios.html", contexto)

@login_required(login_url='login')
def eliminarUsuario(request, id):
    usuario=get_object_or_404(User, id=id)
    print('-->', usuario)
    usuario.delete()
    user=User.objects.all()
    print('2--->', user)
    return render(request, "AppMaster/listarusuarios.html", {"mensaje":"Usuario eliminado correctamente", "user":user})

@login_required(login_url='login')
def detalleUsuario(request, id):
	users = get_object_or_404(UserExt, id=id)
	return render(request, 'AppMaster/detalleUsuario.html', {'user': users})


@login_required(login_url='login')
def editarUsuario(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            
            return render(request, 'AppMaster/profile_edit.html', {"usuarios":usuario} )
        
    else:
        form = UserEditForm(instance=usuario)
    
    return render(request, 'AppMaster/profile_edit.html', {'form': form, 'usuario':usuario, 'email':usuario.email})

@login_required(login_url='login')
def profile(request):
    usuario = request.user
    
    if usuario.profile.avatar:
        avatar = usuario.profile.avatar
    else:
        avatar = "avatares/avatar2.png"

    context = {
        'username': usuario.username,
        'email': usuario.email,
        'avatar': avatar,
        'bio': usuario.profile.bio,
        'website': usuario.profile.website,
    }
    
    return render(request, 'AppMaster/profile.html', context)

@login_required(login_url='login')
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=profile)
        return render(request, 'AppMaster/profile_edit.html', {'form': form})
#------------------------------------------------------------------------------------------------------------------------

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            
            user = authenticate(username = usuario, password = contrasenia)

            if user is not None:
                login(request,user)
                return redirect('inicio')
            
            else:
                form = AuthenticationForm()
                return render(request,"AppMaster/login_request.html", {'mensaje': "Usuario o contrasenia incorrectos 1", 'form':form} )

        else:
            form = AuthenticationForm()
            return render(request,"AppMaster/login_request.html", {'mensaje': "Usuario o contrasenia incorrectos 2", 'form': form} )

    else:

        form = AuthenticationForm()
        return render(request, 'AppMaster/login_request.html', {'form':form})

#-----------------------------------------------------------------------------------------------------------------------
#Vistas para los posteos

class post_new(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy('post_list')
    fields=('author','title', 'text', 'created_date')

@login_required(login_url='login')
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

#@login_required(login_url='login')
def post_detail(request, pk):
	posts = get_object_or_404(Post, pk=pk)
	return render(request, 'AppMaster/post_detail.html', {'posts': posts})

@login_required(login_url='login')
def post_delete(request, pk):
    post=get_object_or_404(Post, pk=pk)
    post.delete()
    posts=Post.objects.all()
    return render(request, "AppMaster/post_list.html", {"mensaje":"Post eliminado correctamente", 'posts': posts})

#@login_required(login_url='login')
def post_list(request):
	posts = Post.objects.all()
	return render(request, 'AppMaster/post_list.html', {'posts': posts})

#---------------------------------------------------------------------------------------------------------------
