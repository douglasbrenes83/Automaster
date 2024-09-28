from django.shortcuts import render,redirect,get_object_or_404
from .models import RegistroVehiculo,RecepcionVehiculo, Reparaciones
from django.contrib.auth.decorators import login_required
from .forms import RegistroVehiculoForm
from .forms import RecepcionVehiculoForm


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
@login_required
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

# Crear una nueva recepción de vehículo
def nueva_recepcion(request):
    if request.method == 'POST':
        form = RecepcionVehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Autos/listar_recepciones')  # Cambia al nombre de tu vista de listado
    else:
        form = RecepcionVehiculoForm()
    
    return render(request, 'Autos/nueva_recepcion.html', {'form': form})

# Actualizar una recepción de vehículo
def actualizar_recepcion(request, recepcion_id):
    recepcion = get_object_or_404(RecepcionVehiculo, id=recepcion_id)
    
    if request.method == 'POST':
        form = RecepcionVehiculoForm(request.POST, instance=recepcion)
        if form.is_valid():
            form.save()
            return redirect('Autos/listar_recepciones')  # Cambia al nombre de tu vista de listado
    else:
        form = RecepcionVehiculoForm(instance=recepcion)
    
    return render(request, 'Autos/actualizar_recepcion.html', {'form': form, 'recepcion': recepcion})

# Eliminar una recepción de vehículo
def eliminar_recepcion(request, recepcion_id):
    recepcion = get_object_or_404(RecepcionVehiculo, id=recepcion_id)
    
    if request.method == 'POST':
        recepcion.delete()
        return redirect('Autos/listar_recepciones')  # Cambia al nombre de tu vista de listado
    
    return render(request, 'eliminar_recepcion.html', {'recepcion': recepcion})

# Listar todas las recepciones de vehículo
def listar_recepciones(request):
    recepciones = RecepcionVehiculo.objects.all()
    return render(request, 'Autos/listar_recepciones.html', {'recepciones': recepciones})
