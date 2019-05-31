from djongo import models
from django import forms
# Create your models here.

class Post(models.Model):
    dominio = models.CharField(max_length=255)
    porcentaje_movil = models.CharField(max_length=255)
    orportunidades_movil = models.ListField()
    diagnosticos_movil = models.ListField()
    porcentaje_ordenador = models.CharField(max_length=255)
    oportunidades_ordenador = models.ListField()
    diagnosticos_ordenador = models.ListField()


class Meta:
    abstract = True