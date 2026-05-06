from django.urls import path
from . import views

urlpatterns = [
    path("", views.valorant, name="valorant"),
    path("habilidades/", views.habilidades, name="habilidades"),
    path("habilidades/nueva/", views.crear_habilidad, name="crear_habilidad"),
    path("habilidades/<int:id>/editar/", views.editar_habilidad, name="editar_habilidad"),
    path("habilidades/<int:id>/eliminar/", views.eliminar_habilidad, name="eliminar_habilidad"),
]