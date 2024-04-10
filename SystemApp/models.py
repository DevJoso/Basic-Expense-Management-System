from django.db import models
from django.urls import reverse


# Create your models here.




class Ingreso(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class TipoIngreso(models.Model):
    nombre = models.CharField(max_length=200)
    ingreso = models.ForeignKey(Ingreso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Mes(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class FormularioIngreso(models.Model):
    
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    ingreso = models.ForeignKey(Ingreso, on_delete=models.CASCADE)
    tipo_ingreso = models.ForeignKey(TipoIngreso, on_delete=models.CASCADE)

    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.mes} - {self.ingreso} - {self.tipo_ingreso} - {self.monto}"


#modelos de egresos
    
class Gasto(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class TipoGasto(models.Model):
    nombre = models.CharField(max_length=200)
    gasto = models.ForeignKey(Gasto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class FormularioEgreso(models.Model):
    
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    gasto = models.ForeignKey(Gasto, on_delete=models.CASCADE)
    tipo_gasto = models.ForeignKey(TipoGasto, on_delete=models.CASCADE)

    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.mes} - {self.gasto} - {self.tipo_gasto} - {self.monto}"
