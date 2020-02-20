from django.shortcuts import render

from django.http import HttpResponseRedirect

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, \
        PermissionRequiredMixin

from django.http import HttpResponse
from django.views import generic


class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin):
        login_url = 'generales:login'
        raise_exception = False
        redirect_field_name = "redirect_to" 

        def handle_no_permission(self):
                from django.contrib.auth.models import AnonymousUser 
                if not self.request.user==AnonymousUser:
                        self.login_url = 'generales:sin_privilegios'  
                return HttpResponseRedirect(reverse_lazy(self.login_url))


class Home (LoginRequiredMixin, generic.TemplateView):
    template_name = 'generales/home.html'
    login_url = 'generales:login'

class HomeSinPrivilegios (LoginRequiredMixin, generic.TemplateView):
    template_name = 'generales/sin_privilegios.html'
    
