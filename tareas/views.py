from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>Bienvenido al Sistema de Control de Tareas</h1>")
