from django.shortcuts import render, redirect 
from django.views.generic.edit import CreateView
from .models import FormularioIngreso, Mes ,FormularioEgreso
from django.http import JsonResponse
from .models import TipoIngreso , TipoGasto
from django.views import generic
from django.urls import reverse_lazy

def inicio(request):
    return render(request, 'inicio.html',{})

def ingreso(request):
    return render(request, 'nuevo-ingreso.html',{})

class FormularioIngresoCreateView(CreateView):
    model = FormularioIngreso
    template_name = 'formularioingreso_form.html'
    fields = ['mes', 'ingreso', 'tipo_ingreso', 'monto']
    success_url = reverse_lazy('formulario_ingreso_creado')

def load_tipos(request):
    ingreso_id = request.GET.get('ingreso')
    tipos = TipoIngreso.objects.filter(ingreso_id=ingreso_id).order_by('nombre')
    return JsonResponse(list(tipos.values('id', 'nombre')), safe=False)

def listaIngresos(request):
    # Solo obtén los meses que tienen al menos un ingreso.
    meses = Mes.objects.filter(formularioingreso__isnull=False).distinct()
    return render(request, 'listaIngreso.html', {'meses': meses})


def detallesIngresos(request, mes_id):
    formulario_ingresos = FormularioIngreso.objects.filter(mes_id=mes_id)
    total_ingresos = sum([ingreso.monto for ingreso in formulario_ingresos])
    return render(request, 'detallesIngresos.html', {'formulario_ingresos': formulario_ingresos, 'total_ingresos': total_ingresos})

class editarIngreso(generic.UpdateView):
    model = FormularioIngreso
    template_name = 'editarIngreso.html'
    fields = ['mes', 'ingreso', 'tipo_ingreso', 'monto']
    success_url = reverse_lazy('listaIngreso')

class borrarIngreso(generic.DeleteView):
    model = FormularioIngreso
    template_name = 'ingreso_confirm_delete.html'
    success_url = reverse_lazy('listaIngreso')

def egreso(request):
    return render(request, 'nuevo-egreso.html',{})
class FormularioEgresoCreateView(CreateView):
    model = FormularioEgreso
    template_name = 'formularioegreso_form.html'
    fields = ['mes', 'gasto', 'tipo_gasto', 'monto']
    success_url = reverse_lazy('formulario_egreso_creado')

def load_tipos_egreso(request):
    gasto_id = request.GET.get('gasto')
    tipos = TipoGasto.objects.filter(gasto_id=gasto_id).order_by('nombre')
    return JsonResponse(list(tipos.values('id', 'nombre')), safe=False)

def listaEgresos(request):
    # Solo obtén los meses que tienen al menos un egreso.
    meses = Mes.objects.filter(formularioegreso__isnull=False).distinct()
    return render(request, 'listaEgreso.html', {'meses': meses})


def detallesEgresos(request, mes_id):
    formulario_egresos = FormularioEgreso.objects.filter(mes_id=mes_id)
    total_egresos = sum([egreso.monto for egreso in formulario_egresos])
    return render(request, 'detallesEgresos.html', {'formulario_egresos': formulario_egresos, 'total_egresos': total_egresos})

class editarEgreso(generic.UpdateView):
    model = FormularioEgreso
    template_name = 'editarEgreso.html'
    fields = ['mes', 'gasto', 'tipo_gasto', 'monto']
    success_url = reverse_lazy('listaEgreso')

class borrarEgreso(generic.DeleteView):
    model = FormularioEgreso
    template_name = 'egreso_confirm_delete.html'
    success_url = reverse_lazy('listaEgreso')
