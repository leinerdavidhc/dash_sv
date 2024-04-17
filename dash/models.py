from django.db import models
from django.utils import timezone

class Vehiculo(models.Model):
    TIPOS_VEHICULO = [
        ('automovil', 'Automóvil'),
        ('camion', 'Camión'),
        ('camioneta', 'Camioneta'),
        ('moto', 'Moto'),
        ('otros', 'Otros'),
    ]

    DIRECCIONES=[
        ('arriba', 'Arriba'),
        ('arriba-izquierda', 'Arriba-Izquierda'),
        ('arriba-derecha', 'Arriba-Derecha'),
        ('izquierda', 'Izquierda'),
        ('izquierda-arriba', 'Izquierda-Arriba'),
        ('derecha', 'Derecha'),
        ('derecha-arriba', 'Derecha-Arriba'),
        ('abajo', 'Abajo'),
    ]
    
    tipo = models.CharField(max_length=20, choices=TIPOS_VEHICULO)
    direccion = models.CharField(max_length=20, choices=DIRECCIONES)
    cantidad = models.IntegerField()
    tiempo_inicio = models.DateTimeField(default=timezone.now, blank=False, null=False)
    tiempo_fin = models.DateTimeField(default=timezone.now, blank=False, null=False)

    def __str__(self):
        return f"{self.tipo} x {self.cantidad} - {self.direccion}"


class Anotacion(models.Model):
    TIPOS_VEHICULO = [
        ('automovil', 'Automóvil'),
        ('camion', 'Camión'),
        ('camioneta', 'Camioneta'),
        ('moto', 'Moto'),
        ('otros', 'Otros'),
    ]
    tiempo_inicio = models.DateTimeField(default=timezone.now, blank=False, null=False)
    tiempo_fin = models.DateTimeField(default=timezone.now, blank=False, null=False)
    observacion = models.TextField(blank=True, null=True)
    grupo_tipo = models.CharField(max_length=20, choices=TIPOS_VEHICULO)
    grupo_cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.grupo_tipo} x {self.grupo_cantidad} - {self.tiempo_paso}"


class Incidentes(models.Model):
    titulo = models.CharField(max_length=20)
    tiempo_inicio = models.DateTimeField(default=timezone.now, blank=False, null=False)
    tiempo_fin = models.DateTimeField(default=timezone.now, blank=False, null=False)
    cantidad_vehiculos = models.IntegerField()
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo}"