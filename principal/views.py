from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Cliente
from .forms import ClienteForm

# Create your views here.

def IndexPage(request):
    return render(request, 'index.html')


def contact(request):
    return render(request,'IndexPrincipal/indexContact.html')


def ResLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirige a la página principal, asume que tienes una URL con nombre 'home'
        else:
            return render(request, 'login/login.html', {'error_message': 'Credenciales inválidas'})
    return render(request, 'login/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión exitosamente.")
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'dashboard/index.html')


        
        

# Crear cliente
def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_create')
    else:
        form = ClienteForm()
    return render(request, 'Clientes/new/cliente_form.html', {'form': form})

# Listar clientes
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_list.html', {'clientes': clientes})

# Detalle del cliente
def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'clientes/cliente_detail.html', {'cliente': cliente})

# Actualizar cliente
def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/cliente_form.html', {'form': form})

# Eliminar cliente
def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'clientes/cliente_confirm_delete.html', {'cliente': cliente})
