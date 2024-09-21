from django import forms
from .models import Cliente
from django.shortcuts import render
#creacion de formulario para cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        def clientes(request):
            Clientes= Cliente.objects.all()
            return render(request,'cliente.html',{'clientes': Clientes})