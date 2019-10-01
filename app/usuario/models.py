from django.db import models
from django.utils import timezone
from formulario.models import Formulario

class Usuario(models.Model):
    nombre = models.CharField(max_length=250, null=False)
    apellido = models.CharField(max_length=250, null=False)
    email = models.EmailField(max_length=250, null=False)
    fecha_nacimiento = models.DateTimeField(null=False)
    formulario = models.ForeignKey(Formulario, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
