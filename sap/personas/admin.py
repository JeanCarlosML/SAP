from django.contrib import admin

# Register your models here.
from personas.models import Domicilio
from personas.models import Persona

admin.site.register(Persona)

admin.site.register(Domicilio)