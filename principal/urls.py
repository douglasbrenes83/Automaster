from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage, name='index'),  # Ruta para la página principal
    path('login/', views.Reslogin, name='login'),
]
