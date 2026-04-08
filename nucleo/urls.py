from django.urls import path

from . import views

urlpatterns = [
    path("", views.nucleo, name="nucleo"),
]