from django.contrib import admin

from .models import Planta, Linea, Bascula, Formadora, Supervisor, Operador
# Register your models here.


admin.site.register(Planta)
admin.site.register(Linea)
admin.site.register(Bascula)
admin.site.register(Formadora)
admin.site.register(Supervisor)
admin.site.register(Operador)

