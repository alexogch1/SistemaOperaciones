from django.shortcuts import render

from django.views .generic.base import TemplateView
from django.http.response import HttpResponse
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border,Font,PatternFill,Side
from django.utils import timezone

from django.views import generic


from .models import TiempoMuertoEnc, TiempoMuertonDet

class TiempoMuertoCompletoXls(generic.TemplateView):
    
    queryset = TiempoMuertoEnc.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TiempoMuertoCompletoXls, self).get_context_data(**kwargs)
        context['detalles'] = TiempoMuertonDet.objects.all()
        context['encabezado'] = self.queryset
        return context

    print('salidas/tiempo_muerto_completo_excel',context_object_name)

    def get (self, request, *args, **kwargs):
        pass


