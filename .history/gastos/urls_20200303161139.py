
from django.urls import path, include
from .views import CuentaGastosView, CuentaGastosNew, CuentaGastosEdit, cuenta_gastos_inactivar, \
    SubCuentaGastosView, SubCuentaGastosNew, SubCuentaGastosEdit, subcuenta_gastos_inactivar, \
        GastosCompletoList, GastosList, GastosNew

from .reportes_excel import CuentaGastosXls
from .reportes_pdf import cuenta_gastos_completo


urlpatterns = [
    path('gastos/',CuentaGastosView.as_view(), name="gastos_list"),
    path('gastos/new',CuentaGastosNew.as_view(), name="cuentas_gastos_new"),
    path('gastos/edit/<int:pk>',CuentaGastosEdit.as_view(), name="cuenta_gastos_edit"),
    path('gastos/estado/<int:id>', cuenta_gastos_inactivar, name="cuenta_gastos_inactivar"),

    path('subcuenta/',SubCuentaGastosView.as_view(), name="subcuenta_gastos_list"),
    path('subcuenta/new',SubCuentaGastosNew.as_view(), name="subcuentas_gastos_new"),
    path('subcuenta/edit/<int:pk>',SubCuentaGastosEdit.as_view(), name="subcuenta_gastos_edit"),
    path('subcuenta/estado/<int:id>', subcuenta_gastos_inactivar, name="subcuenta_gastos_inactivar"),
 
    path('relacion_gastos/',GastosCompletoList.as_view(), name="relacion_gastos_list"),
    path('listado_gastos/',GastosList.as_view(), name="gastos_list"),
    path('listado_gastos/new',GastosNew.as_view(), name="gastos_new"),
    path('listado_gastos/edit/<int:pk>',GastosList.as_view(), name="gastos_edit"),
    path('listado_gastos/estado/<int:id>', GastosList, name="gastos_delete"),

]
"""     
    
    path('gastos/estado/<int:id>', cuenta_gastos_inactivar, name="cuenta_gastos_inactivar"),
    path('gastos/reporte_all_pdf/', cuenta_gastos_completo,name='cuentas_gastos_pdf_all'),
    path('gastos/reporte_all_excel/', CuentaGastosXls.as_view(),name='cuentas_gastos_xls_all'), """