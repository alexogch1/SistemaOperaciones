from django.urls import path
from django.contrib.auth import views as auth_views

from textos.views import  Mision


urlpatterns = [

    path('textos/',Mision.as_view(), name='mision'),
 
]