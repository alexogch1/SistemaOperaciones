import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils import timezone

from .models import ProduccionEnc, ProduccionDet, \
    TiempoMuertoEnc, TiempoMuertoEnc, TiempoMuertonDet

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


def reporte_produccion(request):
    template_path = 'salidas/produccion_print_all.html'
    today = timezone.now()

    producciones = ProduccionEnc.objects.all()
    context = {
        'obj': producciones,
        'today': today,
        'request': request
        }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="listado_Produccion.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def imprimir_produccion_esp(request, produccion_id):
    template_path = 'salidas/produccion_print_one.html'
    today = timezone.now()
    
    enc = ProduccionEnc.objects.filter(id=produccion_id).first()
    #enc = ProduccionEnc.objects.all()
    if enc:
        detalle = ProduccionDet.objects.filter(produccion__id=produccion_id)
    else:
        detalle={}

    
    context = {
        'detalle': detalle,
        'encabezado':enc,
        'today':today,
        'request': request
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def reporte_tiempos_muertos(request):
    template_path = 'salidas/tiempos_muertos_print_all.html'
    today = timezone.now()

    tiempos_muertos = TiempoMuertoEnc.objects.all()
    context = {
        'obj': tiempos_muertos,
        'today': today,
        'request': request
        }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="listado_Produccion.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def imprimir_tiempos_muertos_esp(request, tiempo_muerto_id):
    template_path = 'salidas/tiempos_muertos_print_one.html'
    today = timezone.now()
    
    enc = TiempoMuertoEnc.objects.filter(id=tiempo_muerto_id).first()
    if enc:
        detalle = TiempoMuertonDet.objects.filter(tiempo_muerto_id=tiempo_muerto_id)
    else:
        detalle={}

    
    context = {
        'detalle': detalle,
        'encabezado':enc,
        'today':today,
        'request': request
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="reporte TM.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
