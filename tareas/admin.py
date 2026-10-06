from django.contrib import admin
from .models import Usuario, Categoria, Tarea

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Tarea)