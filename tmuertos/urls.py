from django.urls import path, include

from .views import CategoriaTMView, CategoriaTMNew, CategoriaTMEdit, categoriaTMInactivar, \
    CausaTMView, CausaTMNew, CausaTMEdit, causaTMInactivar

from .reportes_excel import ReporteCatTMXls, ReporteCausaTMXls

urlpatterns = [
    path ('categoriasTM/', CategoriaTMView.as_view(), name= "categoriaTM_list"),
    path('CategoriasTM/new', CategoriaTMNew.as_view(), name="categoriaTM_new"),
    path('CategoriasTM/<int:pk>', CategoriaTMEdit.as_view(), name="categoriaTM_edit"),
    path('CategoriasTM/estado/<int:id>', categoriaTMInactivar, name="categoriaTM_inactivar"),
    path('CategoriasTM/reporte_all_excel/', ReporteCatTMXls.as_view(),name='cat_tm_reporte_xls_all'),

    path ('causasTM/', CausaTMView.as_view(), name= "causaTM_list"),
    path('CausasTM/new', CausaTMNew.as_view(), name="causaTM_new"),
    path('CausasTM/<int:pk>', CausaTMEdit.as_view(), name="causaTM_edit"),
    path('CausasTM/estado/<int:id>', causaTMInactivar, name="causaTM_inactivar"),
    path('CausasTM/reporte_all_excel/', ReporteCausaTMXls.as_view(),name='causas_tm_reporte_xls_all'),

]   