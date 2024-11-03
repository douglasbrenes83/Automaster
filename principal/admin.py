from django.contrib import admin
from .models import Cliente,RegistroVehiculo,RecepcionVehiculo,Facturas

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
    
@admin.register(RecepcionVehiculo)
class RecepcionVehiculoAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'fecha_recepcion', 'hora_recepcion', 'estado', 'reparacion')  # Campos que se mostrarán en la lista
    list_filter = ('fecha_recepcion', 'estado')  # Filtros por fecha y estado
    search_fields = ('vehiculo__matricula', 'vehiculo__modelo', 'estado')  # Campos para la búsqueda
    list_per_page = 20  # Número de elementos por página

    fieldsets = (
        (None, {
            'fields': ('vehiculo', 'fecha_recepcion', 'hora_recepcion', 'estado', 'observaciones', 'reparacion')
        }),
    )
    ordering = ('-fecha_recepcion',)  # Orden por fecha de recepción (descendente)
    from django.contrib import admin
from .models import Mecanico

class MecanicoAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellidos', 'especialidad', 'telefono', 'email')
    search_fields = ('nombre', 'apellidos', 'dni', 'especialidad')

# Registra el modelo y su admin
admin.site.register(Mecanico, MecanicoAdmin)

class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'reparacion', 'fecha', 'subtotal', 'iva', 'total', 'total_dolares')
    search_fields = ('reparacion__id', 'fecha')
    list_filter = ('fecha',)
    ordering = ('fecha',)

admin.site.register(Facturas, FacturaAdmin)
