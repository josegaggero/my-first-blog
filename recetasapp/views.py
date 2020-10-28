from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona 
from .forms import FormularioPersona 
from django.shortcuts import render_to_response


# Create your views here.

def lista_personas(request) :
    lista = Persona.objects.all()
    return render(request, 'recetasapp/lista_personas.html' ,{'lista' : lista})

def persona_nueva(request) :
    if request.method == 'POST' :
       formulario = FormularioPersona(request.POST)
       if formulario.is_valid() :
           persona = formulario.save(commit=False)
           persona.save()
           return render_to_response ('recetasapp/registro.html')
    else: 
         formulario = FormularioPersona()
    return render(request, 'recetasapp/persona_nueva.html',{'form' : formulario})    

    
def lista_registro(request) :
    lista1 = Usuarios.objects.all()
    return render(request, 'recetasapp/lista_registradas.html' ,{'lista1' : lista1})

