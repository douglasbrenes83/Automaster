from django import forms
from .models import Cliente,RegistroVehiculo,RecepcionVehiculo,Mecanico,Reparaciones,Facturas,Reparacion
from django.shortcuts import render
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