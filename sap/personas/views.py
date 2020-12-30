from personas.models import Persona
from django.shortcuts import get_object_or_404, render

# Create your views here.

def detalle_persona(request,id):
    #persona = Persona.objects.get(pk=id)
    
    persona = get_object_or_404(Persona,pk=id)
    return render(request,'personas/detalle.html',{'persona':persona})
