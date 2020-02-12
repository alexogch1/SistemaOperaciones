from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Categoria, SubCategoria, Origen
from .forms import CategoriaForm, SubCategoriaForm, OrigenForm


class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = "generales:login"

class CategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    login_url = "generales:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    login_url = "generales:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = "inv/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:categoria_list")

class SubCategoriaView(LoginRequiredMixin, generic.ListView):
    model = SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"
    login_url = "generales:login"

class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url = "generales:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url = "generales:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class SubCategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = SubCategoria
    template_name = "inv/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:subcategoria_list")

def SubCategoria_Inactivar(request, id):
    subcategoria =  SubCategoria.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not subcategoria:
        return redirect ("inv:subcategoria_list")
    
    if request.method=='GET':
        contexto ={'obj':subcategoria}

    if request.method == 'POST':
        subcategoria.estado = False 
        subcategoria.save()
        return redirect("inv:subcategoria_list")

    return render (request, template_name, contexto)

class OrigenView(LoginRequiredMixin, generic.ListView):
    model = Origen
    template_name = "inv/origen_list.html"
    context_object_name = "obj"
    login_url = "generales:login"

class OrigenNew(LoginRequiredMixin, generic.CreateView):
    model = Origen
    template_name = "inv/origen_form.html"
    context_object_name = "obj"
    form_class = OrigenForm
    success_url = reverse_lazy("inv:origen_list")
    login_url = "generales:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class OrigenEdit(LoginRequiredMixin, generic.UpdateView):
    model = Origen
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = OrigenForm
    success_url = reverse_lazy("inv:origen_list")
    login_url = "generales:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def Origen_Inactivar(request, id):
    origen =  Origen.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not origen:
        return redirect ("inv:origen_list")
    
    if request.method=='GET':
        contexto ={'obj':origen}

    if request.method == 'POST':
        origen.estado = False 
        origen.save()
        return redirect("inv:origen_list")

    return render (request, template_name, contexto)