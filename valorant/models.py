from django.db import models

# Create your models here.

class Agente(models.Model):
    ROLES = [
        ('duelist', 'Duelista'),
        ('controller', 'Controlador'),
        ('initiator', 'Iniciador'),
        ('sentinel', 'Centinela'),
    ]

    nombre = models.CharField(max_length=50)
    rol = models.CharField(max_length=20, choices=ROLES)
    imagen = models.URLField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre