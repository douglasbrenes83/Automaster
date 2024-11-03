from django.shortcuts import render, get_object_or_404, redirect
from .models import Repuesto  # Asegúrate de que el modelo Repuesto esté importado
from .forms import RepuestoForm  # Debes crear un formulario para Repuesto
from django.contrib.auth.decorators import login_required

# Lista todos los repuestos en el inventario
@login_required
def repuesto_list(request):
    repuestos = Repuesto.objects.all()
    return render(request, 'Inventario/repuestos_list.html', {'repuestos': repuestos})

# Crear un nuevo repuesto
@login_required
def repuesto_create(request):
    if request.method == 'POST':
        form = RepuestoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('repuesto_list')
    else:
        form = RepuestoForm()
    return render(request, 'Inventario/repuestos_create.html', {'form': form})

# Actualizar un repuesto existente
@login_required
def repuesto_update(request, pk):
    repuesto = get_object_or_404(Repuesto, pk=pk)
    if request.method == 'POST':
        form = RepuestoForm(request.POST, instance=repuesto)
        if form.is_valid():
            form.save()
            return redirect('repuesto_list')
    else:
        form = RepuestoForm(instance=repuesto)
    return render(request, 'Inventario/repuestos_update.html', {'form': form})

# Eliminar un repuesto
@login_required
def repuesto_delete(request, pk):
    repuesto = get_object_or_404(Repuesto, pk=pk)
    if request.method == 'POST':
        repuesto.delete()
        return redirect('repuesto_list')
    return render(request, 'Inventario/repuestos_delete.html', {'repuesto': repuesto})
