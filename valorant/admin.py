from django.contrib import admin
from .models import Agente, Habilidad

# Register your models here.

admin.site.register(Agente)

@admin.register(Habilidad)
class HabilidadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "agente", "tipo")
    search_fields = ("nombre", "agente__nombre")
    list_filter = ("tipo", "agente")