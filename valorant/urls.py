from django.urls import path

from . import views

urlpatterns = [
    path("", views.valorant, name="valorant"),
]