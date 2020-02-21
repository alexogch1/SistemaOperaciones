from django.db import models
from generales.models import ClaseModelo
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def rango(value):
        if value <1 or value >52:
            raise ValidationError(_('%(value) no está dentro del rango de semanas de 1 a 52'),
        params={'value':value},
        )

class PlantaNomina(ClaseModelo):
    id_planta =models.CharField(
        max_length=2,
        unique=True
    )
    descripcion_planta = models.CharField(
        max_length=20,
        unique=True
    )
    
    def __str__ (self):
        return '{}'.format (self.descripcion_planta)

    def save(self):
        self.descripcion_planta = self.descripcion_planta.upper()
        self.id_planta = self.id_planta.upper()
        super(PlantaNomina,self).save()

    class Meta():
        verbose_name_plural = 'Plantas Nomina' 


class AreaNomina(ClaseModelo):
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
        super(AreaNomina,self).save()

    class Meta():
        verbose_name_plural = 'Areas Nomina' 

class lineaNomina(ClaseModelo):
    id_linea =models.CharField(
        max_length=4,
        unique=True
    )
    descripcion_linea = models.CharField(
        max_length=20,
        unique=True
    )
    
    def __str__ (self):
        return '{}'.format (self.descripcion_linea)

    def save(self):
        self.descripcion_linea = self.descripcion_linea.upper()
        self.id_linea = self.id_linea.upper()
        super(lineaNomina,self).save()
        
    class Meta():
        verbose_name_plural = 'Lineas Nomina' 

class SupervisorNomina(ClaseModelo):
    id_supervisor =models.CharField(
        max_length=4,
        unique=True
    )
    nombre_supervisor = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__ (self):
        return '{}'.format (self.nombre_supervisor)

    def save(self):
        self.nombre_supervisor = self.nombre_supervisor.upper()
        self.id_supervisor = self.id_supervisor.upper()
        super(SupervisorNomina,self).save()
        
    class Meta():
        verbose_name_plural = 'Supervisores Nomina' 

class ConceptoNomina(ClaseModelo):
    PER = "PERCEPCION"
    DED = "DEDUCCION"

    TIPO_CHOICES = (
        (PER, 'PERCEPCION'),
        (DED, 'DEDUCCION')
    )

    id_concepto=models.CharField(max_length=100)
    concepto=models.CharField(max_length=100, unique=True)
    tipo_concepto=models.CharField(choices=TIPO_CHOICES, max_length=30, blank=True, null =True)

    def __str__ (self):
        return '{}'.format (self.concepto)


class NominaEnc(ClaseModelo):
    G1 = "PERSONAL"
    G2 = "SUPERVISOR"
    G3 ="AUXILIAR"

    GRUPO_CHOICES = (
        (G1, 'PERSONAL'),
        (G2, 'SUPERVISOR'),
        (G3, 'AUXILIAR'),
    )

    fecha_nomina= models.DateField()
    planta =models.ForeignKey(PlantaNomina,to_field='descripcion_planta',on_delete=models.CASCADE)
    area=models.ForeignKey(AreaNomina, on_delete=models.CASCADE, to_field='descripcion_area')
    linea =models.ForeignKey(lineaNomina, on_delete=models.CASCADE, to_field='descripcion_linea')
    grupo=models.CharField(choices=GRUPO_CHOICES, max_length=30, blank=True, null =True)
    supervisor=models.ForeignKey(SupervisorNomina, on_delete=models.CASCADE, to_field='nombre_supervisor')
    semana = models.IntegerField(default=1 )
    plantilla = models.IntegerField(default=0)
    total_percepciones = models.DecimalField(default=0.0,max_digits=6, decimal_places=2)
    total_deducciones = models.DecimalField(default=0.0,max_digits=6, decimal_places=2)
    

    def __str__(self):
        return'{} {} {} {} {}'.format(self.semana, self.area, self.linea, self.grupo, self.supervisor)
    
    class Meta:
        verbose_name_plural ="Encabezados Nomina"
        verbose_name = "Encabezado Nomina"

class NominaDet(models.Model):

    nomina = models.ForeignKey(NominaEnc, on_delete=models.CASCADE)
    concepto=models.ForeignKey(ConceptoNomina, on_delete=models.CASCADE, to_field='concepto')
    cantidad =models.FloatField(default=0.0)
    

    def __str__(self):
        return "{} {}".format(self.nomina,self.concepto)
    

    class Meta:
        verbose_name_plural ="Detalles Nomina"
        verbose_name = "Detalle Nomina"

