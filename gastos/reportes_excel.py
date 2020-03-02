from django.shortcuts import render

from django.views .generic.base import TemplateView
from django.http.response import HttpResponse
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border,Font,PatternFill,Side
from django.utils import timezone

from django.views import generic

#from dateutil.parser import parse

from .models import GastosSubCuenta, GastosSubCuenta


class CuentaGastosXls(TemplateView):
    pass