from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import MsgForm
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

# Modulo de inicio
def inicio(request):
    return render (request, "AppMaster/inicio.html")

# Modulo mensaje exitoso
def exitoso(request):
    return render (request, "AppMaster/exitoso.html")

#-------------Mensajes------------------

@login_required
def msg_new(request):
    if request.method == "POST":
        form = MsgForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.userto = form.cleaned_data.get("userto")
            msg.userfrom = request.user
            msg.subject = form.cleaned_data.get("subject")
            msg.text = form.cleaned_data.get("text")
            msg.published_date = timezone.now()
            msg.save()
            return redirect('msg_detail', pk=msg.pk)
    else:
        form = MsgForm()
        return render(request, 'AppMaster/msg_edit.html', {'form': form})

@login_required
def msg_list(request):
    user = request.user
    print('--->', user)
    msgs = Msg.objects.filter(userto=user)
    return render(request, 'AppMaster/msg_list.html', {'msgs': msgs})

@login_required
def msg_edit(request, pk):
    #msg = get_object_or_404(Msg, pk=pk)
    msg = Msg.objects.get(pk=pk)
    if request.method == "POST":
        form = MsgForm(instance=msg)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.userto = form.cleaned_data.get("userto")
            msg.userfrom = form.cleaned_data.get("userfrom")
            msg.subject = form.cleaned_data.get("subject")
            msg.text = form.cleaned_data.get("text")
            msg.published_date = form.cleaned_data.get("published_date")
            msg.save()
            print('--editar POST-->', msg.pk)
            return redirect('msg_detail', msg.pk)
    else:
        form = MsgForm(instance=msg)
        return render(request, 'AppMaster/msg_edit.html', {'form': form})

@login_required
def msg_detail(request, pk):
	#msgs = get_object_or_404(Msg, userto=user)
    msgs = Msg.objects.filter(pk=pk)
    print('--detail-->', pk)
    return render(request, 'AppMaster/msg_detail.html', {'msgs': msgs})

@login_required
def msg_delete(request, pk):
    msg=get_object_or_404(Msg, pk=pk)
    msg.delete()
    msgs=Msg.objects.all()
    return render(request, "AppMaster/msg_list.html", {"mensaje":"Mensaje eliminado correctamente", 'msgs': msgs})