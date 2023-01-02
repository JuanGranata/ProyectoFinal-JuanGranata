from django.shortcuts import render

# Create your views here.

# Modulo de inicio
def inicio(request):
    return render (request, "AppMaster/inicio.html")

# Modulo mensaje exitoso
def exitoso(request):
    return render (request, "AppMaster/exitoso.html")