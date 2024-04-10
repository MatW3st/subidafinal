# models.py
from django.db import models
from datetime import datetime


class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    tipo_usuario = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_usuario

class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    sinopsis = models.TextField()
    duracion = models.IntegerField()
    genero = models.CharField(max_length=255)
    estado = models.CharField(max_length=20, choices=[('estreno', 'Estreno'), ('no_disponible', 'No disponible')])
    imagen = models.ImageField(upload_to='media/')
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.titulo
    


class Horario(models.Model):
    sala = models.CharField(max_length=100)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.now)
    hora = models.TimeField()
    cantidad_boletos = models.PositiveIntegerField(default=0)  # Nuevo campo

    def __str__(self):
        return f"{self.pelicula} - Sala {self.sala} - {self.fecha} {self.hora} - Boletos: {self.cantidad_boletos}"
