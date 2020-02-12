from django.db import models
from django.conf import settings

from generales.models import ClaseModelo, ClaseModelo2

class OwnerModel (ClaseModelo2):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Cliente(ClaseModelo):
    descripcion_cliente  = models.CharField(
        max_length = 100,
        help_text = 'Descripción',
        unique = True
    )
    
    id_cliente = models.CharField(
        max_length = 4,
        help_text = 'Clave o ID  ',
        unique = True,
    )

    def __str__ (self):
        return '{}'.format (self.descripcion_cliente)

    def save(self):
        self.descripcion_cliente = self.descripcion_cliente.upper()
        self.id_cliente = self.id_cliente.upper()
        super(Cliente,self).save()
        
    class Meta():
        verbose_name_plural = 'Clientes' 

class Marca(ClaseModelo):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    descripcion_marca = models.CharField(
        max_length = 100,
        help_text= 'Descripción',
        unique = True,
    )

    id_marca = models.CharField(
        max_length = 4,
        help_text = 'Clave o ID   ',
        unique = True,
    )

    def __str__(self):
        return '{}:{}'.format(self.cliente.descripcion, self.descripcion_marca)

    def save(self):
        self.descripcion_marca = self.descripcion_marca.upper()
        self.id_marca = self.id_marca.upper()
        super(Marca, self).save()

    class Meta:
        verbose_name_plural = 'Marcas'
        unique_together = ('cliente','descripcion_marca')

class Ingred(ClaseModelo):
    descripcion_ing  = models.CharField(
        max_length = 100,
        help_text = 'Descripción',
        unique = True
    )
    
    id_ingred = models.CharField(
        max_length = 2,
        help_text = 'Clave o ID   ',
        unique = True,    
    )

    def __str__ (self):
        return '{}'.format (self.descripcion_ing)

    def save(self):
        self.descripcion_ing = self.descripcion_ing.upper()
        self.id_ingred = self.id_ingred.upper()
        super(Ingred,self).save()
        
    class Meta():
        verbose_name_plural = 'Ingreds'

class Corte(ClaseModelo):
    descripcion_corte  = models.CharField(
        max_length = 100,
        help_text = 'Descripción',
        unique = True
    )
    
    id_corte = models.CharField(
        max_length = 2,
        help_text = 'Clave o ID  ',
        unique = True,    
    )

    def __str__ (self):
        return '{}'.format (self.descripcion_corte)

    def save(self):
        self.descripcion_corte = self.descripcion_corte.upper()
        self.id_corte = self.id_corte.upper()
        super(Corte,self).save()
        
    class Meta():
        verbose_name_plural = 'Cortes'


class CasoEsp(ClaseModelo):
    descripcion_ce  = models.CharField(
        max_length = 100,
        help_text = 'Descripción',
        unique = True
    )
    
    id_ce = models.CharField(
        max_length = 2,
        help_text = 'Clave o ID  ',
        unique = True,
    )

    def __str__ (self):
        return '{}'.format (self.descripcion_ce)

    def save(self):
        self.descripcion_ce = self.descripcion_ce.upper()
        self.id_ce = self.id_ce.upper()
        super(CasoEsp,self).save()
        
    class Meta():
        verbose_name_plural = 'Casos Espeiales' 

class Presentacion(ClaseModelo):
    LBS='LBS'
    KG='KG'
    GR='GR'
    OZ='OZ'
    unidad = [
        (LBS,'LBS'),
        (KG,'KG'),
        (GR,'GR'),
        (OZ,'OZ')
    ]
    descripcion_presenta  = models.CharField(
        max_length = 20,
        help_text = 'Descripción',
        unique = True
    )
    
    id_presentacion = models.CharField(
        max_length = 5,
        help_text = 'Clave o ID',
        unique = True,
    )

    paqs = models.IntegerField(
        default=0,
    )

    peso = models.FloatField(
        default=0,
    )

    unidad = models.CharField(
        max_length = 3,
        choices=unidad,
        default=OZ,
        help_text = 'Unidad de Medida  ',
        unique = False,
    )

    peso_caja = models.FloatField(
        default=0.0000
    )

    def __str__ (self):
        return '{}'.format (self.descripcion_presenta)

    def save(self):
        self.descripcion_presenta = self.descripcion_presenta.upper()
        self.id_presentacion = self.id_presentacion.upper()
        self.unidad = self.unidad.upper()
        super(Presentacion,self).save()
        
    class Meta():
        verbose_name_plural = 'Presentaciones'

class Producto(ClaseModelo):
    
    descripcion_prod  = models.CharField(
        max_length = 100,
        help_text = 'Descripción',
        unique = True
    )    
    id_producto = models.CharField(
        max_length = 15,
        help_text = 'Clave o ID   ',
        unique = True,
    )
    
    peso_caja = models.FloatField(
        default=0.0
    )

    def __str__ (self):
        return '{}'.format (self.descripcion_prod)

    def save(self):
        
        self.descripcion_prod = self.descripcion_prod.upper()
        self.id_producto = self.id_producto.upper()
        super(Producto,self).save()
        
    class Meta():
        verbose_name_plural = 'Productos'
        verbose_name = "Producto"
