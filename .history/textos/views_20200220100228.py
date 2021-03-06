from django.shortcuts import render

from django.http import HttpResponseRedirect

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, \
        PermissionRequiredMixin

from django.http import HttpResponse
from django.views import generic


    
class Mision (LoginRequiredMixin, generic.TemplateView):
    template_name = 'textos/mision.html'
    login_url = 'generales:login'

class Vision (LoginRequiredMixin, generic.TemplateView):
    template_name = 'textos/vision.html'
    login_url = 'generales:login'

class Valores (LoginRequiredMixin, generic.TemplateView):
    template_name = 'textos/valores.html'
    login_url = 'generales:login'

class PoliCal (LoginRequiredMixin, generic.TemplateView):
    template_name = 'textos/politica_calidad.html'
    login_url = 'generales:login'

class Core (LoginRequiredMixin, generic.TemplateView):
    template_name = 'textos/core_business.html'
    login_url = 'generales:login'

class ValorCliente (LoginRequiredMixin, generic.TemplateView):
    template_name = 'textos/valor_cliente.html'
    login_url = 'generales:login'

class ValorAccionistas (LoginRequiredMixin, generic.TemplateView):
    template_name = 'textos/valor_accionistas.html'
    login_url = 'generales:login'

class ValorAsociados (LoginRequiredMixin, generic.TemplateView):
    template_name = 'textos/valor_asociados.html'
    login_url = 'generales:login'