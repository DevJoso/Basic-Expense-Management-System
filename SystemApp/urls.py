from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio-screen'),
    path('ingreso/', views.ingreso, name='ingreso-screen'),
    path('crear_formulario_ingreso/', views.FormularioIngresoCreateView.as_view(), name='formulario_ingreso_creado'),
    path('ajax/load-tipos/', views.load_tipos, name='load-tipos'),
    path('listaIngreso/', views.listaIngresos, name='listaIngreso'),
    path('detallesIngresos/<int:mes_id>/', views.detallesIngresos, name='detallesIngresos'),
    path('editarIngreso/<int:pk>', views.editarIngreso.as_view(), name='editarIngreso'),
    path('borrarIngreso/<int:pk>', views.borrarIngreso.as_view(), name='borrarIngreso'),
    
    path('egreso/', views.egreso, name='egreso-screen'),
    path('crear_formulario_egreso/', views.FormularioEgresoCreateView.as_view(), name='formulario_egreso_creado'),
    path('ajax/load-tipos-egreso/', views.load_tipos_egreso, name='ajax_load_tipos_egreso'),
    path('listaEgreso/', views.listaEgresos, name='listaEgreso'),
    path('detallesEgresos/<int:mes_id>/', views.detallesEgresos, name='detallesEgresos'),
    path('editarEgreso/<int:pk>', views.editarEgreso.as_view(), name='editarEgreso'),
    path('borrarEgreso/<int:pk>', views.borrarEgreso.as_view(), name='borrarEgreso'),
]
