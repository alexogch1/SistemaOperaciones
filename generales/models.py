from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True) # Siempre se asigna el valor verdadero
    fc = models.DateTimeField( auto_now_add=True ) # se coloca la fecha del servidor cada vez que se añade un nueve registro
    fm = models.DateTimeField( auto_now=True ) # se modifica la fecha del servidor en cada movimiento del registro
    uc = models.ForeignKey(User, on_delete=models.CASCADE) # toma la llave del usuario en una relacion un usuario a varios productos,
    um = models.IntegerField(blank=True, null=True) #usuario que modifica, lo lee de la clase user

    class Meta:
        abstract= True # Este modelo no es tomado en cuenta  por django cuando se realizan las migraciones


class ClaseModelo2(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    # uc = models.ForeignKey(User, on_delete=models.CASCADE)
    # um = models.IntegerField(blank=True,null=True)
    uc = UserForeignKey(auto_user_add=True,related_name='+')
    um = UserForeignKey(auto_user=True,related_name='+')

    class Meta:
        abstract=True


