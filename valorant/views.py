from django.shortcuts import render
from .models import Agente

# Create your views here.

def valorant(request):
    agentes = Agente.objects.all()

    data = [
        {
            "nombre": a.nombre,
            "imagen": a.imagen,
            "rol_display": a.get_rol_display()
        }
        for a in agentes
    ]

    return render(request, 'valorant/index.html', {'agentes': data})