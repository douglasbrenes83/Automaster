from django import forms
from .models import Cliente,RegistroVehiculo,RecepcionVehiculo
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

    