from django.contrib import admin
from .models import GastosCuenta, GastosSubCuenta,GastoEnc, GastoDet

admin.site.register(GastosCuenta)
admin.site.register(GastosSubCuenta)
admin.site.register(GastosSubCuenta)
admin.site.register(GastoEnc)
admin.site.register(GastoDet)