from django.contrib import admin
from .models import Cliente

# Register your models here.
# admin.py


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellidos', 'direccion', 'telefono')
    search_fields = ('nombre', 'apellidos', 'dni')

admin.site.register(Cliente, ClienteAdmin)