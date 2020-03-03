
from django.urls import path, include
from .views import CuentaGastosView, CuentaGastosNew, CuentaGastosEdit, cuenta_gastos_inactivar, \
    SubCuentaGastosView, SubCuentaGastosNew, SuCuentaGastosEdit

from .reportes_excel import CuentaGastosXls
from .reportes_pdf import cuenta_gastos_completo


urlpatterns = [
    path('gastos/',CuentaGastosView.as_view(), name="gastos_list"),
    path('gastos/new',CuentaGastosNew.as_view(), name="cuentas_gastos_new"),
    path('gastos/edit/<int:pk>',CuentaGastosEdit.as_view(), name="cuenta_gastos_edit"),
    path('gastos/estado/<int:id>', cuenta_gastos_inactivar, name="cuenta_gastos_inactivar"),

    path('subcuenta/',SubCuentaGastosView.as_view(), name="subcuenta_gastos_list"),
    path('subcuenta/new',SubCuentaGastosNew.as_view(), name="subcuentas_gastos_new"),
    path('subcuenta/edit/<int:pk>',SuCuentaGastosEdit.as_view(), name="subcuenta_gastos_edit"),
    path('subcuenta/estado/<int:id>', subcuenta_gastos_inactivar, name="subcuenta_gastos_inactivar"),
 


]
"""     
    
    path('gastos/estado/<int:id>', cuenta_gastos_inactivar, name="cuenta_gastos_inactivar"),
    path('gastos/reporte_all_pdf/', cuenta_gastos_completo,name='cuentas_gastos_pdf_all'),
    path('gastos/reporte_all_excel/', CuentaGastosXls.as_view(),name='cuentas_gastos_xls_all'), """