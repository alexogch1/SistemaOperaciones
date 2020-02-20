from django.urls import path
from django.contrib.auth import views as auth_views

from textos.views import  Mision, Vision, Valores


urlpatterns = [

    path('mision/',Mision.as_view(), name='mision'),
    path('vision/',Vision.as_view(), name='vision'),
    path('valores/',Vision.as_view(), name='valores'),
 
]