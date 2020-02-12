from django.contrib import admin

from .models import ProduccionEnc, ProduccionDet, TiempoMuertoEnc, TiempoMuertonDet, \
    ProduccionCongDet, ProduccionCongEnc, TiempoMuertoCongEnc, TiempoMuertoCongDet

admin.site.register(ProduccionEnc)
admin.site.register(ProduccionDet)
admin.site.register(TiempoMuertoEnc)
admin.site.register(TiempoMuertonDet)
admin.site.register(ProduccionCongDet)
admin.site.register(ProduccionCongEnc)
admin.site.register(TiempoMuertoCongEnc)
admin.site.register(TiempoMuertoCongDet)
