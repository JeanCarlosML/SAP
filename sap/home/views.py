from personas.models import Persona
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    
    #Para acceder a la cantidad de registros de un Modelo se usa el metodo count()
    #n0_personas = Persona.objects.count()
    personas = Persona.objects.all()
    # Para trabajar de manera dinamica los templates
    # Podemos usar el metodo render que recibe el objeto request
    # Despues el nombre de la plantilla que debe estar por defecto
    # en la carpeta templates dentro de cada app
    # Ademas el diccionario de variables
    return render(request, "home.html", {"personas": personas})
