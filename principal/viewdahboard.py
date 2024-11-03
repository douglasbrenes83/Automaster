from django.shortcuts import render
from .models import Cita

def dashboard(request):
    ultimas_citas = Cita.objects.all().order_by('-fecha')[:10]  # Obtiene las últimas 10 citas
    context = {
        'ultimas_citas': ultimas_citas,
    }
    return render(request, 'tu_template.html', context)
