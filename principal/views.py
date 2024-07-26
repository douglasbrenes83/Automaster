from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

# Create your views here.

def IndexPage(request):
    return render(request, 'index.html')


def ResLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('bienvenido')  # Cambia esto al nombre de tu página principal
        else:
            # Si la autenticación falla, puedes manejarlo como quieras
            return render(request, 'login/login.html', {'error_message': 'Credenciales inválidas'})
    return render(request, 'login/login.html')
        