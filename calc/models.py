# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Funciones(models.Model):
    LIMITES = 'l'
    DERIVADAS = 'd'
    INTEGRALES = 'i'
    ECUACIONESDIFERENCIALES = 'ed'

    TIPOS_CHOICES = (
        (LIMITES, 'Limites'),
        (DERIVADAS, 'Derivadas'),
        (INTEGRALES, 'Integrales'),
        (ECUACIONESDIFERENCIALES, 'Ecuaciones Diferenciales'),
    )
    tipo = models.CharField(max_length=2, choices=TIPOS_CHOICES)
    problema = models.CharField(max_length=1000)
    solucion = models.CharField(max_length=1000)