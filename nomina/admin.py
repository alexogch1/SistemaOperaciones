from django.contrib import admin
from .models import PlantaNomina, AreaNomina,  lineaNomina, SupervisorNomina, \
    ConceptoNomina,NominaEnc, NominaDet

admin.site.register(PlantaNomina)
admin.site.register(AreaNomina)
admin.site.register(lineaNomina)
admin.site.register(SupervisorNomina)
admin.site.register(ConceptoNomina)

admin.site.register(NominaEnc)
admin.site.register(NominaDet)

