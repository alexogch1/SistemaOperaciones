from django.db import models
from django.conf import settings

from generales.models import ClaseModelo, ClaseModelo2


class GastosCuenta(ClaseModelo):
    descripcion_cuenta_gasto  = models.CharField(
        max_length = 100,
        help_text = 'Descripción Categoria',
        unique = True
    )
    
    id_cuenta_gasto = models.CharField(
        max_length = 6,
        help_text = 'Clave o ID  ',
        unique = True,
    )
    def __str__ (self):
        return '{}'.format (self.descripcion_cuenta_gasto)

    def save(self):
        self.descripcion_cuenta_gasto = self.descripcion_cuenta_gasto.upper()
        self.id_cuenta_gasto = self.id_cuenta_gasto.upper()
        super(GastosCuenta,self).save()
        
    class Meta():
        verbose_name_plural = 'Cuentas Gastos' 


class GastosSubCuenta(ClaseModelo):
    cuenta_gasto = models.ForeignKey(GastosCuenta,to_field='descripcion_cuenta_gasto',on_delete=models.CASCADE)
    descripcion_subcuenta_gasto  = models.CharField(
        max_length = 100,
        help_text = 'Descripción SubCuenta',
    )

    id_subcuenta_gasto = models.CharField(
        max_length = 6,
        help_text = 'Clave o ID'
    )

    def __str__ (self):
        return '{}'.format (self.descripcion_subcuenta_gasto)

    def save(self):
        self.descripcion_subcuenta_gasto = self.descripcion_subcuenta_gasto.upper()
        self.id_subcuenta_gasto = self.id_subcuenta_gasto.upper()
        super(GastosSubCuenta,self).save()
        
    class Meta:
        verbose_name_plural = 'SubCuentas Gastos'
        unique_together = ('cuenta_gasto','descripcion_subcuenta_gasto')