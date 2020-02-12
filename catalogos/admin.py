from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Cliente, Marca, Ingred, Corte, Presentacion, CasoEsp, Producto

admin.site.register(Cliente)
admin.site.register(Marca)
admin.site.register(Ingred)
admin.site.register(Corte)
admin.site.register(Presentacion)
admin.site.register(CasoEsp)
admin.site.register(Producto)   
