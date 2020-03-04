from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from django.http import HttpResponse
import json

from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin
from dateutil.parser import parse

from django.contrib.auth.decorators import login_required, permission_required

from .models import GastosCuenta, GastosSubCuenta, UnidNegocio, AreaGasto, GastoEnc, GastoDet
from generales.views import SinPrivilegios
from .forms import CuentaGastosForm, SubCuentaGastosForm, GastosEncForm, GastosDetForm, DetalleGastosFormSet

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


class GastosNew(SinPrivilegios, generic.CreateView):
    permission_required='nomina.add_gastoenc'
    model=GastoEnc
    login_url='generales:home'
    template_name='gastos/gastos_form.html'
    form_class=GastosEncForm
    success_url=reverse_lazy('gastos:gastos_list')

    def get(self, request, *args, **kwargs):
        self.object=None
        form_class=self.get_form_class()
        form=self.get_form(form_class)
        detalle_gastos_formset=DetalleGastosFormSet()
        return self.render_to_response(
            self.get_context_data(
                form=form,
                detalle_gastos = detalle_gastos_formset
            )
        )
    
    def post(self, request, *args, **kwargs):
        form_class=self.get_form_class()
        form=self.get_form(form_class)
        detalle_gastos=DetalleGastosFormSet(request.POST)

        if form.is_valid() and detalle_gastos.is_valid():
            return self.form_valid(form, detalle_gastos)
        else:
            return self.form_invalid(form, detalle_gastos)

    def form_valid(self, form, detalle_gastos):
        self.object=form.save()
        detalle_gastos.instance=self.object
        detalle_gastos.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, detalle_gastos):
        return self.render_to_response(
            self.get_context_data(
                form=form, 
                detalle_gastos=detalle_gastos
            )
        )

class NominaEdit(SinPrivilegios,generic.UpdateView):
    permission_required='nomina.change_nominaenc'
    model=NominaEnc
    login_url='generales:home'
    template_name='nomina/nomina_form.html'
    form_class=NominaEncForm
    success_url=reverse_lazy('nomina:nomina_list')

    def get_success_url(self):
        from django.urls import reverse
        return reverse ('nomina:nomina_edit',
        kwargs={'pk':self.get_object().id})

    def get (self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalles =NominaDet.objects.filter(nomina=self.object).order_by('pk')
        detalles_data = []
        for detalle in detalles:
            d={
                'concepto':detalle.concepto,
                'cantidad':detalle.cantidad
            }
            detalles_data.append(d)

        detalle_nomina = DetalleNominaFormSet(initial=detalles_data)
        detalle_nomina.extra += len(detalles_data)
        return self.render_to_response(
            self.get_context_data(
                form=form,
                detalle_nomina = detalle_nomina
            )
        )

    def post(self,request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form=self.get_form(form_class)
        detalle_nomina = DetalleNominaFormSet(request.POST)
        if form.is_valid() and detalle_nomina.is_valid():
            return self.form_valid(form, detalle_nomina)
        else:
            return self.form_valid(form, detalle_nomina)

        
    def form_valid(self, form, detalle_nomina):
        self.object = form.save()
        detalle_nomina.instance =self.object
        NominaDet.objects.filter(nomina=self.object).delete()
        detalle_nomina.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, detalle_nomina):
        return self.render_to_response(
            self.get_context_data(
                form=form, 
                detalle_nomina=detalle_nomina
            )
        )

class GastosDel(SinPrivilegios,generic.DeleteView):
    permission_required='gastos:delete_gastoenc'
    model= GastoEnc
    template_name = 'gastos/gastos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy('gastos:gastos_list')

    