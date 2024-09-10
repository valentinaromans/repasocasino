from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ignacio(request):
    return HttpResponse("Hola, este es el inicio de la app.")

def garrido(request):
    return HttpResponse("Hola, esta es la binevenida de la app.")