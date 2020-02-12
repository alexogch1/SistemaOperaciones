from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from django.http import HttpResponse
import json

from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin

from django.contrib.auth.decorators import login_required, permission_required
    
from .models import Cliente, Marca, Ingred, Corte, CasoEsp, Presentacion, Producto
from .forms import ClienteForm, MarcaForm, IngredForm,\
    CorteForm, CasoEspForm, PresentacionForm, ProductoForm

#import .views as vistas 

from generales.views import SinPrivilegios

class ClienteView(SinPrivilegios, generic.ListView):
    permission_required = "catalogos.view_cliente"
    model = Cliente
    template_name = "catalogos/cliente_list.html"
    context_object_name = "obj"
    
class ClienteNew(SinPrivilegios, generic.CreateView):
    permission_required = "catalogos.add_cliente"
    model = Cliente
    template_name = "catalogos/cliente_form.html"
    context_object_name = "obj"
    form_class = ClienteForm
    success_url = reverse_lazy("catalogos:cliente_list")


    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ClienteEdit(SinPrivilegios, generic.UpdateView):
    permission_required = "catalogos.change_cliente"
    model = Cliente
    template_name = "catalogos/cliente_form.html"
    context_object_name = "obj"
    form_class = ClienteForm
    success_url = reverse_lazy("catalogos:cliente_list")


    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

        
@login_required(login_url="/login/")
@permission_required("catalogos.change_cliente",login_url="/login/")
def Cliente_Inactivar(request,id):
    cliente = Cliente.objects.filter(pk=id).first()

    if request.method=="POST":
        if cliente:
            cliente.estado = not cliente.estado
            cliente.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    return HttpResponse("FAIL")
    return render(request, template_name,contexto)
    
class MarcaView(SinPrivilegios, generic.ListView):
    permission_required = "catalogos.view_Marca"
    model = Marca
    template_name = "catalogos/marca_list.html"
    context_object_name = "obj"


class MarcaNew(SinPrivilegios, generic.CreateView):
    permission_required = "catalogos.add_Marca"
    model = Marca
    template_name = "catalogos/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("catalogos:marca_list")


    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class MarcaEdit(SinPrivilegios, generic.UpdateView):
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
    
    return HttpResponse("FAIL")

class IngredView(SinPrivilegios, generic.ListView):
    permission_required = "catalogos.view_ingred"
    model = Ingred
    template_name = "catalogos/ingred_list.html"
    context_object_name = "obj"


class IngredNew(SinPrivilegios, generic.CreateView):
    permission_required = "catalogos.add_ingred"
    model = Ingred
    template_name = "catalogos/ingred_form.html"
    context_object_name = "obj"
    form_class = IngredForm
    success_url = reverse_lazy("catalogos:ingred_list")


    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class IngredEdit(SinPrivilegios, generic.UpdateView):
    permission_required = "catalogos.update_ingred"
    model = Ingred
    template_name = "catalogos/ingred_form.html"
    context_object_name = "obj"
    form_class = IngredForm
    success_url = reverse_lazy("catalogos:ingred_list")


    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url="/login/")
@permission_required("catalogos.change_ingred",login_url="/login/")
def Ingred_Inactivar(request,id):
    ingred = Ingred.objects.filter(pk=id).first()

    if request.method=="POST":
        if ingred:
            ingred.estado = not ingred.estado
            ingred.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")


class CorteView(SinPrivilegios, generic.ListView):
    permission_required = "catalogos.view_corte"
    model = Corte
    template_name = "catalogos/corte_list.html"
    context_object_name = "obj"


class CorteNew(SinPrivilegios, generic.CreateView):
    permission_required = "catalogos.add_corte"
    model = Corte
    template_name = "catalogos/corte_form.html"
    context_object_name = "obj"
    form_class = CorteForm
    success_url = reverse_lazy("catalogos:corte_list")


    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class CorteEdit(SinPrivilegios, generic.UpdateView):
    permission_required = "catalogos.update_corte"
    model = Corte
    template_name = "catalogos/corte_form.html"
    context_object_name = "obj"
    form_class = CorteForm
    success_url = reverse_lazy("catalogos:corte_list")


    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


@login_required(login_url="/login/")
@permission_required("catalogos.change_corte",login_url="/login/")
def Corte_Inactivar(request,id):
    corte = Corte.objects.filter(pk=id).first()

    if request.method=="POST":
        if corte:
            corte.estado = not corte.estado
            corte.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")

class CasoEspView(SinPrivilegios, generic.ListView):
    permission_required = "catalogos.view_ce"
    model = CasoEsp
    template_name = "catalogos/ce_list.html"
    context_object_name = "obj"


class CasoEspNew(SinPrivilegios, generic.CreateView):
    permission_required = "catalogos.add_ce"
    model = CasoEsp
    template_name = "catalogos/ce_form.html"
    context_object_name = "obj"
    form_class = CasoEspForm
    success_url = reverse_lazy("catalogos:ce_list")


    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class CasoEspEdit(SinPrivilegios, generic.UpdateView):
    permission_required = "catalogos.update_ce"
    model = CasoEsp
    template_name = "catalogos/ce_form.html"
    context_object_name = "obj"
    form_class = CasoEspForm
    success_url = reverse_lazy("catalogos:ce_list")


    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url="/login/")
@permission_required("catalogos.change_casoesp",login_url="/login/")
def CasoEsp_Inactivar(request,id):
    casoesp = CasoEsp.objects.filter(pk=id).first()

    if request.method=="POST":
        if casoesp:
            casoesp.estado = not casoesp.estado
            casoesp.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")

class PresentacionView(SinPrivilegios,  generic.ListView):
    permission_required = "catalogos.view_presentacion"
    model = Presentacion
    template_name = "catalogos/presentacion_list.html"
    context_object_name = "obj"


class PresentacionNew(SinPrivilegios, generic.CreateView):
    permission_required = "catalogos.add_presentacion"
    model = Presentacion
    template_name = "catalogos/presentacion_form.html"
    context_object_name = "obj"
    form_class = PresentacionForm
    success_url = reverse_lazy("catalogos:presentacion_list")


    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class PresentacionEdit(SinPrivilegios, generic.UpdateView):
    permission_required = "catalogos.change_presentacion"
    model = Presentacion
    template_name = "catalogos/presentacion_form.html"
    context_object_name = "obj"
    form_class = PresentacionForm
    success_url = reverse_lazy("catalogos:presentacion_list")

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


@login_required(login_url="/login/")
@permission_required("catalogos.change_presentacion",login_url="/login/")
def Presentacion_Inactivar(request,id):
    pres = Presentacion.objects.filter(pk=id).first()

    if request.method=="POST":
        if pres:
            pres.estado = not pres.estado
            pres.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")

class ProductoView(SinPrivilegios, generic.ListView):
    permission_required = "catalogos.view_product"
    model = Producto
    template_name = "catalogos/producto_list.html"
    context_object_name = "obj"


class IngredientView(IngredView):
    template_name="catalogos/Buscar_Ingred.html"
    
class CortView(CorteView):
    template_name="catalogos/Buscar_Corte.html"

class PresentaView(PresentacionView):
    template_name="catalogos/Buscar_Presenta.html"

class MarcView(MarcaView):
    template_name="catalogos/Buscar_Marca.html"

class CEView(CasoEspView):
    template_name="catalogos/Buscar_ce.html"


class ProductoNew(SinPrivilegios, generic.CreateView):
    permission_required = "catalogos.add_producto"
    model = Producto
    template_name = "catalogos/producto_form2.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("catalogos:producto_list")
    success_message="Producto Creado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ProductoEdit(SinPrivilegios, generic.UpdateView):
    permission_required = "catalogos.change_producto"
    model = Producto
    template_name = "catalogos/producto_form3.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("catalogos:producto_list")


    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


@login_required(login_url="/login/")
@permission_required("catalogos.change_producto",login_url="/login/")
def Producto_Inactivar(request,id):
    prod = Producto.objects.filter(pk=id).first()

    if request.method=="POST":
        if prod:
            prod.estado = not prod.estado
            prod.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")