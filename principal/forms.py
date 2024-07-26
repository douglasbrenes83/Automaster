from django import forms
from .models import Cliente

#creacion de formulario para cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'