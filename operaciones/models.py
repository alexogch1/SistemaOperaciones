from django.db import models
from generales.models import ClaseModelo

class TipoCambio(ClaseModelo):
    tipo_cambio=models.FloatField()
    fecha=models.DateField()

    def __str__(self):
        return '{}'.format(self.fecha)

    class Meta:
        verbose_name_plural = 'Tipos_Cambio'