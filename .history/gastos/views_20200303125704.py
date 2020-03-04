from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from django.http import HttpResponse
import json

from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin

from django.contrib.auth.decorators import login_required, permission_required

from .models import GastosCuenta, GastosSubCuenta, UnidNegocio, AreaGasto, GastoEnc, GastoDet
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



class SubCuentaGastosNew(SinPrivilegios, generic.CreateView):
    permission_required = "gastos.add_gastossubcuenta"
    model = GastosSubCuenta
    template_name = "gastos/subcuenta_gastos_form.html"
    context_object_name = "obj"
    form_class = SubCuentaGastosForm
    success_url = reverse_lazy("gastos:subcuenta_gastos_list")

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SubCuentaGastosEdit(SinPrivilegios, generic.UpdateView):
    permission_required = "gastos.change_gastossubcuenta"
    model = GastosSubCuenta
    template_name = "gastos/subcuenta_gastos_form.html"
    context_object_name = "obj"
    form_class = SubCuentaGastosForm
    success_url = reverse_lazy("gastos:subcuenta_gastos_list")


    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


@login_required(login_url="/login/")
@permission_required("gastos.change_gastossubcuenta",login_url="/login/")
def subcuenta_gastos_inactivar(request,id):
    subcuenta = GastosSubCuenta.objects.filter(pk=id).first()

    if request.method=="POST":
        if subcuenta:
            subcuenta.estado = not subcuenta.estado
            subcuenta.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")

class GastosCompletoList(generic.ListView):
    template_name='gastos/gastos_completos.html'
    context_object_name='gastos'
    queryset = GastoEnc.objects.all()

    def get_context_data(self, **kwargs):
        context = super(GastosCompletoList, self).get_context_data(**kwargs)
        context['detalles'] = GastoDet.objects.all()
        context['encabezado'] = self.queryset
        return context 

class GastosList(generic.ListView):
    model=GastoEnc
    template_name='gastos/gastos_list.html'
    context_object_name='gastos'

    def get_context_data(self, **kwargs):
        context = super(GastosList, self).get_context_data(**kwargs)
        initial_date = self.request.GET.get('fecha_inicial')
        final_date = self.request.GET.get('fecha_final')
        if  not initial_date or not final_date:
            context ['gastos'] = GastoEnc.objects.order_by('fecha_registro')
        else:
            initial_date = parse(initial_date)
            final_date = parse(final_date)    
            context['gastos'] = GastoEnc.objects.filter(fecha_registro__gte=initial_date, fecha_registro__lte=final_date )
        return context