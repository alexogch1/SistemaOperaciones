from django.urls import path, include

from .views import NominaList, NominaNew, NominaEdit, NominaDel,NominaCompletaList

urlpatterns = [
    path('nomina/', NominaList.as_view(), name="nomina_list"),
    path('nomina_completa/', NominaCompletaList.as_view(), name="nomina_completa"),
    path('nomina/nueva/',NominaNew.as_view(),name="nomina_new"),
    path('nomina/editar/<int:pk>', NominaEdit.as_view() ,name="nomina_edit"),
    path('nomina/delete/<int:pk>', NominaDel.as_view() ,name="nomina_delete")
]