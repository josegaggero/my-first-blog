from django import forms

from .models import Persona, Iniciar, Contraseña, Receta

class FormularioReceta(forms.ModelForm):
     class Meta:
       model = Receta
       fields = ('titulo','advertencia','ingrdientes','intrucciones','imagen')

class FormularioContraseña(forms.ModelForm) :
     class Meta:
       model = Contraseña
       fields = ('contraseña1','contraseña2') 

class FormularioPersona(forms.ModelForm) :
     class Meta:
       model = Persona
       fields = ('nombre', 'apellido', 'email', 'pais')


class FormularioInicio(forms.ModelForm) :
     class Meta:
       model = Iniciar
       fields = ('mail', 'clave')


