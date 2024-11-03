from django import forms
from .models import Cliente,RegistroVehiculo,RecepcionVehiculo,Mecanico,Reparaciones,Facturas,Reparacion
from django.shortcuts import render
from .models import Repuesto
from .models import Cita
from django import forms
from .models import Cita, Mecanico  # Asegúrate de importar tus modelos

class CitaForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        empty_label="Seleccione un cliente",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    mecanico = forms.ModelChoiceField(
        queryset=Mecanico.objects.all(),
        empty_label="Seleccione un mecánico",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    vehiculo = forms.ModelChoiceField(
        queryset=RegistroVehiculo.objects.all(),  # Asegúrate de usar RegistroVehiculo
        empty_label="Seleccione un vehículo",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Cita
        fields = ['cliente', 'vehiculo', 'fecha', 'hora', 'estado', 'mecanico', 'descripcion']
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción de la cita'}),
        }


class RepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = ['nombre', 'descripcion', 'cantidad_en_inventario', 'precio_unitario', 'proveedor', 'reparaciones']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del repuesto'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del repuesto'}),
            'cantidad_en_inventario': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad en inventario'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio unitario'}),
            'proveedor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del proveedor'}),
            'reparaciones': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

#creacion de formulario para cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        def clientes(request):
            Clientes= Cliente.objects.all()
            return render(request,'cliente.html',{'clientes': Clientes})

class RegistroVehiculoForm(forms.ModelForm):
    class Meta:
        model = RegistroVehiculo
        fields = ['matricula', 'modelo', 'color', 'fecha_entrada', 'hora_entrada', 'cliente']
        widgets = {
            'fecha_entrada': forms.DateInput(attrs={'type': 'date'}),
            'hora_entrada': forms.TimeInput(attrs={'type': 'time'}),
        }

class RecepcionVehiculoForm(forms.ModelForm):
    class Meta:
        model = RecepcionVehiculo
        fields = ['vehiculo', 'fecha_recepcion', 'hora_recepcion', 'estado', 'observaciones', 'reparacion']
        widgets = {
            'fecha_recepcion': forms.DateInput(attrs={'type': 'date'}),
            'hora_recepcion': forms.TimeInput(attrs={'type': 'time'}),
            'estado': forms.TextInput(attrs={'placeholder': 'Ingrese el estado'}),
            'observaciones': forms.Textarea(attrs={'placeholder': 'Ingrese observaciones', 'rows': 3}),
        }


class MecanicoForm(forms.ModelForm):
    class Meta:
        model = Mecanico
        fields = ['dni', 'nombre', 'apellidos', 'especialidad', 'telefono', 'email']
        widgets = {
            'dni': forms.TextInput(attrs={'placeholder': 'Ingrese el DNI'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre'}),
            'apellidos': forms.TextInput(attrs={'placeholder': 'Ingrese los apellidos'}),
            'especialidad': forms.TextInput(attrs={'placeholder': 'Ingrese la especialidad', 'required': 'false'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese el teléfono', 'required': 'false'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ingrese el correo electrónico', 'required': 'false'}),
        }
class ReparacionesForm(forms.ModelForm):
    class Meta:
        model = Reparaciones
        fields = ['vehiculo', 'cliente', 'fecha_inicio', 'fecha_fin', 'total_mano_de_obra', 'estatus']
        widgets = {
            'vehiculo': forms.Select(attrs={'placeholder': 'Seleccione el vehículo'}),
            'cliente': forms.Select(attrs={'placeholder': 'Seleccione el cliente'}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Fecha de inicio'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Fecha de fin'}),
            'total_mano_de_obra': forms.NumberInput(attrs={'placeholder': 'Total mano de obra'}),
            'estatus': forms.TextInput(attrs={'placeholder': 'Estatus'}),
        }
class FacturaForm(forms.ModelForm):
    class Meta:
        model = Facturas
        fields = ['reparacion', 'fecha', 'subtotal', 'iva', 'total', 'total_dolares']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'subtotal': forms.NumberInput(attrs={'class': 'form-control'}),
            'iva': forms.NumberInput(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_dolares': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(FacturaForm, self).__init__(*args, **kwargs)
        self.fields['reparacion'].widget.attrs.update({'class': 'form-control'})
   
    class ReparacionForm(forms.ModelForm):
     class Meta:
        model = Reparacion
        fields = ['nombre', 'descripcion', 'costo_estimado']  # Campos del formulario
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la reparación'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción de la reparación'}),
            'costo_estimado': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Costo estimado en NIO'}),
        }
    
    