from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    dirección = models.CharField(max_length=100)
    Ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
