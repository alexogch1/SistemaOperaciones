from django.urls import path

from .views import TipoCambioView, TipoCambioNew,tc_inactivar,\
    TipoCambioEdit, ReporteTC

from .reportes_pdf import reporte_tc_completo
urlpatterns = [
    path('tc/', TipoCambioView.as_view(),name='tc_list'),
    path('tc/new/', TipoCambioNew.as_view(),name='tc_new'),
    path('tc/edit/<int:pk>', TipoCambioEdit.as_view(),name='tc_edit'),
    path('tc/estado/<int:id>', tc_inactivar, name="tc_inactivar"),
    path('tc/reporte_excel/', ReporteTC.as_view(),name='tc_reporte'),
    path('tc/reporte_all_pdf/', reporte_tc_completo,name='tc_reporte_pdf_all')
    
]