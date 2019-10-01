from django.db import models
from datetime import datetime


class Formulario(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False)
    dato1 = models.IntegerField(null=False, blank=False)
    dato2 = models.IntegerField(null=False, blank=False)
    dato3 = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.id

class Formulario_id(models.Model):
    id_inicio = models.IntegerField(null=False, blank=False)
    id_fin = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.id_inicio
