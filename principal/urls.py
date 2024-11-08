from django.urls import path
from . import views
from . import viewsauto
from . import viewsmecanico
from . import viewsreparaciones
from . import viewsfactura
from . import viewsinventario  
from . import viewscita


urlpatterns = [
    #urls
    path('', views.IndexPage, name='index'),  # Ruta para la página principal
    path('admin', views.IndexPage, name='admin'),  # Ruta para la página principal
    path('Contacto/', views.contact, name='contacto'),
    path('login/', views.ResLogin, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/new/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('clientes/edit/<int:pk>/', views.cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/delete/', views.cliente_delete, name='cliente_delete'),
    path('vehiculos/', viewsauto.vehiculo_list, name='vehiculo_list'),
    path('vehiculos/new/',viewsauto.vehiculo_create, name='vehiculo_create'),
    path('vehiculos/actualizar/<int:vehiculo_id>/', viewsauto.actualizar_vehiculo, name='actualizar_vehiculo'),
    path('vehiculos/eliminar/<int:vehiculo_id>/', viewsauto.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('recepciones/', viewsauto.listar_recepciones, name='listar_recepciones'),
    path('recepciones/new/', viewsauto.nueva_recepcion, name='nueva_recepcion'),
    path('recepciones/actualizar/<int:recepcion_id>/', viewsauto.actualizar_recepcion, name='actualizar_recepcion'),
    path('recepciones/eliminar/<int:recepcion_id>/', viewsauto.eliminar_recepcion, name='eliminar_recepcion'),
    path('Mecanicos/', viewsmecanico.mecanico_list, name='mecanico_list'),
    path('Mecanicos/new/', viewsmecanico.mecanico_create, name='mecanico_create'),
    path('Mecanicos/update/<int:pk>/edit/', viewsmecanico.mecanico_update, name='mecanico_update'),
    path('Mecanicos/<int:pk>/delete/', viewsmecanico.mecanico_delete, name='mecanico_delete'),
    path('Reparaciones/', viewsreparaciones.reparacion_list, name='reparacion_list'),
    path('Reparaciones/new/', viewsreparaciones.reparacion_create, name='reparacion_create'),
    path('Reparaciones/update/<int:pk>/edit/', viewsreparaciones.reparacion_update, name='reparacion_update'),
    path('Reparaciones/<int:pk>/delete/', viewsreparaciones.reparacion_delete, name='reparacion_delete'),
    path('Facturas/', viewsfactura.factura_list, name='factura_list'),
    path('Facturas/new/', viewsfactura.factura_create, name='factura_create'),
    #path('Facturas/update/<int:pk>/edit/', viewsfactura.factura_update, name='factura_update'),
    #path('Facturas/<int:pk>/delete/', viewsfactura.factura_delete, name='factura_delete')
    path('Reparacion/', viewsreparaciones.repar_list, name='repar_list'),
    path('Inventario/', viewsinventario.repuesto_list, name='repuesto_list'),           # Listar repuestos
    path('Inventario/nuevo/', viewsinventario.repuesto_create, name='repuesto_create'),  # Crear un nuevo repuesto
    path('Inventario/<int:pk>/editar/', viewsinventario.repuesto_update, name='repuesto_update'),  # Actualizar un repuesto
    path('Inventario/<int:pk>/eliminar/', viewsinventario.repuesto_delete, name='repuesto_delete'),  # Eliminar un repuesto
    path('Citas/', viewscita.cita_list, name='cita_list'),  # Lista de citas
    path('Citas/nueva/', viewscita.cita_create, name='cita_create'),  # Crear nueva cita
    path('Citas/<int:pk>/editar/', viewscita.cita_update, name='cita_update'),  # Editar cita existente
    path('Citas/<int:pk>/eliminar/', viewscita.cita_delete, name='cita_delete'),  # Eliminar cita

]
