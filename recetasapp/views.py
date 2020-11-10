from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona , Iniciar, Contraseña, Receta
from .forms import FormularioPersona, FormularioInicio, FormularioContraseña, FormularioReceta
from django.shortcuts import render_to_response


# Create your views here.

########----Recetas----########
def recetas(request) :
    if request.method == 'POST' :
       formulario3 = FormularioReceta(request.POST , request.FILES)
       if formulario3.is_valid() :
           receta = formulario3.save(commit=False)
           receta.save()
           return render_to_response ('recetasapp/contraseña1.html')
    else: 
         formulario3 = FormularioReceta()       
    return render(request, 'recetasapp/recetas.html',{'form' : formulario3})


def lista_recetas(request) :
    lista3 = Receta.objects.all()
    return render(request, 'recetasapp/lista_recetas.html' ,{'lista3' : lista3})

###############################




#####Recuperar contraseña ######

def contraseña(request) :
    if request.method == 'POST' :
       formulario2 = FormularioContraseña(request.POST)
       if formulario2.is_valid() :
           contraseñas = formulario2.save(commit=False)
           contraseñas.save()
           return render_to_response ('recetasapp/contraseña1.html')
    else: 
         formulario2 = FormularioContraseña()       
    return render(request, 'recetasapp/contraseña.html',{'form' : formulario2})


def lista_contraseña(request) :
    lista2 = Contraseña.objects.all()
    return render(request, 'recetasapp/lista_contraseña.html' ,{'lista2' : lista2})

###########


###################
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
###################


#########Ingresar##########
def formulario_inicio(request):
    if request.method == 'POST' :
       formulario =  FormularioInicio(request.POST)
       if formulario.is_valid() :
           persona = formulario.save(commit=False)
           persona.save()
           return render_to_response ('recetasapp/registro.html')
    else: 
         formulario = FormularioInicio()       

    return render(request, "recetasapp/form.html",{'form' : formulario})
###########################







# Mi pagina web
def iniciar(request):
    return render(request, "recetasapp/paises.html")


def chile(request):
    return render(request, "recetasapp/chile.html")   

def inicio(request):
    return render(request, "recetasapp/index.html")
# fin


def lista_registro(request) :
    lista1 = Iniciar.objects.all()
    return render(request, 'recetasapp/lista_registradas.html' ,{'lista1' : lista1})

