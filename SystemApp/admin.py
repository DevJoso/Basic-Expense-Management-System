from django.contrib import admin
from .models import Ingreso, TipoIngreso, Mes, FormularioIngreso ,Gasto, TipoGasto, FormularioEgreso

# Register your models here.
admin.site.register(Ingreso)
admin.site.register(TipoIngreso)
admin.site.register(Mes)
admin.site.register(FormularioIngreso)


admin.site.register(Gasto)
admin.site.register(TipoGasto)
admin.site.register(FormularioEgreso)


