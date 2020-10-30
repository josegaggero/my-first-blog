from django.urls import path, include
from.import views

urlpatterns = [

    path('', views.lista_personas, name='lista_personas'),
    path('persona/nueva', views.persona_nueva, name='persona_nueva'),
    path('registrado', views.lista_registro, name='lista_registro'),

  
]
