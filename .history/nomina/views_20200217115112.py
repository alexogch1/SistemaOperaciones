from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from generales.views import SinPrivilegios
from .form import NominaEncForm, NominaDetForm, DetalleNominaFormSet

from .models import NominaEnc, NominaDet

class NominaList(generic.ListView):
    model=NominaEnc
    template_name='nomina/nomina_list.html'
    context_object_name='nomina'

class NominaNew(SinPrivilegios ,generic.CreateView):
    permission_required='nomina.add_nominaenc'
    model=NominaEnc
    login_url='general:home'
    template_name='nomina/nomina_form.html'
    form_class=NominaEncForm
    success_url=reverse_lazy('nomina:nomina_list')

    def get(self, request, *args, **kwargs):
        self.object=None
        form_class=self.get_form_class()
        form=self.get_form(form_class)
        detalle_nomina_formset=DetalleNominaFormSet()
        return self.render_to_response(
            self.get_context_data(
                form=form,
                detalle_nomina = detalle_nomina_formset
            )
        )
    
    def post(self, request, *args, **kwargs):
        form_class=self.get_form_class()
        form=self.get_form(form_class)
        detalle_nomina=DetalleNominaFormSet(request.POST)

        if form.is_valid() and detalle_nomina.is_valid():
            return self.form_valid(form, detalle_nomina)
        else:
            return self.form_invalid(form, detalle_nomina)

    def form_valid(self, form, detalle_nomina):
        self.object=form.save()
        detalle_nomina.instance=self.object
        detalle_nomina.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, detalle_nomina):
        return self.render_to_response(
            self.get_context_data(
                form=form, 
                detalle_nomina=detalle_nomina
            )
        )

class NominaEdit(SinPrivilegios,generic.UpdateView):
    permission_required='nomina.change_nominaenc'
    model=NominaEnc
    login_url='general:home'
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

class NominaDel(SinPrivilegios,generic.DeleteView):
    permission_required='nomina:delete_nominaenc'
    model= NominaEnc
    template_name = 'nomina/nomina_del.html'
    context_object_name='obj'
    success_url=reverse_lazy('nomina:nomina_list')

    