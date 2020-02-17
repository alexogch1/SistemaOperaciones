from django.urls import path
from django.contrib.auth import views as auth_views

from generales.views import Home, HomeSinPrivilegios, Mision


urlpatterns = [

    path('',Mision.as_view(), name='mision'),
 
]