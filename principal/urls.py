from django.urls import path
from . import views
from . import viewsauto

urlpatterns = [
    #urls
    path('', views.IndexPage, name='index'),  # Ruta para la página principal
    path('Contacto/', views.contact, name='contacto'),
    path('login/', views.ResLogin, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/new/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('clientes/edit/', views.cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/delete/', views.cliente_delete, name='cliente_delete'),
    path('vehiculos/', viewsauto.vehiculo_list, name='vehiculo_list'),
    path('vehiculos/new/',viewsauto.vehiculo_create, name='vehiculo_create'),
    path('vehiculos/actualizar/<int:vehiculo_id>/', viewsauto.actualizar_vehiculo, name='actualizar_vehiculo'),
    path('vehiculos/eliminar/<int:vehiculo_id>/', viewsauto.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('recepciones/', viewsauto.listar_recepciones, name='listar_recepciones'),
    path('recepciones/new/', viewsauto.nueva_recepcion, name='nueva_recepcion'),
    path('recepciones/actualizar/<int:recepcion_id>/', viewsauto.actualizar_recepcion, name='actualizar_recepcion'),
    path('recepciones/eliminar/<int:recepcion_id>/', viewsauto.eliminar_recepcion, name='eliminar_recepcion'),

]
