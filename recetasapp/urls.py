from django.urls import path, include
from.import views

urlpatterns = [
    path('', views.lista_personas, name='lista_personas'),
    path('nueva', views.persona_nueva, name='nueva'),
    path('registrado', views.lista_registro, name='lista_registro'),
    path('paises', views.iniciar, name='paises'),
    path('chile', views.chile, name='chile'),
    path('inicio', views.inicio, name='inicio'),
    ###################
    path('formulario', views.formulario_inicio, name='formulario_inicio'),
    ###########
    path('lista_contraseña' ,views.lista_contraseña, name='lista_contraseña'),
    path('forms', views.contraseña, name='forms'),
    #######Reecetas######
    path('lista_recetas' , views.lista_recetas, name='lista_recetas'),
    path('recetas1',views.recetas )
    
    
]
