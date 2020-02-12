
from django.urls import path, include

from .views import PlantaView, PlantaNew, PlantaEdit, Planta_Inactivar, \
    LineaView, LineaNew, LineaEdit, Linea_Inactivar, \
        SupervisorView, SupervisorNew, SupervisorEdit, Supervisor_Inactivar, \
            OperadorView, OperadorNew, OperadorEdit, Operador_Inactivar, \
                BasculaView, BasculaNew, BasculaEdit, BasculaInactivar, \
                    FormadoraView, FormadoraNew, FormadoraEdit, FormadoraInactivar
                
    
    

urlpatterns = [
    path('plantas/',PlantaView.as_view(), name="planta_list"),
    path('plantas/new',PlantaNew.as_view(), name="planta_new"),
    path('plantas/edit/<int:pk>',PlantaEdit.as_view(), name="planta_edit"),
    path('plantas/estado/<int:id>', Planta_Inactivar, name="planta_inactivar"),

    path('lineas/',LineaView.as_view(), name="linea_list"),
    path('lineas/new',LineaNew.as_view(), name="linea_new"),
    path('lineas/edit/<int:pk>',LineaEdit.as_view(), name="linea_edit"),
    path('lineas/estado/<int:id>', Linea_Inactivar, name="linea_inactivar"),

    path('basculas/',BasculaView.as_view(), name="bascula_list"),
    path('basculas/new',BasculaNew.as_view(), name="bascula_new"),
    path('basculas/edit/<int:pk>',BasculaEdit.as_view(), name="bascula_edit"),
    path('basculas/estado/<int:id>', BasculaInactivar, name="bascula_inactivar"),

    path('formadoras/',FormadoraView.as_view(), name="formadora_list"),
    path('formadoras/new',FormadoraNew.as_view(), name="formadora_new"),
    path('formadoras/edit/<int:pk>',FormadoraEdit.as_view(), name="formadora_edit"),
    path('formadoras/estado/<int:id>', FormadoraInactivar, name="formadora_inactivar"),

    path('supervisores/',SupervisorView.as_view(), name="supervisor_list"),
    path('supervisores/new',SupervisorNew.as_view(), name="supervisor_new"),
    path('supervisores/edit/<int:pk>',SupervisorEdit.as_view(), name="supervisor_edit"),
    path('supervisores/estado/<int:id>', Supervisor_Inactivar, name="Supervisor_Inactivar"),

    path('operadores/',OperadorView.as_view(), name="operador_list"),
    path('operadores/new',OperadorNew.as_view(), name="operador_new"),
    path('operadores/edit/<int:pk>',OperadorEdit.as_view(), name="operador_edit"),
    path('operadores/estado/<int:id>', Operador_Inactivar, name="Operador_Inactivar"),

]