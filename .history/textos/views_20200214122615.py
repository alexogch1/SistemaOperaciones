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