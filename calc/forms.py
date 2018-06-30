# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django import forms
from calc.models import Funciones

class FormularioFunciones(forms.ModelForm):
    class Meta:
        model = Funciones
        fields = '__all__'
        exclude = ('solucion',)
        labels = {
            'tipo': 'Tipo',
            'problema': 'Problema',
        }
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control col-md-6 col-xs-12'}),
            'ploblema': forms.TextInput(attrs={'class': 'form-control col-md-6 col-xs-12'}),
        }

