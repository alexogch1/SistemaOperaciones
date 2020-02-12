from django.shortcuts import render
from django.views import generic

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse

from generales.views import SinPrivilegios
from .models import CategoriaTM, CausaTM
from .forms import CategoriaTMForm, CausaTMForm

class CategoriaTMView(SinPrivilegios, generic.ListView):
    permission_required = "tmuertos.view_categoriaTM"
    model = CategoriaTM
    template_name = "tmuertos/categoriaTM_list.html"
    context_object_name = "obj"

class VistaBaseCreate(SuccessMessageMixin,SinPrivilegios,\
    generic.CreateView):
    context_object_name='obj'
    Success_Message="Registro Agregado Satisfactoriamente"

    def form_valid(self,form):
        form.instance.uc=self.request.user
        return super().form_valid(form)

class VistaBaseEdit(SuccessMessageMixin,SinPrivilegios,\
    generic.UpdateView):
    context_object_name='obj'
    Success_Message="Registro Actualizado Satisfactoriamente"

    def form_valid(self,form):
        form.instance.um=self.request.user.id
        return super().form_valid(form)

class CategoriaTMNew(VistaBaseCreate):
    model = CategoriaTM
    template_name="tmuertos/categoriaTM_form.html"
    form_class=CategoriaTMForm
    success_url= reverse_lazy("tmuertos:categoriaTM_list")
    permission_required="tmuertos.add_categoriaTM"

class CategoriaTMEdit(VistaBaseEdit):
    model = CategoriaTM
    template_name="tmuertos/categoriaTM_form.html"
    form_class=CategoriaTMForm
    success_url= reverse_lazy("tmuertos:categoriaTM_list")
    permission_required="tmuertos.change_categoriaTM"

@login_required(login_url="/login/")
@permission_required("tmuertos.change_causaTM",login_url="/login/")
def categoriaTMInactivar(request,id):
    categoriaTM = CategoriaTM.objects.filter(pk=id).first()

    if request.method=="POST":
        if categoriaTM:
            categoriaTM.estado = not categoriaTM.estado
            categoriaTM.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")

class CausaTMView(SinPrivilegios, generic.ListView):
    model = CausaTM
    template_name = "tmuertos/causaTM_list.html"
    context_object_name = "obj"
    permission_required="tmuertos.view_causaTM"

class CausaTMNew(VistaBaseCreate):
    model = CausaTM
    template_name="tmuertos/causaTM_form.html"
    form_class=CausaTMForm
    success_url= reverse_lazy("tmuertos:causaTM_list")
    permission_required="tmuertos.add_causaTM"

class CausaTMEdit(VistaBaseEdit):
    model = CausaTM
    template_name="tmuertos/causaTM_form.html"
    form_class=CausaTMForm
    success_url= reverse_lazy("tmuertos:causaTM_list")
    permission_required="tmuertos.change_causaTM"

@login_required(login_url="/login/")
@permission_required("tmuertos.change_causaTM",login_url="/login/")
def causaTMInactivar(request,id):
    causaTM = CausaTM.objects.filter(pk=id).first()

    if request.method=="POST":
        if causaTM:
            causaTM.estado = not causaTM.estado
            causaTM.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")