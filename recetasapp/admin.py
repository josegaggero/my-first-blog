from django.contrib import admin
from .models import Persona, Usuarios
from .models import Iniciar
from .models import Contraseña
from .models import Receta

# Register your models here.
admin.site.register(Persona)
admin.site.register(Usuarios)
admin.site.register(Iniciar)
admin.site.register(Contraseña)
admin.site.register(Receta)







