from django.contrib import admin
from .models import UnidNegocio, AreaGasto, GastosCuenta, GastosSubCuenta,GastoEnc, GastoDet

admin.site.register(UnidNegocio)
admin.site.register(AreaGasto)
admin.site.register(GastosCuenta)
admin.site.register(GastosSubCuenta)

admin.site.register(GastoEnc)
admin.site.register(GastoDet)