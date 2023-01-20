from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, User
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.utils import timezone

# Create your views here.

#------------------------------------------------------------------------------------------------
#vistas de mensajeria

@login_required(login_url='login')
def all_messages(request):
    
    for_me = Message.objects.filter(receiver=request.user)
    from_me = Message.objects.filter(sender=request.user)
    
    context = {
        'for_me': for_me,
        'from_me':from_me,
    }
    
    return render(request, 'AppMaster/bandeja.html', context)

@login_required(login_url='login')
def new_message(request):
    if request.method == 'POST':
        
        form = Message_Form(request.POST)
        
        if form.is_valid():
            
            receiver = form.cleaned_data['receiver']
            
            try:
                user = User.objects.get(username=receiver)
                
                message = Message.objects.create()
                message.sender = str(request.user)
                message.receiver = form.cleaned_data['receiver']
                message.subject = form.cleaned_data['subject']
                message.content = str(form.cleaned_data['content'])
                message.seen = False 

                message.save()

                print('EXISTE')
                
                return redirect('all_messages')
                    
            except User.DoesNotExist:
                
                print('NO EXISTE')
                
                error_message = f"El usuario {receiver} no existe"
                form = Message_Form()
            
                return render(request, 'AppMaster/nuevo_mensaje.html',{'form':form, 'error_message':error_message})
        else:
            form = Message_Form()    
    else:
        form = Message_Form()
    
    return render(request, 'AppMaster/nuevo_mensaje.html',{'form':form})

@login_required(login_url='login')
def chat(request, id):
    message = Message.objects.get(id=id)

    message.seen = True
    message.save()


    return render(request, 'AppMaster/chat.html', {'message': message}) 

@login_required(login_url='login')
def chat_view(request, id):
    message = Message.objects.get(id=id)

    message.seen = True
    message.save()


    return render(request, 'AppMaster/chat_view.html', {'message': message}) 

@login_required(login_url='login')
def respond_message(request, receiver):
    
    mensaje = Message.objects.create(sender = request.user.username, receiver = receiver)

    if request.method == 'POST':
        form = RespondForm(request.POST, instance=mensaje)
        if form.is_valid():
            form.save()
            return redirect('all_messages')
    else:
        form = RespondForm(instance=mensaje)
        return render(request, 'AppMaster/responder_mensaje.html', {'form': form, 'receiver': receiver})