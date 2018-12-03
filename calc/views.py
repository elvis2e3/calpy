# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from calc.Calc import calc
from calc.forms import FormularioFunciones


def resolver(request):
    template = 'index.html'
    form = FormularioFunciones(request.POST or None)
    solucion = None
    problema = None
    if request.method == 'POST':
        formulario = form.save(commit=False)
        calculo = calc()
        formulario.solucion = calculo.control(formulario.problema,formulario.tipo)
        formulario.problema = calculo.parse_latex(formulario.problema)
        solucion = formulario.solucion
        problema = formulario.problema
        formulario.save()
    datos = {
        'formulario' : form,
        'solucion' : solucion,
        'problema' : problema
    }
    return render(request, template,datos)