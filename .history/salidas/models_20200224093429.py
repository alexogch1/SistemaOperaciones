from django.db import models
from django.conf import settings

from decimal import Decimal

#Para los signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

from generales.models import ClaseModelo, ClaseModelo2
from catalogos.models import Producto
from tmuertos.models import CausaTM
from plantas.models import Planta, Linea, Supervisor, Operador

class OwnerModel (ClaseModelo):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class ProduccionEnc(ClaseModelo):
    T1='1ER. TURNO'
    T2='2DO. TURNO'
    T3='3ER. TURNO'
    TM='MIXTO'
    SI = 'SI'
    NO = 'NO'
    
    TURNO = [
        (T1,'1ER. TURNO'),
        (T2,'2DO. TURNO'),
        (T3,'3ER. TURNO'),
        (TM,'MIXTO')]
    RESPUESTA = [
        (SI,'SI'),
        (NO,'NO')]

    fecha_produccion = models.DateField()
    ftm =models.CharField(
        max_length=2,
        choices=RESPUESTA,
        default=SI
    )

    fpr =models.CharField(
        max_length=2,
        choices=RESPUESTA,
        default=SI
    )

    observaciones = models.CharField(max_length=200, null=True,blank=True)
    total_produccion = models.FloatField(default=0)
    total_utilizado = models.FloatField(default=0)
    total_merma = models.FloatField(default=0)
    peso =models.IntegerField(default=0)
    cantidad =models.IntegerField(default=0)

    planta=models.ForeignKey(Planta, on_delete=models.CASCADE)
    linea=models.ForeignKey(Linea, on_delete=models.CASCADE)
    supervisor=models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    operador=models.ForeignKey(Operador, on_delete=models.CASCADE)
    plantilla = models.IntegerField(default=0)

    turno=models.CharField(
        max_length=20,
        choices=TURNO,
        default=T1
    )

    def __str__(self):
        return'{}'.format(self.observaciones)
    
    def save(self):
        self.observaciones = self.observaciones.upper()
        
        self.total_produccion = float(self.total_produccion)
        self.total_utilizado = float(self.total_utilizado)
        self.total_merma = float(self.total_merma)
        #self.plantilla = int(self.plantilla)

        #self.total_merma = 100-((float(self.total_produccion)/  float(self.total_utilizado)*100)
        
        super(ProduccionEnc, self).save()

    class Meta:
        verbose_name_plural ="Encabezados Producciones"
        verbose_name = "Encabezado Produccion"

class ProduccionDet(ClaseModelo):
    PROCESO = 'PROCESO'
    TERMINADO = 'TERMINADO'
    TIPOPROD = [
        (PROCESO,'PROCESO'),
        (TERMINADO,'TERMINADO')]
        

    produccion = models.ForeignKey(ProduccionEnc, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tproducto =models.CharField(
        max_length=20,
        choices=TIPOPROD,
        default=TERMINADO,
        )
    peso =models.IntegerField(default=0)
    cantidad =models.IntegerField(default=0)
    resto =models.FloatField(default=0)
    velocidad =models.IntegerField(default=0)
    total_produccion = models.FloatField(default=0)
    total_utilizado = models.FloatField(default=0)
    total_merma = models.FloatField(default=0)

    def __str__(self):
        return "{}".format(self.producto)
    
    def save(self):
        self.total_produccion = float((float(int(self.cantidad))* float(self.peso)+ float(int(self.resto))))
        self.total_utilizado = float(self.total_utilizado)
        self.total_merma = 100-((float(self.total_produccion) / float(self.total_utilizado))*100)
        super(ProduccionDet, self).save()

    class Meta:
        verbose_name_plural ="Detalles Producciones"
        verbose_name = "Detalle Produccion"

@receiver (post_delete, sender=ProduccionDet)
def detalle_produccion_borrar(sender, instance, **kwargs):
    #id_producto = instance.producto.id
    id_produccion = instance.produccion.id

    enc = ProduccionEnc.objects.filter(pk=id_produccion).first()
    if enc:
        total=ProduccionDet.objects.filter(produccion=id_produccion).aggregate(Sum('total_produccion'))
        enc.total_produccion = total["total_produccion__sum"]            

        total_util=ProduccionDet.objects.filter(produccion=id_produccion).aggregate(Sum('total_utilizado'))
        enc.total_utilizado = total_util["total_utilizado__sum"]            

        """ total_merm=ProduccionDet.objects.filter(produccion=id_produccion).aggregate(Sum('total_merma'))
        enc.total_merma = total_merm["total_merma__sum"]    """         

        total_merma = 100-((enc.total_produccion / enc.total_utilizado)*100)
        enc.total_merma = total_merma 

        enc.save()

@receiver(post_save, sender=ProduccionDet)
def detalle_produccion_guardar(sender, instance,**kwargs):
    id_producto = instance.producto.id
    
    fecha_produccion = instance.produccion.fecha_produccion

    prod = Producto.objects.filter(pk=id_producto).first()
    #en esta parte se puede actualizar el inventario
    prod.ultima_produccion = fecha_produccion
    
    prod.save()

class TiempoMuertoEnc(ClaseModelo):
    T1='1ER. TURNO'
    T2='2DO. TURNO'
    T3='3ER. TURNO'
    TM='MIXTO'
    TURNO = [
        (T1,'1ER. TURNO'),
        (T2,'2DO. TURNO'),
        (T3,'3ER. TURNO'),
        (TM,'MIXTO')]

    fecha_produccion = models.DateField()
    observaciones = models.CharField(max_length=200, null=True,blank=True)
    total_tm = models.FloatField(default=0)
    cantidad =models.IntegerField(default=0)

    planta=models.ForeignKey(Planta, on_delete=models.CASCADE)
    linea=models.ForeignKey(Linea, on_delete=models.CASCADE)
    supervisor=models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    

    turno=models.CharField(
        max_length=20,
        choices=TURNO,
        default=T1
    )
    def __str__(self):
        return'{}'.format(self.observaciones)
    
    def save(self):
        self.observaciones = self.observaciones.upper()
        self.total_tm = float(self.total_tm)
        super(TiempoMuertoEnc, self).save()

    class Meta:
        verbose_name_plural ="Encabezados Tiempos Muertos"
        verbose_name = "Encabezado Tiempo Muerto"

class TiempoMuertonDet(ClaseModelo):
    tiempo_muerto = models.ForeignKey(TiempoMuertoEnc, related_name='detalles' on_delete=models.CASCADE)
    causa = models.ForeignKey(CausaTM, on_delete=models.CASCADE)
    obs = models.CharField(max_length=100, null=True, )
    cantidad =models.IntegerField(default=0)
    total_tm = models.FloatField(default=0)
    

    def __str__(self):
        return "{}".format(self.causa)
    
    def save(self):
        self.total_tm = float(self.cantidad)
        #self.obs = self.obs.upper()
        
        super(TiempoMuertonDet, self).save()

    class Meta:
        verbose_name_plural ="Detalles Tiempos Muertos"
        verbose_name = "Detalle Tiempo Muerto"


        # Comienza los Modelos para las tablas de IQF y WP

class ProduccionCongEnc(ClaseModelo):
    TURNO_1 = "TURNO 1"
    TURNO_2 = "TURNO 2"
    TURNO_3 = "TURNO 3"
    TURNO_M= "TURNO MIXTO"
    TURNO_APOYO= "TURNO APOYO"
    SI = "SI"
    NO = "NO"
    TURNO_CHOICES = (
        (TURNO_1, 'TURNO 1'),
        (TURNO_2, 'TURNO 2'),
        (TURNO_3, 'TURNO 3'),
        (TURNO_M, 'TURNO MIXTO'),
        (TURNO_APOYO, 'TURNO APOYO'),
    )

    RESPUESTA = [
        (SI,'SI'),
        (NO,'NO')]
        
    fecha_produccion = models.DateField()
    observaciones = models.CharField(max_length=200, null=True,blank=True)
    total_produccion = models.FloatField(default=0)
    total_utilizado = models.FloatField(default=0)
    total_merma = models.FloatField(default=0)
    peso =models.IntegerField(default=0)
    cantidad =models.IntegerField(default=0)
        
    planta=models.ForeignKey(Planta, on_delete=models.CASCADE)
    linea=models.ForeignKey(Linea, on_delete=models.CASCADE)
    supervisor=models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    plantilla=models.IntegerField(default=0)
            
        
    

    shift=models.CharField(choices=TURNO_CHOICES, max_length=30)
    horas_turno= models.FloatField(default=8)
        
    def __str__(self):
        return'{}'.format(self.observaciones)
            
    def save(self):
        self.observaciones = self.observaciones.upper()
        self.total_produccion = float(self.total_produccion)
        self.total_utilizado = float(self.total_utilizado)
        self.total_merma = float(self.total_merma)
  
        super(ProduccionCongEnc, self).save()
        
    class Meta:
        verbose_name_plural ="Encabezados Producciones Cong"
        verbose_name = "Encabezado Produccion cong"
        
class ProduccionCongDet(ClaseModelo):
    PROCESO = 'PROCESO'
    TERMINADO = 'TERMINADO'
    TIPOPROD = (
    (PROCESO,'PROCESO'),
    (TERMINADO,'TERMINADO'))
                
        
    produccion = models.ForeignKey(ProduccionCongEnc, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tproducto =models.CharField(
        max_length=20,
        choices=TIPOPROD,
        default=PROCESO,
    )
    
    peso =models.IntegerField(default=0)
    cantidad =models.IntegerField(default=0)
    resto =models.FloatField(default=0)
            
    total_produccion = models.FloatField(default=0)
    total_utilizado = models.FloatField(default=0)
    total_merma = models.FloatField(default=0)
    r1=models.IntegerField(default=0)
    r2=models.IntegerField(default=0)
    r3=models.IntegerField(default=0)
    r4=models.IntegerField(default=0)
    r5=models.IntegerField(default=0)
        
    def __str__(self):
        return "{}".format(self.producto)
            
    def save(self):
        self.total_produccion = float((float(int(self.cantidad))* float(self.peso)+ float(int(self.resto))))
        self.total_utilizado = float(self.total_utilizado)
        self.total_merma = 100-((float(self.total_produccion) / float(self.total_utilizado))*100)
        self.r1 = int(self.r1)
        self.r2 = int(self.r2)
        self.r3 = int(self.r3)
        self.r4 = int(self.r4)
        self.r5 = int(self.r5)
        super(ProduccionCongDet, self).save()
        
    class Meta:
        verbose_name_plural ="Detalles Producciones Cong"
        verbose_name = "Detalle Produccion Cong"
        
@receiver (post_delete, sender=ProduccionCongDet)
def detalle_produccion_cong_borrar(sender, instance, **kwargs):
            
    id_produccion = instance.produccion.id
        
    enc = ProduccionCongEnc.objects.filter(pk=id_produccion).first()
    if enc:
        total=ProduccionCongDet.objects.filter(produccion=id_produccion).aggregate(Sum('total_produccion'))
        enc.total_produccion = total["total_produccion__sum"]            
        
        total_util=ProduccionCongDet.objects.filter(produccion=id_produccion).aggregate(Sum('total_utilizado'))
        enc.total_utilizado = total_util["total_utilizado__sum"]            
        
        total_merma = 100-((enc.total_produccion / enc.total_utilizado)*100)
        enc.total_merma = total_merma 
        
        enc.save()
        
    @receiver(post_save, sender=ProduccionCongDet)
    def detalle_produccion_cong_guardar(sender, instance,**kwargs):
        id_producto = instance.producto.id
            
        #fecha_produccion = instance.produccion.fecha_produccion
        fecha_produciion = instance.produccion_cong.fecha_produccion
        
        prod = Producto.objects.filter(pk=id_producto).first()
        #en esta parte se puede actualizar el inventario
        prod.ultima_produccion = fecha_produccion
            
        prod.save()
        
class TiempoMuertoCongEnc(ClaseModelo):
    TURNO_1 = "TURNO 1"
    TURNO_2 = "TURNO 2"
    TURNO_3 = "TURNO 3"
    TURNO_M= "TURNO MIXTO"
    TURNO_APOYO= "TURNO APOYO"

    TURNO_CHOICES = (
        (TURNO_1, 'TURNO 1'),
        (TURNO_2, 'TURNO 2'),
        (TURNO_3, 'TURNO 3'),
        (TURNO_M, 'TURNO MIXTO'),
        (TURNO_APOYO, 'TURNO APOYO'),
    )
        
    fecha_produccion = models.DateField()
    observaciones = models.CharField(max_length=200, null=True,blank=True)
    total_tm = models.FloatField(default=0)
    cantidad =models.IntegerField(default=0)
        
    planta=models.ForeignKey(Planta, on_delete=models.CASCADE)
    linea=models.ForeignKey(Linea, on_delete=models.CASCADE)
    supervisor=models.ForeignKey(Supervisor, on_delete=models.CASCADE)
            
    turno=models.CharField(
        max_length=20,
        choices=TURNO_CHOICES,
        default=TURNO_1
    )
    def __str__(self):
        return'{}'.format(self.observaciones)
            
    def save(self):
        self.observaciones = self.observaciones.upper()
        self.total_tm = float(self.total_tm)
        super(TiempoMuertoCongEnc, self).save()
        
    class Meta:
        verbose_name_plural ="Encabezados Tiempos Muertos Cong"
        verbose_name = "Encabezado Tiempo Muerto Cong"
        
class TiempoMuertoCongDet(ClaseModelo):
    tiempo_muerto = models.ForeignKey(TiempoMuertoCongEnc, on_delete=models.CASCADE)
    causa = models.ForeignKey(CausaTM, on_delete=models.CASCADE)
    cantidad =models.IntegerField(default=0)
    obs = models.CharField(max_length=100, null=True, )
    total_tm = models.FloatField(default=0)
            
        
    def __str__(self):
        return "{}".format(self.causa)
            
    def save(self):
        self.total_tm = float(self.cantidad)
                
        super(TiempoMuertoCongDet, self).save()
        
    class Meta:
        verbose_name_plural ="Detalles Tiempos Muertos Cong"
        verbose_name = "Detalle Tiempo Muerto Cong"