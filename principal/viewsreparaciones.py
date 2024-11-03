from django.shortcuts import render, get_object_or_404, redirect
from .models import Reparaciones,Reparacion
from .forms import ReparacionesForm  # Ensure you have a form for Reparaciones
from django.contrib.auth.decorators import login_required

# List all reparaciones
@login_required
def reparacion_list(request):
    reparaciones = Reparaciones.objects.all()
    return render(request, 'Reparaciones/reparacion_list.html', {'reparaciones': reparaciones})

# Create a new reparacion
@login_required
def reparacion_create(request):
    if request.method == 'POST':
        form = ReparacionesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reparacion_list')
    else:
        form = ReparacionesForm()
    return render(request, 'Reparaciones/reparacion_create.html', {'form': form})

# Update an existing reparacion
@login_required
def reparacion_update(request, pk):
    reparacion = get_object_or_404(Reparaciones, pk=pk)
    if request.method == 'POST':
        form = ReparacionesForm(request.POST, instance=reparacion)
        if form.is_valid():
            form.save()
            return redirect('reparacion_list')
    else:
        form = ReparacionesForm(instance=reparacion)
    return render(request, 'Reparaciones/reparacion_update.html', {'form': form})

# Delete a reparacion
@login_required
def reparacion_delete(request, pk):
    reparacion = get_object_or_404(Reparaciones, pk=pk)
    if request.method == 'POST':
        reparacion.delete()
        return redirect('reparacion_list')
    return render(request, 'Reparaciones/reparacion_delete.html', {'reparacion': reparacion})

def repar_list(request):
    reparaciones = Reparacion.objects.all()
    return render(request, 'Reparacion/repar_list.html', {'reparaciones': reparaciones})
