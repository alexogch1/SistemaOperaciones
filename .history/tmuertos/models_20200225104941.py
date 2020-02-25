from django.db import models


from generales.models import ClaseModelo

class CategoriaTM(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        unique=True
    )

    id_categoriaTM = models.CharField(
        max_length=4,
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        self.id_cateogoriaTM = self.id_categoriaTM.upper()
        super(CategoriaTM, self).save()

    class Meta:
        verbose_name_plural = "CategoriasTM"

class CausaTM(ClaseModelo):
    PRG='Programado'
    NPR='No Programado'
    IMP='Imprevisto'
    TIPO_TM = [
        (PRG,'Programado'),
        (NPR,'No Programado'),
        (IMP,'Imprevisto')
    ]

    categoriaTM = models.ForeignKey(CategoriaTM, on_delete = models.CASCADE)
    descripcion = models.CharField(
        max_length = 100,
        unique=True,
        help_text= 'Descripción de la Categoría',
    )

    id_causaTM = models.CharField(
        max_length = 4,
        help_text= 'Id Causa TM',
        unique=True
    )

    tipo=models.CharField(
        max_length=15,
        choices=TIPO_TM,
        default=PRG
    )

    tolerancia=models.IntegerField(
        default=0
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        self.id_causaTM = self.id_causaTM.upper()
        self.tipo = self.tipo.upper()
        super(CausaTM, self).save()

    class Meta:
        verbose_name_plural = 'CausasTM'
        unique_together = ('categoriaTM','descripcion')