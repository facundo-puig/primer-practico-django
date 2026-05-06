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
    

class Habilidad(models.Model):
    TECLA = [
        ('C', 'C'),
        ('Q', 'Q'),
        ('E', 'E'),
        ('X', 'Ultimate'),
    ]

    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, related_name='habilidades')
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=1, choices=TECLA)
    icono = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.agente.nombre} - {self.nombre}"