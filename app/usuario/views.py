from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

def reportes(request):
    usuarios=Usuario.objects.all()
    return render(request, 'reportes.html', {'usuarios': usuarios})

def usuarios(request):
    usuarios=Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})
