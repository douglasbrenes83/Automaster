from django.shortcuts import render,redirect,get_object_or_404
from .models import RegistroVehiculo
from .forms import RegistroVehiculoForm

#vista lista de autos
def vehiculo_list(request):
    vehiculos = RegistroVehiculo.objects.all()
    return render(request, 'Autos/vehiculo_list.html', {'vehiculos': vehiculos})
#crear vehiculo
def vehiculo_create(request):
    if request.method == 'POST':
        form = RegistroVehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculo_list')  # Redirige a la lista después de crear el vehículo
    else:
        form = RegistroVehiculoForm()
    
    return render(request, 'Autos/vehiculo_form.html', {'form': form})
#update vehiculo
def actualizar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(RegistroVehiculo, id=vehiculo_id)
    
    if request.method == 'POST':
        form = RegistroVehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('vehiculo_list')  # Cambia a la URL que desees
    else:
        form = RegistroVehiculoForm(instance=vehiculo)

    return render(request, 'Autos/actualizar_vehiculo.html', {'form': form, 'vehiculo': vehiculo})

#eliminar vehiculo
def eliminar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(RegistroVehiculo, id=vehiculo_id)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('listar_vehiculos')  # Redirige a una vista de lista después de eliminar
    return render(request, 'Autos/vehiculo_list.html', {'vehiculo': vehiculo})