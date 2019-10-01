from django.shortcuts import render
from django.http import HttpResponse
from .models import Formulario
from .forms import FormularioForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

def index(request):
    formulario = Formulario.objects.all()
    contexto = {'formularios':formulario}
    return render(request, 'index.html', contexto)


def formulario_create(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = FormularioForm()
    return render(request, 'formulario_create.html', {'form':form})


def formulario_edit(request, id_formulario):
    formulario = Formulario.objects.filter(id=id_formulario).first()
    if request.method == 'GET':
        form = FormularioForm(instance=formulario)
    else:
        form = FormularioForm(request.POST, instance=formulario)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request, 'formulario_create.html', {'form':form})


def formulario_delete(request, id_formulario):
    formulario = Formulario.objects.filter(id=id_formulario).first()
    if request.method == 'POST':
        formulario.delete()
        return redirect('index')
    return render(request, 'formulario_delete.html', {'formulario':formulario})
