# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from calc.forms import FormularioFunciones


def resolver(request):
    template = 'index.html'
    form = FormularioFunciones(request.POST or None)
    solucion = None
    problema = None
    if request.method == 'POST':
        formulario = form.save(commit=False)
        formulario.solucion = "x**2"
        solucion = formulario.solucion
        problema = formulario.problema
        formulario.save()
    datos = {
        'formulario' : form,
        'solucion' : solucion,
        'problema' : problema
    }
    return render(request, template,datos)