
from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls
urlpatterns = [
    path ('', include(('generales.urls', 'generales'), namespace = 'generales')),
    path ('inv/', include(('inv.urls', 'inv'), namespace = 'inv')),
    path ('catalogos/', include(('catalogos.urls', 'catalogos'), namespace = 'catalogos')),
    path ('textos/', include(('textos.urls', 'textos'), namespace = 'textos')),
    path ('salidas/', include(('salidas.urls', 'salidas'), namespace = 'salidas')),
    path ('plantas/', include(('plantas.urls', 'plantas'), namespace = 'plantas')),
    path ('tmuertos/', include(('tmuertos.urls', 'tmuertos'), namespace = 'tmuertos')),
    path ('operaciones/', include(('operaciones.urls', 'operaciones'), namespace = 'operaciones')),
    path ('nomina/', include(('nomina.urls', 'nomina'), namespace = 'nomina')),
    path ('apis/', include(('apis.urls', 'apis'), namespace = 'apis')),
    path ('admin/', admin.site.urls),
    path ('coreapi-docs/',include_docs_urls(title='Documentacion CoreAPI MarBran')),
    path ('admin/backups/', include('dbbackup_ui.urls')),
]
