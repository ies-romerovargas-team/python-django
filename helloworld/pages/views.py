# from django.shortcuts import render
from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse("¡Hola mundo!")

def about_page_view(request):
    return HttpResponse("¡About us!")

# En python, las funciones separan las palabras con el caracter subrayado, y las clases con CamelKey

