from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


from .models import Usuario, Categoria, Tarea
from .serializers import (
    UsuarioSerializer,
    CategoriaSerializer,
    TareaSerializer
)


# Vistas de la aplicación
def inicio(request):
    return render(request, "tareas/inicio.html")


def error_404(request, exception):
    return render(request, "tareas/404.html", status=404)


# API REST
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

@login_required
def panel_privado(request):
    return render(request, "tareas/panel_privado.html")

class PanelTareasView(LoginRequiredMixin, TemplateView):
    template_name = "tareas/panel_tareas.html"