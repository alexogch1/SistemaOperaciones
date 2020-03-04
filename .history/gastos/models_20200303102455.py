from django.db import models
from django.conf import settings


from generales.models import ClaseModelo, ClaseModelo2


class UnidNegocio(ClaseModelo):
    id_unidad_negocio=models.CharField(
        max_length=4,
        unique=True
    )
    descripcion_unidad_negocio=models.CharField(
        max_length=20,
        unique=True
    )
    
    def __str__ (self):
        return '{}'.format (self.descripcion_unidad_negocio)

    def save(self):
        self.descripcion_unidad_negocio = self.descripcion_unidad_negocio.upper()
        self.id_unidad_negocio = self.id_unidad_negocio.upper()
        super(UnidNegocio,self).save()

    class Meta():
        verbose_name_plural = 'Unidades de Noegocio'

class AreaGasto(ClaseModelo):
    id_area=models.CharField(
        max_length=4,
        unique=True
    )
    descripcion_area=models.CharField(
        max_length=20,
        unique=True
    )
    
    def __str__ (self):
        return '{}'.format (self.descripcion_area)

    def save(self):
        self.descripcion_area = self.descripcion_area.upper()
        self.id_area = self.id_area.upper()
        super(AreaGasto,self).save()

    class Meta():
        verbose_name_plural = 'Areas Gasto' 

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
    cuenta = models.ForeignKey(GastosCuenta, to_field='descripcion_cuenta_gasto', related_name='detalles', on_delete=models.CASCADE)
    descripcion_subcuenta_gasto  = models.CharField(
        max_length = 100,
        help_text = 'Descripción SubCuenta',
        unique = True,
    )

    id_subcuenta_gasto = models.CharField(
        max_length = 6,
        help_text = 'Clave o ID',
        unique = True,
    )

    def __str__ (self):
        return '{}'.format (self.descripcion_subcuenta_gasto)

    def save(self):
        self.descripcion_subcuenta_gasto = self.descripcion_subcuenta_gasto.upper()
        self.id_subcuenta_gasto = self.id_subcuenta_gasto.upper()
        super(GastosSubCuenta,self).save()
        
    class Meta:
        verbose_name_plural = 'SubCuentas Gastos'
        unique_together = ('cuenta','descripcion_subcuenta_gasto')

class GastoEnc(models.Model):
    fecha_registro= models.DateField()
    unidad_negocio =models.ForeignKey(UnidNegocio, on_delete=models.CASCADE, to_field='descripcion_unidad_negocio')
    area=models.ForeignKey(AreaGasto, on_delete=models.CASCADE, to_field='descripcion_area')


    def __str__(self):
        return' {} {} {}-{}'.format(self.unidad_negocio, self.area, self.fecha_registro.month, self.fecha_registro.year)
    


    class Meta:
        verbose_name_plural ="Encabezados Gastos"
        verbose_name = "Encabezado Gastos"

class GastoDet(models.Model):
    G1 = "PRESUPUESTO"
    G2 = "OBJETIVO"
    G3 ="REAL"

    GRUPO_CHOICES = (
        (G1, 'PRESUPUESTO'),
        (G2, 'OBJETIVO'),
        (G3, 'REAL'),
    )

    gasto = models.ForeignKey(GastoEnc, related_name='detalles' ,on_delete=models.CASCADE)
    grupo=models.CharField(choices=GRUPO_CHOICES, max_length=30, blank=False, null =False)
    subcuenta=models.ForeignKey(GastosSubCuenta, blank=False, null =False, on_delete=models.CASCADE)
    cantidad =models.FloatField(default=0.0)
    
    def __str__(self):
        return "{} {}".format(self.gasto, self.grupo)
    
    class Meta:
        verbose_name_plural ="Detalles Gastos"
        verbose_name = "Detalle Gastos"

