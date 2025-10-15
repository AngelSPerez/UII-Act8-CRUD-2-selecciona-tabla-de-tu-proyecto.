from django.shortcuts import render, get_object_or_404, redirect
from .models import Empleados
from .forms import EmpleadosForm

def index(request):
    empleados = Empleados.objects.all()
    return render(request, 'index.html', {'empleados': empleados})

def ver_empleado(request, id):
    empleado = get_object_or_404(Empleados, pk=id)
    return render(request, 'ver_empleado.html', {'empleado': empleado})

def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EmpleadosForm()
    return render(request, 'agregar_empleado.html', {'form': form})

def editar_empleado(request, id):
    empleado = get_object_or_404(Empleados, pk=id)
    if request.method == 'POST':
        form = EmpleadosForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EmpleadosForm(instance=empleado)
    return render(request, 'editar_empleado.html', {'form': form, 'empleado': empleado})

def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleados, pk=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('inicio')
    return render(request, 'borrar_empleado.html', {'empleado': empleado})