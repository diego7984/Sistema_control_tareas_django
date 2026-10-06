from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'tareas', views.TareaViewSet)


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("api/", include(router.urls)),
]