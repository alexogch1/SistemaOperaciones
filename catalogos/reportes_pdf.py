import os
from django.conf import settings
from django.http import HttpResponse
from django.db.models import Subquery
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils import timezone

from .models import Ingred, Corte, Presentacion, Cliente, \
    Marca, CasoEsp, Producto

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path

def reporte_ingred_completo(request):
    today = timezone.now()
    template_path='catalogos/ingred_print_all.html'

    ingred= Ingred.objects.all()
    context={
        'obj': ingred,
        'today': today,
        'request':request
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content_Disposition']='inline' ; filename='Ingredientes.pdf'
    template = get_template(template_path)
    html = template.render(context)

     # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def reporte_corte_completo(request):
    today = timezone.now()
    template_path='catalogos/cortes_print_all.html'

    corte= Corte.objects.all()
    context={
        'obj': corte,
        'today': today,
        'request':request
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content_Disposition']='inline' ; filename='Cortes.pdf'
    template = get_template(template_path)
    html = template.render(context)

     # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def reporte_presenta_completo(request):
    today = timezone.now()
    template_path='catalogos/presenta_print_all.html'

    presenta= Presentacion.objects.all()
    context={
        'obj': presenta,
        'today': today,
        'request':request
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content_Disposition']='inline' ; filename='Presentaciones.pdf'
    template = get_template(template_path)
    html = template.render(context)

     # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def reporte_cliente_completo(request):
    today = timezone.now()
    template_path='catalogos/cliente_print_all.html'

    cliente= Cliente.objects.all()
    context={
        'obj': cliente,
        'today': today,
        'request':request
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content_Disposition']='inline' ; filename='Clientes.pdf'
    template = get_template(template_path)
    html = template.render(context)

     # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def reporte_marcas_completo(request):
    today = timezone.now()
    template_path='catalogos/marcas_print_all.html'


    marca= Marca.objects.all()
    
    context={
        'obj': marca,
        'today': today,
        'request':request
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content_Disposition']='inline' ; filename='Marcas.pdf'
    template = get_template(template_path)
    html = template.render(context)

     # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def reporte_ce_completo(request):
    today = timezone.now()
    template_path='catalogos/ce_print_all.html'


    ce= CasoEsp.objects.all()
    
    context={
        'obj': ce,
        'today': today,
        'request':request
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content_Disposition']='inline' ; filename='Casos Especiales.pdf'
    template = get_template(template_path)
    html = template.render(context)

     # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def reporte_productos_completo(request):
    today = timezone.now()
    template_path='catalogos/productos_print_all.html'


    producto= Producto.objects.all()
    
    context={
        'obj': producto,
        'today': today,
        'request':request
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content_Disposition']='inline' ; filename='Productos.pdf'
    template = get_template(template_path)
    html = template.render(context)

     # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response