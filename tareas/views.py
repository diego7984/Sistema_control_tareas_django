from django.shortcuts import render

def inicio(request):
    return render(request, "tareas/inicio.html")

def error_404(request, exception):
    return render(request, "tareas/404.html", status=404)