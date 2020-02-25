
from django.urls import path, include

from .views import ProduccionView, produccion, ProduccionDetDelete, \
    TiempoMuertoView, tiempos_muertos, TiempoMuertoDetDelete,\
        produccion_inactivar, tiempo_muerto_inactivar, \
        tiempos_muertos_resumen,\
            ProduccionCongView, produccion_cong, ProduccionCongDetDelete, \
                produccion_cong_inactivar, \
                    TiempoMuertoCongView, TiempoMuertoCompletoList  ,  tiempos_muertos_cong, TiempoMuertoCongDetDelete
    
from .reportes import reporte_produccion, imprimir_produccion_esp, imprimir_tiempos_muertos_esp,\
    reporte_tiempos_muertos
from.reportes_excel import TiempoMuertoCompletoXls
        

    

urlpatterns = [
    path('salidas/', ProduccionView.as_view(), name="produccion_list"),
    path('salidas/new', produccion, name="produccion_new"),
    path('salidas/edit/<int:produccion_id>',produccion, name="produccion_edit"),
    path('salidas/<int:produccion_id>/delete/<int:pk>',ProduccionDetDelete.as_view(), name="produccion_del"),
    path('salidas/produccion/estado/<int:id>', produccion_inactivar, name="Produccion_Inactivar"),

    path('salidas/listado', reporte_produccion, name='produccion_print_all'),
    path('salidas/<int:produccion_id>/imprimir', imprimir_produccion_esp, name='produccion_print_one'),

    path('salidas/tiempo-muerto', TiempoMuertoView.as_view(), name="tiempos_muertos_list"),
    path('salidas/tiempo_muerto_completo', TiempoMuertoCompletoList.as_view(), name="tiempos_muertos_completos"),
    
    path('salidas/tiempo-muerto/new', tiempos_muertos, name="tiempos_muertos_new"),
    path('salidas/tiempo-muerto/edit/<int:tiempo_muerto_id>',tiempos_muertos, name="tiempos_muertos_edit"),
    path('salidas/tiempo-muerto/<int:tiempo_muerto_id>/delete/<int:pk>',TiempoMuertoDetDelete.as_view(), name="tiempos_muertos_del"),
    path('salidas/tiempo-muerto/estado/<int:id>', tiempo_muerto_inactivar, name="TiempoMuerto_Inactivar"),
    path('salidas/tiempo_muerto_completo_excel', TiempoMuertoCompletoXls.as_view(), name="tiempos_muertos_completos_excel"),


    path('salidas/tiempo-muerto/listado', reporte_tiempos_muertos, name='tiempos_muertos_print_all'),
    path('salidas/tiempo-muerto/resumen', tiempos_muertos_resumen, name='tiempos_muertos_resumen'),

   
    path('prod/cong/', ProduccionCongView.as_view(), name="produccion_cong_list"),
    path('salidas/cong/new', produccion_cong, name="produccion_cong_new"),
    path('prod/edit/<int:produccion_cong_id>',produccion_cong, name="produccion_cong_edit"),
    path('prod/<int:produccion_cong_id>/delete/<int:pk>',ProduccionCongDetDelete.as_view(), name="produccion_cong_del"),
    path('salidas/produccion/cong/estado/<int:id>', produccion_cong_inactivar, name="Produccion_cong_Inactivar"),

    path('salidas/tiempo-muerto-cong', TiempoMuertoCongView.as_view(), name="tiempos_muertos_cong_list"),
    path('salidas/tiempo-muerto-cong/new', tiempos_muertos_cong, name="tiempos_muertos_cong_new"),
    path('prod/tiempo-muerto-cong/edit/<int:tiempo_muerto_cong_id>',tiempos_muertos_cong, name="tiempos_muertos_cong_edit"),
    path('prod/tiempo-muerto-cong/<int:tiempo_muerto_cong_id>/delete/<int:pk>',TiempoMuertoCongDetDelete.as_view(), name="tiempos_muertos_cong_del"),
    

    path('salidas/<int:produccion_id>/imprimir', imprimir_produccion_esp, name='produccion_print_one'),
    path('salidas/tiempos_muertos/<int:tiempo_muerto_id>/imprimir', imprimir_tiempos_muertos_esp, name='tiempos_muertos_print_one'),

    
]