from django.contrib import admin
from .models import Cliente,RegistroVehiculo

# Register your models here.
# admin.py


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellidos', 'direccion', 'telefono')
    search_fields = ('nombre', 'apellidos', 'dni')

admin.site.register(Cliente, ClienteAdmin)

@admin.register(RegistroVehiculo)
class RegistroVehiculoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'modelo', 'color', 'fecha_entrada', 'hora_entrada', 'cliente')
    search_fields = ('matricula', 'modelo', 'cliente__nombre')  # Asumiendo que Cliente tiene un campo 'nombre'
    list_filter = ('fecha_entrada', 'color')

    def __str__(self):
        return f"{self.modelo} ({self.matricula})"
  