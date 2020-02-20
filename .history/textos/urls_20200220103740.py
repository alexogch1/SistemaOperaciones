from django.urls import path
from django.contrib.auth import views as auth_views

from textos.views import  Mision, Vision, Valores, PoliCal, Core,ValorCliente,\
    ValorAccionistas, ValorAsociados, FoodDefense


urlpatterns = [

    path('mision/',Mision.as_view(), name='mision'),
    path('vision/',Vision.as_view(), name='vision'),
    path('valores/',Valores.as_view(), name='valores'),
    path('politica_calidad/',PoliCal.as_view(), name='politica_calidad'),
    path('core_business/',Core.as_view(), name='core_business'),
    path('valor_cliente/',ValorCliente.as_view(), name='valor_cliente'),
    path('valor_accionistas/',ValorAccionistas.as_view(), name='valor_accionistas'),
    path('valor_asociados/',ValorAsociados.as_view(), name='valor_asociados'),
    path('food_defense/',FoodDefense.as_view(), name='food_defense'),
 
]