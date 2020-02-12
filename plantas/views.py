from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from django.http import HttpResponse
import json

from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin

from django.contrib.auth.decorators import login_required, permission_required
    
from .models import Planta, Linea, Supervisor, Operador, Bascula, Formadora
from .forms import PlantaForm, LineaForm, SupervisorForm, OperadorForm, BasculaForm,\
FormadoraForm

from generales.views import SinPrivilegios

class PlantaView(SinPrivilegios, generic.ListView):
    permission_required = "plantas.view_planta"
    model = Planta
    template_name = "plantas/planta_list.html"
    context_object_name = "obj"

class PlantaNew(SinPrivilegios, generic.CreateView):
    permission_required = "plantas.add_planta"
    model = Planta
    template_name = "plantas/planta_form.html"
    context_object_name = "obj"
    form_class = PlantaForm
    success_url = reverse_lazy("plantas:planta_list")


    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

#flag
class PlantaEdit(SinPrivilegios, generic.UpdateView):
    permission_required = "plantas.update_planta"
    model = Planta
    template_name = "plantas/planta_form.html"
    context_object_name = "obj"
    form_class = PlantaForm
    success_url = reverse_lazy("plantas:planta_list")


    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

        
@login_required(login_url="/login/")
@permission_required("plantas.change_planta",login_url="/login/")
def Planta_Inactivar(request,id):
    planta = Planta.objects.filter(pk=id).first()

    if request.method=="POST":
        if planta:
            planta.estado = not planta.estado
            planta.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")

class LineaView(SinPrivilegios, generic.ListView):
    permission_required = "plantas.view_linea"
    model = Linea
    template_name = "plantas/linea_list.html"
    context_object_name = "obj"
    

class LineaNew(SinPrivilegios, generic.CreateView):
    permission_required = "plantas.add_linea"
    model = Linea
    template_name = "plantas/linea_form.html"
    context_object_name = "obj"
    form_class = LineaForm
    success_url = reverse_lazy("plantas:linea_list")
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class LineaEdit(SinPrivilegios, generic.UpdateView):
    model = Linea
    template_name = "plantas/linea_form.html"
    context_object_name = "obj"
    form_class = LineaForm
    success_url = reverse_lazy("plantas:linea_list")
    permission_required = "plantas.update_linea"
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


@login_required(login_url="/login/")
@permission_required("plantas.change_linea",login_url="/login/")
def Linea_Inactivar(request,id):
    linea = Linea.objects.filter(pk=id).first()

    if request.method=="POST":
        if linea:
            linea.estado = not linea.estado
            linea.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")

class SupervisorView(SinPrivilegios, generic.ListView):
    permission_required = "plantas.view_supervisor"
    model = Supervisor
    template_name = "plantas/supervisor_list.html"
    context_object_name = "obj"
    

class SupervisorNew(SinPrivilegios, generic.CreateView):
    permission_required = "plantas.add_supervisor"
    model = Supervisor
    template_name = "plantas/supervisor_form.html"
    context_object_name = "obj"
    form_class = SupervisorForm
    success_url = reverse_lazy("plantas:supervisor_list")
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SupervisorEdit(SinPrivilegios, generic.UpdateView):
    model = Supervisor
    template_name = "plantas/supervisor_form.html"
    context_object_name = "obj"
    form_class = SupervisorForm
    success_url = reverse_lazy("plantas:supervisor_list")
    permission_required = "plantas.update_supervisor"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


@login_required(login_url="/login/")
@permission_required("plantas.change_supervisor",login_url="/login/")
def Supervisor_Inactivar(request,id):
    supervisor = Supervisor.objects.filter(pk=id).first()

    if request.method=="POST":
        if supervisor:
            supervisor.estado = not supervisor.estado
            supervisor.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")

class OperadorView(SinPrivilegios, generic.ListView):
    permission_required = "plantas.view_operador"
    model = Operador
    template_name = "plantas/operador_list.html"
    context_object_name = "obj"
    

class OperadorNew(SinPrivilegios, generic.CreateView):
    permission_required = "plantas.add_operador"
    model = Operador
    template_name = "plantas/operador_form.html"
    context_object_name = "obj"
    form_class = OperadorForm
    success_url = reverse_lazy("plantas:operador_list")
    
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class OperadorEdit(SinPrivilegios, generic.UpdateView):
    model = Operador
    template_name = "plantas/operador_form.html"
    context_object_name = "obj"
    form_class = OperadorForm
    success_url = reverse_lazy("plantas:operador_list")
    permission_required = "plantas.change_operador"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url="/login/")
@permission_required("plantas.change_operador",login_url="/login/")
def Operador_Inactivar(request,id):
    operador = Operador.objects.filter(pk=id).first()

    if request.method=="POST":
        if operador:
            operador.estado = not operador.estado
            operador.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")

class BasculaView(SinPrivilegios, generic.ListView):
    permission_required = "plantas.view_bascula"
    model = Bascula
    template_name = "plantas/bascula_list.html"
    context_object_name = "obj"
    

class BasculaNew(SinPrivilegios, generic.CreateView):
    permission_required = "plantas.add_bascula"
    model = Bascula
    template_name = "plantas/bascula_form.html"
    context_object_name = "obj"
    form_class = BasculaForm
    success_url = reverse_lazy("plantas:bascula_list")
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class BasculaEdit(SinPrivilegios, generic.UpdateView):
    model = Bascula
    template_name = "plantas/bascula_form.html"
    context_object_name = "obj"
    form_class = BasculaForm
    success_url = reverse_lazy("plantas:bascula_list")
    permission_required="plantas.change_bascula"
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)



@login_required(login_url="/login/")
@permission_required("plantas.change_bascula",login_url="/login/")
def BasculaInactivar(request,id):
    bascula = Bascula.objects.filter(pk=id).first()

    if request.method=="POST":
        if bascula:
            print('estado de la bascula', bascula.estado)

            
            bascula.estado = not bascula.estado
            bascula.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")

class FormadoraView(SinPrivilegios, generic.ListView):
    permission_required = "plantas.view_formadora"
    model = Formadora
    template_name = "plantas/formadora_list.html"
    context_object_name = "obj"
    

class FormadoraNew(SinPrivilegios, generic.CreateView):
    permission_required = "plantas.add_formadora"
    model = Formadora
    template_name = "plantas/formadora_form.html"
    context_object_name = "obj"
    form_class = FormadoraForm
    success_url = reverse_lazy("plantas:formadora_list")
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class FormadoraEdit(SinPrivilegios, generic.UpdateView):
    model = Formadora
    template_name = "plantas/formadora_form.html"
    context_object_name = "obj"
    form_class = FormadoraForm
    success_url = reverse_lazy("plantas:formadora_list")
    permission_required="plantas.change_formadora"
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)



@login_required(login_url="/login/")
@permission_required("plantas.change_formadora",login_url="/login/")
def FormadoraInactivar(request,id):
    formadora = Formadora.objects.filter(pk=id).first()

    if request.method=="POST":
        if formadora:
            formadora.estado = not formadora.estado
            formadora.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")