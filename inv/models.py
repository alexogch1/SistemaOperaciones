from django.db import models

from generales.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length = 100,
        help_text= 'Descripción de la Categoría',
        unique = True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = 'Categorias'

class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    descripcion = models.CharField(
        max_length = 100,
        help_text= 'Descripción de la Categoría',
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural = 'Categorias'
        unique_together = ('categoria','descripcion')

class Origen(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    descripcion = models.CharField(
        max_length = 100,
        help_text= 'Descripción de la Categoría',
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Origen, self).save()

    class Meta:
        verbose_name_plural = 'Origenes'
        unique_together = ('categoria','descripcion')

 