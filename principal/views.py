from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def IndexPage(request):
    return render(request, 'index.html')

def Reslogin(request):
    return render(request,'login/login.html')
        