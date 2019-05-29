from djongo import models
from django.db import models
# Create your models here.
class Tutorial(models.Model):
    _id = models.CharField(max_length=200, default="")
    dominio = models.CharField(max_length=200, default="")
    porcentaje_movil = models.CharField(max_length=200, default="")
    orportunidades_movil = models.CharField(max_length=900, default="")
    diagnosticos_movil = models.CharField(max_length=900, default="")
    porcentaje_ordenador = models.CharField(max_length=200, default="")
    oportunidades_ordenador = models.CharField(max_length=900, default="")
    diagnosticos_ordenador = models.CharField(max_length=900, default="")


    #def __str__(self):
#        return self._id