from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cita
from .forms import CitaForm  # Asegúrate de tener un formulario para Cita

# Lista todas las citas
@login_required
def cita_list(request):
    citas = Cita.objects.all()
    return render(request, 'Cita/cita_list.html', {'citas': citas})

# Crea una nueva cita



def cita_create(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cita_list')  # Redirige a la lista de citas después de crear
    else:
        form = CitaForm()
    
    return render(request, 'Cita/cita_create.html', {'form': form})  # Asegúrate de proporcionar la ruta correcta# Asegúrate de usar el nombre correcto de la plantilla


# Actualiza una cita existente

def cita_update(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()  # Guarda los cambios en la cita
            return redirect('cita_list')  # Redirige a la lista de citas después de actualizar
    else:
        form = CitaForm(instance=cita)  # Pre-carga el formulario con la información de la cita existente

    return render(request, 'Cita/cita_update.html', {'form': form, 'title': 'Actualizar Cita'})

# Elimina una cita
@login_required
def cita_delete(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita.delete()
        return redirect('cita_list')
    return render(request, 'Cita/cita_delete.html', {'cita': cita})
