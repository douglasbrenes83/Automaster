from django import forms
from .models import Cliente,RegistroVehiculo
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