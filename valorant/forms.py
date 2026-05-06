from django import forms
from .models import Habilidad

class HabilidadForm(forms.ModelForm):
    class Meta:
        model = Habilidad
        fields = ['agente', 'nombre', 'descripcion', 'tipo', 'icono']
        