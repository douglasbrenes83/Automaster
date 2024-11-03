from django.shortcuts import render, redirect, get_object_or_404
from .models import Facturas, Reparaciones
from .forms import FacturaForm  # Asegúrate de tener un formulario para Factura
from django.contrib import messages

# Vista para listar facturas
def factura_list(request):
    facturas = Facturas.objects.all().order_by('-fecha')  # Obtener todas las facturas
    return render(request, 'Facturas/factura_list.html', {'facturas': facturas})

# Vista para crear una nueva factura
def factura_create(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Factura registrada exitosamente.")
            return redirect('Faturas/factura_list')  # Redirige a la lista de facturas
    else:
        form = FacturaForm()
    return render(request, 'Facturas/factura_create.html', {'form': form})

# Vista para ver los detalles de una factura específica
def factura_detail(request, factura_id):
    factura = get_object_or_404(Facturas, id=factura_id)
    return render(request, 'factura_detail.html', {'factura': factura})

# Vista para editar una factura
def factura_edit(request, factura_id):
    factura = get_object_or_404(Facturas, id=factura_id)
    if request.method == 'POST':
        form = FacturaForm(request.POST, instance=factura)
        if form.is_valid():
            form.save()
            messages.success(request, "Factura actualizada exitosamente.")
            return redirect('factura_list')  # Redirige a la lista de facturas
    else:
        form = FacturaForm(instance=factura)
    return render(request, 'factura_edit.html', {'form': form, 'factura': factura})
