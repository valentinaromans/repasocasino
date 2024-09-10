from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sepulveda(request):
    html = """
        <h1>Bienvenido a la página principal 'Sepúlveda'</h1>
    """
    return HttpResponse(html)

def danitza(request):
    html = """
        <h6>Hola, esta es la segunda página 'Danitza'</h6>
    """
    return HttpResponse(html)
