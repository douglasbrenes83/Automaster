from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Mecanico
from .forms import MecanicoForm  # Asegúrate de crear un formulario para Mecanico

# Lista todos los mecánicos
def mecanico_list(request):
    Mecanicos = Mecanico.objects.all()
    return render(request, 'mecanicos/mecanico_list.html', {'Mecanicos': Mecanicos})

# Crea un nuevo mecánico
def mecanico_create(request):
    if request.method == 'POST':
        form = MecanicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mecanico_list')
    else:
        form = MecanicoForm()
    return render(request, 'mecanicos/mecanico_create.html', {'form': form})


# Actualiza un mecánico existente
def mecanico_update(request, pk):
    mecanico = get_object_or_404(Mecanico, pk=pk)
    if request.method == 'POST':
        form = MecanicoForm(request.POST, instance=mecanico)
        if form.is_valid():
            form.save()
            return redirect('mecanico_list')
    else:
        form = MecanicoForm(instance=mecanico)
    return render(request, 'mecanicos/mecanico_update.html', {'form': form})

# Elimina un mecánico
def mecanico_delete(request, pk):
    mecanico = get_object_or_404(Mecanico, pk=pk)
    if request.method == 'POST':
        mecanico.delete()
        return redirect('mecanico_list')
    return render(request, 'mecanicos/mecanico_delete.html', {'mecanico': mecanico})
