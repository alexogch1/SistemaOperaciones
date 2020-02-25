from django.db import models
from django.conf import settings

from generales.models import ClaseModelo, ClaseModelo2

class OwnerModel (ClaseModelo2):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Planta(ClaseModelo):
    descripcion  = models.CharField(
        max_length = 100,
        help_text = 'Descripcion de Planta',
        unique = True
    )
    
    id_planta = models.CharField(
        max_length = 2,
        help_text = 'Clave o ID de la Planta',
        unique = True,
    )

    def __str__ (self):
        return '{}'.format (self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        self.id_planta = self.id_planta.upper()
        super(Planta,self).save()
        
    class Meta():
        verbose_name_plural = 'Plantas' 

class Linea(ClaseModelo):
    planta = models.ForeignKey(Planta, on_delete = models.CASCADE)
    descripcion = models.CharField(
        max_length = 100,
        help_text= 'Descripción de la Línea',
        unique = False
    )

    id_linea = models.CharField(
        max_length = 4,
        help_text= 'Id Linea',
        unique = True
    )

    def __str__(self):
        return '{}:{}'.format(self.planta.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        self.id_linea = self.id_linea.upper()
        super(Linea, self).save()

    class Meta:
        verbose_name_plural = 'Lineas'
        unique_together = ('planta','descripcion')


class Supervisor(ClaseModelo):
    planta = models.ForeignKey(Planta, on_delete = models.CASCADE)
    descripcion = models.CharField(
        max_length = 100,
        help_text= 'Descripción del Supervisor',
        unique = True
    )

    id_supervisor = models.CharField(
        max_length = 4,
        help_text= 'Id Supervisor',
        unique = True
    )

    def __str__(self):
        return '{}:{}'.format(self.planta.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        self.id_supervisor = self.id_supervisor.upper()
        super(Supervisor, self).save()

    class Meta:
        verbose_name_plural = 'Supervisores'
        unique_together = ('planta','descripcion')


class Operador(ClaseModelo):
    planta = models.ForeignKey(Planta, on_delete = models.CASCADE)
    descripcion = models.CharField(
        max_length = 100,
        help_text= 'Descripción del Operador',
        unique = True
    )

    id_operador = models.CharField(
        max_length = 4,
        help_text= 'Id operador',
        unique = True
    )

    def __str__(self):
        return '{}:{}'.format(self.planta.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        self.id_operador = self.id_operador.upper()
        super(Operador, self).save()

    class Meta:
        verbose_name_plural = 'Operadores'
        unique_together = ('planta','descripcion')

class Bascula(ClaseModelo):
    linea = models.ForeignKey(Linea, on_delete = models.CASCADE)
    descripcion = models.CharField(
        max_length = 100,
        help_text= 'Descripción de la Báscula',
        unique = False
    )

    id_bascula = models.CharField(
        max_length = 6,
        help_text= 'Id Bascula',
        unique = True
    )

    celdas = models.IntegerField(default=0)
        
    modelo = models.CharField(
        max_length = 20,
        help_text= 'Modelo Báscula',
    )

    def __str__(self):
        return '{}:{}'.format(self.linea.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        self.id_bascula = self.id_bascula.upper()
        self.modelo = self.modelo.upper()
        super(Bascula, self).save()

    class Meta:
        verbose_name_plural = 'Basculas'
        unique_together = ('linea','descripcion')

class Formadora(ClaseModelo):
    linea = models.ForeignKey(Linea, on_delete = models.CASCADE)
    descripcion = models.CharField(
        max_length = 100,
        help_text= 'Descripción de la Formadora',
        unique = False
    )

    id_formadora = models.CharField(
        max_length = 6,
        help_text= 'Id Formadora',
        unique = True
    )

    modelo = models.CharField(
        max_length = 20,
        help_text= 'Modelo Formadora',
    )

    def __str__(self):
        return '{}:{}'.format(self.linea.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        self.id_formadora = self.id_formadora.upper()
        self.modelo = self.modelo.upper()
        super(Formadora, self).save()

    class Meta:
        verbose_name_plural = 'Formadoras'
        unique_together = ('linea','descripcion')

