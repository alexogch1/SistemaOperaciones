from django.shortcuts import render,redirect, get_object_or_404
from django.http import JsonResponse
from django.views import generic
from django.urls import reverse_lazy

from django.http import HttpResponse



from salidas.models import ProduccionEnc, ProduccionDet, TiempoMuertoEnc, TiempoMuertonDet
from salidas.forms import ProduccionEncForm, TiempoMuertoEncForm
from generales.views import SinPrivilegios
from catalogos.models import Ingred, Producto
from tmuertos.models import CausaTM
from plantas.models import Planta, Linea, Supervisor, Operador

    

