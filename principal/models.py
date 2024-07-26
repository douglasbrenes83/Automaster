from django.db import models
# Create your models here.

class Cliente(models.Model):
    dni = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
    
class RegistroVehiculo(models.Model):
    matricula = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    fecha_entrada = models.DateField()
    hora_entrada = models.TimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='vehiculos')

    def __str__(self):
        return f"{self.modelo} ({self.matricula})"
    
class Mecanico(models.Model):
    dni = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class AsignacionMecanico(models.Model):
    vehiculo = models.ForeignKey(RegistroVehiculo, on_delete=models.CASCADE, related_name='asignaciones')
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE, related_name='asignaciones')
    fecha_asignacion = models.DateField()

    def __str__(self):
        return f"{self.mecanico} - {self.vehiculo} ({self.fecha_asignacion})"


class Reparaciones(models.Model):
    vehiculo = models.ForeignKey(RegistroVehiculo, on_delete=models.CASCADE, related_name='reparaciones')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reparaciones')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    total_mano_de_obra = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    estatus = models.CharField(max_length=20)

    def __str__(self):
        return f"Reparación {self.id} - {self.estatus}"


class GestionRepuesto(models.Model):
    nombre = models.CharField(max_length=50)
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class RepuestoReparacion(models.Model):
    reparacion = models.ForeignKey(Reparaciones, on_delete=models.CASCADE, related_name='repuestos')
    repuesto = models.ForeignKey(GestionRepuesto, on_delete=models.CASCADE, related_name='reparaciones')
    cantidad = models.IntegerField()

    class Meta:
        unique_together = ('reparacion', 'repuesto')

    def __str__(self):
        return f"{self.repuesto} - {self.cantidad}"


class RecepcionVehiculo(models.Model):
    vehiculo = models.ForeignKey(RegistroVehiculo, on_delete=models.CASCADE, related_name='recepciones')
    fecha_recepcion = models.DateField()
    hora_recepcion = models.TimeField()
    estado = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=255, blank=True, null=True)
    reparacion = models.ForeignKey(Reparaciones, on_delete=models.SET_NULL, null=True, blank=True, related_name='recepciones')

    def __str__(self):
        return f"{self.vehiculo} - {self.fecha_recepcion}"


class Facturas(models.Model):
    reparacion = models.ForeignKey(Reparaciones, on_delete=models.CASCADE, related_name='facturas')
    fecha = models.DateField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    total_dolares = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Factura {self.id} - {self.fecha}"


class DetalleFactura(models.Model):
    factura = models.ForeignKey(Facturas, on_delete=models.CASCADE, related_name='detalles')
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.descripcion} - {self.monto}"


class RepuestoFactura(models.Model):
    factura = models.ForeignKey(Facturas, on_delete=models.CASCADE, related_name='repuestos')
    repuesto = models.ForeignKey(GestionRepuesto, on_delete=models.CASCADE, related_name='facturas')
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.repuesto} - {self.cantidad} a {self.precio_unitario}"


class Reservas(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')
    vehiculo = models.ForeignKey(RegistroVehiculo, on_delete=models.CASCADE, related_name='reservas')
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    especialidad = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return f"Reserva {self.id} - {self.fecha_reserva} ({self.estado})"


