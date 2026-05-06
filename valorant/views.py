from django.shortcuts import get_object_or_404, redirect, render
from .models import Agente, Habilidad
from .forms import HabilidadForm

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

def habilidades(request):
    habilidades = Habilidad.objects.all()
    return render(request, 'valorant/habilidades.html', {'habilidades': habilidades})

def crear_habilidad(request):
    if request.method == "POST":
        form = HabilidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("habilidades")
    else:
        form = HabilidadForm()
    return render(request, "valorant/crear_habilidad.html", {"form": form})

def editar_habilidad(request, id):
    habilidad = get_object_or_404(Habilidad, id=id)
    if request.method == "POST":
        form = HabilidadForm(request.POST, instance=habilidad)
        if form.is_valid():
            form.save()
            return redirect("habilidades")
    else:
        form = HabilidadForm(instance=habilidad)
    return render(request, "valorant/editar_habilidad.html", {"form": form})

def eliminar_habilidad(request, id):
    habilidad = get_object_or_404(Habilidad, id=id)
    if request.method == "POST":
        habilidad.delete()
        return redirect("habilidades")
    return render(request, "valorant/eliminar_habilidad.html", {"habilidad": habilidad})