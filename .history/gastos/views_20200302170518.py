from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from django.http import HttpResponse
import json

from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin

from django.contrib.auth.decorators import login_required, permission_required

from .models import GastosCuenta, GastosSubCuenta
from generales.views import SinPrivilegios
from .forms import CuentaGastosForm, SubCuentaGastosForm

class CuentaGastosView(SinPrivilegios ,generic.ListView):
    model=GastosCuenta
    template_name='gastos/cuenta_gastos_list.html'
    context_object_name='obj'
    permission_required='gastos.view_gastoscuenta'

class CuentaGastosNew( SinPrivilegios, generic.CreateView):
    permission_required = "gastos.add_gastoscuenta"
    model = GastosCuenta
    template_name = "gastos/cuenta_gastos_form.html"
    context_object_name = "obj"
    form_class = CuentaGastosForm
    success_url = reverse_lazy("gastos:gastos_list")
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class CuentaGastosEdit(SinPrivilegios ,generic.UpdateView):
    permission_required = "gastos.update_gastoscuenta"
    model = GastosCuenta
    template_name = "gastos/cuenta_gastos_form.html"
    context_object_name = "obj"
    form_class = CuentaGastosForm
    success_url = reverse_lazy("gastos:gastos_list")

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url="/login/")
@permission_required("catalogos.update_gastoscuenta",login_url="/login/")
def cuenta_gastos_inactivar(request,id):
    CuentaGastos = GastosCuenta.objects.filter(pk=id).first()

    if request.method=="POST":
        if CuentaGastos:
            CuentaGastos.estado = not CuentaGastos.estado
            CuentaGastos.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")

class SubCuentaGastosView(SinPrivilegios, generic.ListView):
    permission_required = "gastos.view_gastossubcuenta"
    model = GastosSubCuenta
    template_name = "gastos/subcuenta_gastos_list.html"
    context_object_name = "obj"
    id_cuenta = GastosSubCuenta.objects.cuenta_id.first()
    queryset = GastosCuenta.objects.first(id = 'cuenta_id')

    def get_context_data(self, **kwargs):
        context = super(SubCuentaGastosView, self).get_context_data(**kwargs)
        context['detalles'] = GastosSubCuenta.objects.first()
        context['encabezado'] = self.queryset
        return context
 

""" class NominaCompletaList(generic.ListView):
    template_name='nomina/nomina_completa.html'
    context_object_name='nomina'
    queryset = NominaEnc.objects.all()

    def get_context_data(self, **kwargs):
        context = super(NominaCompletaList, self).get_context_data(**kwargs)
        context['detalles'] = NominaDet.objects.all()
        context['encabezado'] = self.queryset
        return context  """



class SubCuentaGastosNew(SinPrivilegios, generic.CreateView):
    permission_required = "catalogos.add_gastossubcuenta"
    model = GastosSubCuenta
    template_name = "gastos/subcuenta_gastos_form.html"
    context_object_name = "obj"
    form_class = SubCuentaGastosForm
    success_url = reverse_lazy("gastos:subcuenta_gastos_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

"""class MarcaEdit(SinPrivilegios, generic.UpdateView):
    permission_required = "catalogos.update_Marca"
    model = Marca
    template_name = "catalogos/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("catalogos:marca_list")


    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


@login_required(login_url="/login/")
@permission_required("catalogos.change_marca",login_url="/login/")
def Marca_Inactivar(request,id):
    marca = Marca.objects.filter(pk=id).first()

    if request.method=="POST":
        if marca:
            marca.estado = not marca.estado
            marca.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL") """