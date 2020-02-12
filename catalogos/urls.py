
from django.urls import path, include

from .views import ClienteView,ClienteNew, ClienteEdit, Cliente_Inactivar, \
    MarcaView, MarcaNew, MarcaEdit, Marca_Inactivar, \
      IngredView, IngredNew, IngredEdit, Ingred_Inactivar, \
          CorteView, CorteNew, CorteEdit, Corte_Inactivar, \
            CasoEspView, CasoEspNew, CasoEspEdit, CasoEsp_Inactivar,\
              PresentacionView, PresentacionNew, PresentacionEdit, Presentacion_Inactivar, \
                ProductoView, ProductoNew, ProductoEdit, Producto_Inactivar, \
                IngredientView,CortView, PresentaView, MarcView, CEView

from.reportes_pdf import reporte_ingred_completo, reporte_corte_completo, reporte_presenta_completo, \
  reporte_cliente_completo, reporte_marcas_completo, reporte_ce_completo, reporte_productos_completo
from .reportes_excel import ReporteIngXls, ReporteCorteXls, ReportePresentaXls, ReporteClienteXls, \
  ReporteMarcaXls, ReporteCasoEspXls, ReporteProductoXls
    
urlpatterns = [
    path('ingreds/',IngredView.as_view(), name="ingred_list"),
    path('producto/buscar-ingred/',IngredientView.as_view(), name="producto_ingred"),
    path('ingreds/new',IngredNew.as_view(), name="ingred_new"),
    path('ingreds/edit/<int:pk>',IngredEdit.as_view(), name="ingred_edit"),
    path('ingredientes/estado/<int:id>', Ingred_Inactivar, name="ingred_inactivar"),
    path('ingredientes/reporte_all_pdf/', reporte_ingred_completo,name='ingred_reporte_pdf_all'),
    path('ingredientes/reporte_all_excel/', ReporteIngXls.as_view(),name='ingred_reporte_xls_all'),

    path('cortes/',CorteView.as_view(), name="corte_list"),
    path('producto/buscar-corte/',CortView.as_view(), name="producto_corte"),
    path('cortes/new',CorteNew.as_view(), name="corte_new"),
    path('cortes/edit/<int:pk>',CorteEdit.as_view(), name="corte_edit"),
    path('cortes/estado/<int:id>', Corte_Inactivar, name="corte_inactivar"),
    path('cortes/reporte_all_pdf/', reporte_corte_completo,name='cortes_reporte_pdf_all'),
    path('cortes/reporte_all_excel/', ReporteCorteXls.as_view(),name='cortes_reporte_xls_all'),


    path('presentaciones/',PresentacionView.as_view(), name="presentacion_list"),
    path('producto/buscar-presenta/',PresentaView.as_view(), name="producto_presenta"),
    path('presentaciones/new',PresentacionNew.as_view(), name="presentacion_new"),
    path('presentaciones/edit/<int:pk>',PresentacionEdit.as_view(), name="presentacion_edit"),
    path('presentaciones/estado/<int:id>', Presentacion_Inactivar, name="presentacion_inactivar"),
    path('presentaciones/reporte_all_pdf/', reporte_presenta_completo,name='presenta_reporte_pdf_all'),
    path('presentaciones/reporte_all_excel/', ReportePresentaXls.as_view(),name='presenta_reporte_xls_all'),

    path('clientes/',ClienteView.as_view(), name="cliente_list"),
    path('clientes/new',ClienteNew.as_view(), name="cliente_new"),
    path('clientes/edit/<int:pk>',ClienteEdit.as_view(), name="cliente_edit"),
    path('clientes/estado/<int:id>', Cliente_Inactivar, name="cliente_inactivar"),
    path('clientes/reporte_all_pdf/', reporte_cliente_completo,name='cliente_reporte_pdf_all'),
    path('clientes/reporte_all_excel/', ReporteClienteXls.as_view(),name='cliente_reporte_xls_all'),

    path('marcas/',MarcaView.as_view(), name="marca_list"),
    path('producto/buscar-marca/',MarcView.as_view(), name="producto_marca"),
    path('marcas/new',MarcaNew.as_view(), name="marca_new"),
    path('marcas/edit/<int:pk>',MarcaEdit.as_view(), name="marca_edit"),
    path('marcas/estado/<int:id>', Marca_Inactivar, name="marca_inactivar"),
    path('marcas/reporte_all_pdf/', reporte_marcas_completo,name='marcas_reporte_pdf_all'),
    path('marcas/reporte_all_excel/', ReporteMarcaXls.as_view(),name='marca_reporte_xls_all'),
  
    path('casos especiales/',CasoEspView.as_view(), name="ce_list"),
    path('producto/buscar-ce/',CEView.as_view(), name="producto_ce"),
    path('casos especiales/new',CasoEspNew.as_view(), name="ce_new"),
    path('casos especiales/edit/<int:pk>',CasoEspEdit.as_view(), name="ce_edit"),
    path('casos especiales/estado/<int:id>', CasoEsp_Inactivar, name="ce_inactivar"),
    path('casos especiales/reporte_all_pdf/', reporte_ce_completo,name='ce_reporte_pdf_all'),
    path('casos especiales/reporte_all_excel/', ReporteCasoEspXls.as_view(),name='ce_reporte_xls_all'),

    path('productos/edit/<int:pk>',ProductoEdit.as_view(), name="producto_edit"),
    path('productos/estado/<int:id>', Producto_Inactivar, name="producto_inactivar"),
    path('products/',ProductoView.as_view(), name="producto_list"),
    path('products/new',ProductoNew.as_view(),name='producto_new'),
    path('products/reporte_all_pdf/', reporte_productos_completo,name='productos_reporte_pdf_all'),
    path('products/reporte_all_excel/', ReporteProductoXls.as_view(),name='productos_reporte_xls_all'),
    


]