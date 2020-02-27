from django.shortcuts import render,redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
import datetime
from datetime import datetime
from django.http import HttpResponse

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required

import json
from django.db.models import Sum

from .models import ProduccionEnc, ProduccionDet, TiempoMuertoEnc, TiempoMuertonDet, \
    ProduccionCongEnc, ProduccionCongDet, TiempoMuertoCongEnc, TiempoMuertoCongDet

from salidas.forms import ProduccionEncForm, TiempoMuertoEncForm,\
        ProduccionCongEncForm, TiempoMuertoCongEncForm

from generales.views import SinPrivilegios
from catalogos.models import Producto
from tmuertos.models import CausaTM

from dateutil.parser import parse

from plantas.models import Planta, Linea, Supervisor, Operador

class ProduccionView(SinPrivilegios, generic.ListView):
    model = ProduccionEnc
    template_name = "salidas/produccion_list.html"
    context_object_name = "obj"
    permission_required="salidas.view_produccionenc"


@login_required(login_url='/login/')
@permission_required('salidas.view_produccionenc', login_url='generales:sin_privilegios')
def produccion(request,produccion_id=None):
    template_name="salidas/produccion.html"
    prod=Producto.objects.filter(estado=True)
    form_produccion={}
    contexto={}

    if request.method=='GET':
        form_produccion=ProduccionEncForm()
        enc = ProduccionEnc.objects.filter(pk=produccion_id).first()

        if enc:
            det = ProduccionDet.objects.filter(produccion=enc)
            fecha_produccion = datetime.date.isoformat(enc.fecha_produccion)
            
            e = {
                'fecha_produccion':fecha_produccion,
                'ftm':enc.ftm,
                'fpr':enc.fpr,
                'planta':enc.planta,
                'linea':enc.linea,
                'turno':enc.turno,
                'supervisor':enc.supervisor,
                'operador':enc.operador,
                'plantilla':enc.plantilla,
                'observaciones': enc.observaciones,
                'total_produccion':enc.total_produccion,
                'total_utilizado':enc.total_utilizado,
                'total_merma':enc.total_merma
            }
            form_produccion = ProduccionEncForm(e)
        else:
            det=None
        
        contexto={'productos':prod,'encabezado':enc,'detalle':det,'form_enc':form_produccion}
        
    if request.method=='POST':
        fecha_produccion = request.POST.get("fecha_produccion")
        ftm = request.POST.get("ftm")
        fpr = request.POST.get("fpr")
        planta = request.POST.get("planta")
        linea = request.POST.get("linea")
        turno = request.POST.get("turno")
        supervisor = request.POST.get('supervisor')
        operador = request.POST.get('operador')
        plantilla = request.POST.get('plantilla')
        observaciones = request.POST.get("observaciones")
        plant=Planta.objects.get(pk=planta)
        line=Linea.objects.get(pk=linea)
        spvs=Supervisor.objects.get(pk=supervisor)
        opr=Operador.objects.get(pk=operador)
        

        if not produccion_id:
            enc = ProduccionEnc(
            fecha_produccion=fecha_produccion,
            fpr = fpr,
            planta=plant,
            linea=line,
            turno=turno,
            supervisor=spvs,
            operador=opr,
            plantilla=plantilla,
            observaciones=observaciones,
            uc = request.user 
            )

            if enc:
                enc.save()
                produccion_id=enc.id
        else:
            enc=ProduccionEnc.objects.filter(pk=produccion_id).first()
            if enc:
                enc.fecha_produccion = fecha_produccion
                enc.ftm =ftm
                enc.fpr =fpr
                enc.observaciones = observaciones 
                enc.planta = plant
                enc.linea = line
                enc.turno = turno
                enc.supervisor=spvs
                enc.operador=opr
                enc.platilla=plant
                enc.um=request.user.id
                enc.save()

        if not produccion_id:
            return redirect("salidas:produccion_list")

        producto = request.POST.get("id_id_producto")
        tproducto = request.POST.get("id_tproducto")
        
        cantidad = request.POST.get("id_cantidad_detalle")
        resto = request.POST.get("id_resto_detalle")
        velocidad = request.POST.get("id_velocidad_detalle")
        peso = request.POST.get("id_peso_detalle")
        total  = request.POST.get("id_total_detalle")
        total_util  = request.POST.get("id_total_utilizado")
        total_merm  = request.POST.get("id_merma_detalle")

        prod = Producto.objects.get(pk=producto)

        det     = ProduccionDet(
            produccion=enc,
            producto=prod,
            tproducto=tproducto,
            cantidad=cantidad,
            resto=resto,
            velocidad=velocidad,
            total_produccion = total,
            total_utilizado = total_util,
            total_merma = total_merm,
            peso=peso,
            uc = request.user
        )

        if det:
            det.save()
            total=ProduccionDet.objects.filter(produccion=produccion_id).aggregate(Sum('total_produccion'))
            enc.total_produccion = total["total_produccion__sum"]            

            total_util=ProduccionDet.objects.filter(produccion=produccion_id).aggregate(Sum('total_utilizado'))
            enc.total_utilizado = total_util["total_utilizado__sum"]            

            #total_merm=ProduccionDet.objects.filter(produccion=produccion_id).aggregate(Sum('total_merma'))
            #enc.total_merma = total_merm["total_merma__sum"]            
            
            enc.total_merma=100-((enc.total_produccion/enc.total_utilizado)*100)
            enc.save()

        return redirect("salidas:produccion_edit",produccion_id=produccion_id)

    return render(request, template_name, contexto)

class ProduccionDetDelete(SinPrivilegios, generic.DeleteView):
    permission_required = "salidas.delete_producciondet"
    model = ProduccionDet
    template_name = "salidas/produccion_det_del.html"
    context_object_name = 'obj'
    
    def get_success_url(self):
          produccion_id=self.kwargs['produccion_id']
          return reverse_lazy('salidas:produccion_edit', kwargs={'produccion_id': produccion_id})


class TiempoMuertoView(SinPrivilegios, generic.ListView):
    model = TiempoMuertoEnc
    template_name = "salidas/tiempos_muertos_list.html"
    context_object_name = "obj"
    permission_required="salidas.view_tmuertosenc"

    def get_context_data(self, **kwargs):
        context = super(TiempoMuertoView, self).get_context_data(**kwargs)
        initial_date='2020-01-01'
        initial_date= datetime.now()
        if not initial_date or not final_date:

            
    
        
            #initial_date = self.request.GET.get('fecha_inicial')
            #final_date = self.request.GET.get('fecha_final')
            
            context      = TiempoMuertoEnc.objects.order_by('-fecha_produccion')[1]    
        initial_date = parse(initial_date)
        final_date = parse(final_date)    
        context['detalles'] = TiempoMuertoEnc.objects.filter(fecha_produccion__gte=initial_date, fecha_produccion__lte=final_date )
        return context
        



class TiempoMuertoCompletoList(generic.ListView):
        
    template_name='salidas/tiempos_muertos_completos.html'
    context_object_name='obj'
    queryset = TiempoMuertoEnc.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TiempoMuertoCompletoList, self).get_context_data(**kwargs)
        context['detalles'] = TiempoMuertonDet.objects.all()
        context['encabezado'] = self.queryset
        return context


@login_required(login_url='/login/')
@permission_required('salidas.view_tmuertosenc', login_url='generales:sin_privilegios')
def tiempos_muertos(request,tiempo_muerto_id=None):
    template_name="salidas/tiempos_muertos.html"
    causa=CausaTM.objects.filter(estado=True)
    form_tmuertos={}
    contexto={}

    if request.method=='GET':
        form_tmuertos=TiempoMuertoEncForm()
        enc = TiempoMuertoEnc.objects.filter(pk=tiempo_muerto_id).first()

        if enc:
            det = TiempoMuertonDet.objects.filter(tiempo_muerto=enc)
            fecha_produccion = datetime.date.isoformat(enc.fecha_produccion)
            
            
            e = {
                'fecha_produccion':fecha_produccion,
                'planta':enc.planta,
                'linea':enc.linea,
                'turno':enc.turno,
                
                
                'supervisor':enc.supervisor,
            
                'observaciones': enc.observaciones,
                'cantidad':enc.cantidad,
                'total_tm':enc.total_tm,
                
            }
            form_tmuertos = TiempoMuertoEncForm(e)
        else:
            det=None
        
        contexto={'causas':causa,'encabezado':enc,'detalle':det,'form_enc':form_tmuertos}
        
    if request.method=='POST':
        fecha_produccion = request.POST.get("fecha_produccion")
        planta = request.POST.get("planta")
        linea = request.POST.get("linea")
        turno = request.POST.get("turno")
        supervisor = request.POST.get('supervisor')
        
        observaciones = request.POST.get("observaciones")
        total = 0
        
        plant=Planta.objects.get(pk=planta)
        line=Linea.objects.get(pk=linea)
        spvs=Supervisor.objects.get(pk=supervisor)
        

        if not tiempo_muerto_id:

            enc = TiempoMuertoEnc(
            fecha_produccion=fecha_produccion,
            planta=plant,
            linea=line,
            turno=turno,
            supervisor=spvs,
            
            observaciones=observaciones,
            uc = request.user 
            )
            if enc:
                enc.save()
                tiempo_muerto_id=enc.id
        else:
            enc=TiempoMuertoEnc.objects.filter(pk=tiempo_muerto_id).first()
            if enc:
                enc.fecha_produccion = fecha_produccion
                enc.observaciones = observaciones 
                enc.planta = plant
                enc.linea = line
                enc.turno = turno
                enc.supervisor=spvs
                enc.um=request.user.id
                enc.save()

        if not tiempo_muerto_id:
            return redirect("salidas:tiempos_muertos_list")

        causa = request.POST.get("id_id_tmuerto")
        obs = request.POST.get("id_obs_detalle")
        cantidad = request.POST.get("id_cantidad_detalle")
        total  = request.POST.get("id_total_detalle")
        

        cau = CausaTM.objects.get(pk=causa)

        det     = TiempoMuertonDet(
            tiempo_muerto=enc,
            causa=cau,
            obs=obs,
            cantidad=cantidad,
            total_tm=total,
            uc=request.user
        )

        if det:
            det.save()
            total=TiempoMuertonDet.objects.filter(tiempo_muerto=tiempo_muerto_id).aggregate(Sum('total_tm'))
            enc.total_tm = total["total_tm__sum"]            

            enc.save()

        return redirect("salidas:tiempos_muertos_edit",tiempo_muerto_id=tiempo_muerto_id)

    return render(request, template_name, contexto)

class TiempoMuertoDetDelete(SinPrivilegios, generic.DeleteView):
    permission_required = "salidas.delete_tmuertodet"
    model = TiempoMuertonDet
    template_name = "salidas/tiempos_muertos_det_del.html"
    context_object_name = 'obj'
    
    def get_success_url(self):
          tiempo_muerto_id=self.kwargs['tiempo_muerto_id']
          return reverse_lazy('salidas:tiempos_muertos_edit', kwargs={'tiempo_muerto_id': tiempo_muerto_id})


def tiempos_muertos_resumen(request):
    from django.db import connection
    from django.db.models import Q
    from django.db.models import Subquery, OuterRef

    
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT id,fecha_produccion,observaciones,total_tm FROM salidas_tiempomuertoenc")
        rawData = cursor.fetchall()
        
        result = []
        for r in rawData:
            result.append(list(r))
        contexto = {'consultas': result }
    return render(request, 'salidas/tiempos_muertos_resumen.html', contexto )

@login_required(login_url="/login/")
@permission_required("salidas.change_produccionenc",login_url="/login/")
def produccion_inactivar(request,id):
    produccion = ProduccionEnc.objects.filter(pk=id).first()

    if request.method=="POST":
        if produccion:
            print('estado de la Producción', produccion.estado)

            
            produccion.estado = not produccion.estado
            produccion.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")

@login_required(login_url="/login/")
@permission_required("plantas.change_tiempomuertoenc",login_url="/login/")
def tiempo_muerto_inactivar(request,id):
    tm = TiempoMuertoEnc.objects.filter(pk=id).first()

    if request.method=="POST":
        if tm:
            print('estado del Tiempo Muerto', tm.estado)

            
            tm.estado = not tm.estado
            tm.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")

# Inician las vistas para Produccion Congelado

class ProduccionCongView(SinPrivilegios, generic.ListView):
    model = ProduccionCongEnc
    template_name = "salidas/produccion_cong_list.html"
    context_object_name = "obj"
    permission_required="salidas.view_produccioncongenc"


@login_required(login_url='/login/')
@permission_required('salidas.view_produccioncongenc', login_url='generales:sin_privilegios')
def produccion_cong(request,produccion_cong_id=None):
    template_name="salidas/produccion_cong.html"
    prod=Producto.objects.filter(estado=True)
    form_produccion_cong={}
    contexto={}

    if request.method=='GET':
        form_produccion_cong=ProduccionCongEncForm()
        enc = ProduccionCongEnc.objects.filter(pk=produccion_cong_id).first()

        if enc:
            det = ProduccionCongDet.objects.filter(produccion=enc)
            fecha_produccion = datetime.date.isoformat(enc.fecha_produccion)
            
            
            e = {
                'fecha_produccion':fecha_produccion,
                'planta':enc.planta,
                'linea':enc.linea,
                #'turno':enc.turno,
                'shift':enc.shift,
                'horas_turno':enc.horas_turno,
                'plantilla':enc.plantilla,
                'supervisor':enc.supervisor,
                'observaciones': enc.observaciones,
                'total_produccion':enc.total_produccion,
                'total_utilizado':enc.total_utilizado,
                'total_merma':enc.total_merma
            }
            form_produccion_cong = ProduccionCongEncForm(e)
        else:
            det=None
        
        contexto={'productos':prod,'encabezado':enc,'detalle':det,'form_enc':form_produccion_cong}
        
    if request.method=='POST':
        fecha_produccion = request.POST.get("fecha_produccion")


        planta = request.POST.get("planta")
        linea = request.POST.get("linea")
        #turno = request.POST.get("turno")
        shift = request.POST.get('shift')
        horas_turno = request.POST.get('horas_turno')
        plantilla = request.POST.get('plantilla')
        supervisor = request.POST.get('supervisor')
        observaciones = request.POST.get("observaciones")
        plant=Planta.objects.get(pk=planta)
        line=Linea.objects.get(pk=linea)
        spvs=Supervisor.objects.get(pk=supervisor)

        if not produccion_cong_id:

            enc = ProduccionCongEnc(
            fecha_produccion=fecha_produccion,
            planta=plant,
            linea=line,
            shift=shift,
            horas_turno=horas_turno,
            plantilla=plantilla,
            supervisor=spvs,
            observaciones=observaciones,
            uc = request.user 
            )

            if enc:
                enc.save()
                produccion_cong_id=enc.id
        else:
            enc=ProduccionCongEnc.objects.filter(pk=produccion_cong_id).first()
            if enc:
                enc.fecha_produccion = fecha_produccion
                enc.observaciones = observaciones 
                enc.planta = plant
                enc.linea = line
                #enc.turno = turno
                enc.shift = shift
                enc.horas_turno = horas_turno
                enc.plantilla = plantilla
                enc.supervisor=spvs
                enc.um=request.user.id
                enc.save()

        if not produccion_cong_id:
            return redirect("salidas:produccion_cong_list")

        producto = request.POST.get("id_id_producto")
        tproducto = request.POST.get("id_tproducto")
        cantidad = request.POST.get("id_cantidad_detalle")
        resto = request.POST.get("id_resto_detalle")
        peso = request.POST.get("id_peso_detalle")
        total  = request.POST.get("id_total_detalle")
        total_util  = request.POST.get("id_total_utilizado")
        resto  = request.POST.get("id_resto_detalle")
        total_merma  = request.POST.get("id_merma_detalle")
        r1 = request.POST.get("id_r1_detalle")
        r2 = request.POST.get('id_r2_detalle')
        r3 = request.POST.get('id_r3_detalle')
        r4 = request.POST.get('id_r4_detalle')
        r5 = request.POST.get('id_r5_detalle')

        prod = Producto.objects.get(pk=producto)

        det     = ProduccionCongDet(
            produccion=enc,
            producto=prod,
            tproducto=tproducto,
            cantidad=cantidad,
            resto=resto,
            total_produccion=total,
            total_utilizado=total_util,
            total_merma = total_merma,
            r1=r1,
            r2=r2,
            r3=r3,
            r4=r4,
            r5=r5,
            peso=peso,
            uc = request.user
        )

        if det:
            det.save()
            total=ProduccionCongDet.objects.filter(produccion=produccion_cong_id).aggregate(Sum('total_produccion'))
            enc.total_produccion = total["total_produccion__sum"]  
                      
            total_util=ProduccionCongDet.objects.filter(produccion=produccion_cong_id).aggregate(Sum('total_utilizado'))
            enc.total_utilizado = total_util["total_utilizado__sum"]            
       

            enc.total_merma=100-((enc.total_produccion/enc.total_utilizado)*100)
            enc.save()

        return redirect("salidas:produccion_cong_edit",produccion_cong_id=produccion_cong_id)

    return render(request, template_name, contexto)

class ProduccionCongDetDelete(SinPrivilegios, generic.DeleteView):
    permission_required = "salidas.delete_produccioncongdet"
    model = ProduccionCongDet
    template_name = "salidas/produccion_cong_det_del.html"
    context_object_name = 'obj'
    
    def get_success_url(self):
          produccion_cong_id=self.kwargs['produccion_cong_id']
          return reverse_lazy('salidas:produccion_cong_edit', kwargs={'produccion_cong_id': produccion_cong_id})


class TiempoMuertoCongView(SinPrivilegios, generic.ListView):
    model = TiempoMuertoCongEnc
    template_name = "salidas/tiempos_muertos_cong_list.html"
    context_object_name = "obj"
    permission_required="salidas.view_tmuertoscongenc"


@login_required(login_url='/login/')
@permission_required('salidas.view_tmuertoscongenc', login_url='generales:sin_privilegios')
def tiempos_muertos_cong(request,tiempo_muerto_cong_id=None):
    template_name="salidas/tiempos_muertos_cong.html"
    causa=CausaTM.objects.filter(estado=True)
    form_tmuertos_cong={}
    contexto={}

    if request.method=='GET':
        form_tmuertos_cong=TiempoMuertoCongEncForm()
        enc = TiempoMuertoCongEnc.objects.filter(pk=tiempo_muerto_cong_id).first()

        if enc:
            det = TiempoMuertoCongDet.objects.filter(tiempo_muerto=enc)
            fecha_produccion = datetime.date.isoformat(enc.fecha_produccion)
            
            e = {
                'fecha_produccion':fecha_produccion,
                'planta':enc.planta,
                'linea':enc.linea,
                'turno':enc.turno,
                'supervisor':enc.supervisor,
                'observaciones': enc.observaciones,
                'cantidad':enc.cantidad,
                'total_tm':enc.total_tm,
                
            }
            form_tmuertos_cong = TiempoMuertoCongEncForm(e)
        else:
            det=None
        
        contexto={'causas':causa,'encabezado':enc,'detalle':det,'form_enc':form_tmuertos_cong}
        
    if request.method=='POST':
        fecha_produccion = request.POST.get("fecha_produccion")
        planta = request.POST.get("planta")
        linea = request.POST.get("linea")
        turno = request.POST.get("turno")
        supervisor = request.POST.get('supervisor')
        observaciones = request.POST.get("observaciones")
        total = 0
        
        plant=Planta.objects.get(pk=planta)
        line=Linea.objects.get(pk=linea)
        spvs=Supervisor.objects.get(pk=supervisor)
        
        if not tiempo_muerto_cong_id:

            enc = TiempoMuertoCongEnc(
            fecha_produccion=fecha_produccion,
            planta=plant,
            linea=line,
            turno=turno,
            supervisor=spvs,
            observaciones=observaciones,
            uc = request.user 
            )
            if enc:
                enc.save()
                tiempo_muerto_cong_id=enc.id
        else:
            enc=TiempoMuertoCongEnc.objects.filter(pk=tiempo_muerto_cong_id).first()
            if enc:
                enc.fecha_produccion = fecha_produccion
                enc.observaciones = observaciones 
                enc.planta = plant
                enc.linea = line
                enc.turno = turno
                enc.supervisor=spvs
                enc.um=request.user.id
                enc.save()

        if not tiempo_muerto_cong_id:
            return redirect("salidas:tiempos_muertos_cong_list")

        causa = request.POST.get("id_id_tmuerto")
        cantidad = request.POST.get("id_cantidad_detalle")
        obs = request.POST.get('id_obs_detalle')
        total  = request.POST.get("id_total_detalle")
        
        cau = CausaTM.objects.get(pk=causa)


        det     = TiempoMuertoCongDet(
            tiempo_muerto=enc,
            causa=cau,
            obs=obs,
            cantidad=cantidad,
            total_tm=total,
            uc=request.user
        )

        if det:
            det.save()
            total=TiempoMuertoCongDet.objects.filter(tiempo_muerto=tiempo_muerto_cong_id).aggregate(Sum('total_tm'))
            enc.total_tm = total["total_tm__sum"]            

            enc.save()

        return redirect("salidas:tiempos_muertos_cong_edit",tiempo_muerto_cong_id=tiempo_muerto_cong_id)

    return render(request, template_name, contexto)

class TiempoMuertoCongDetDelete(SinPrivilegios, generic.DeleteView):
    permission_required = "salidas.delete_tmuertocongdet"
    model = TiempoMuertoCongDet
    template_name = "salidas/tiempos_muertos_cong_det_del.html"
    context_object_name = 'obj'
    
    def get_success_url(self):
          tiempo_muerto_cong_id=self.kwargs['tiempo_muerto_cong_id']
          return reverse_lazy('salidas:tiempos_muertos_cong_edit', kwargs={'tiempo_muerto_cong_id': tiempo_muerto_cong_id})


def tiempos_muertos_cong_resumen(request):
    from django.db import connection
    from django.db.models import Q
    from django.db.models import Subquery, OuterRef
    with connection.cursor() as cursor:
        cursor.execute("SELECT id,fecha_produccion,observaciones,total_tm FROM salidas_tiempomuertocongenc")
        rawData = cursor.fetchall()
        
        result = []
        for r in rawData:
            result.append(list(r))
        contexto = {'consultas': result }
    return render(request, 'salidas/tiempos_muertos_cong_resumen.html', contexto )

@login_required(login_url="/login/")
@permission_required("salidas.change_produccioncongenc",login_url="/login/")
def produccion_cong_inactivar(request,id):
    produccion_cong = ProduccionCongEnc.objects.filter(pk=id).first()

    if request.method=="POST":
        if produccion_cong:
            print('estado de la Producción', produccion_cong.estado)

            
            produccion_cong.estado = not produccion_cong.estado
            produccion_cong.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")

@login_required(login_url="/login/")
@permission_required("plantas.change_tiempomuertocongenc",login_url="/login/")
def tiempo_muerto_cong_inactivar(request,id):
    tm_cong = TiempoMuertoCongEnc.objects.filter(pk=id).first()

    if request.method=="POST":
        if tm_cong:
            print('estado del Tiempo Muerto', tm_cong.estado)

            
            tm_cong.estado = not tm_cong.estado
            tm_cong.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    
    return HttpResponse("FAIL")

