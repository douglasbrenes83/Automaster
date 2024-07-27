from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage, name='index'),  # Ruta para la página principal
    path('Contacto/', views.contact, name='contacto'),
    path('login/', views.ResLogin, name='login'),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/new/',views.cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('clientes/<int:pk>/edit/', views.cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/delete/', views.cliente_delete, name='cliente_delete'),
]
