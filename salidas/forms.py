from django import forms

from .models import ProduccionEnc, TiempoMuertoEnc, \
        ProduccionCongEnc, TiempoMuertoCongEnc

class ProduccionEncForm(forms.ModelForm):
    fecha_produccion = forms.DateInput() 

    class Meta:
        model = ProduccionEnc
        fields = [ 'planta','linea','turno', 'supervisor','operador','plantilla', 'observaciones', 'fecha_produccion','ftm','fpr','cantidad','peso','total_utilizado', 'total_produccion','total_merma']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['fecha_produccion'].widget.attrs['readonly'] = True
        self.fields['total_produccion'].widget.attrs['readonly'] = True
        self.fields['total_utilizado'].widget.attrs['readonly'] = True
        self.fields['total_merma'].widget.attrs['readonly'] = True
        
class TiempoMuertoEncForm(forms.ModelForm):
    fecha_produccion = forms.DateInput() 

    class Meta:
        model = TiempoMuertoEnc
        fields = [ 'planta','linea','turno', 'supervisor', 'observaciones', 'fecha_produccion','total_tm']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['fecha_produccion'].widget.attrs['readonly'] = True
        self.fields['total_tm'].widget.attrs['readonly'] = True
     

        # Inicia forms para Congelación

class ProduccionCongEncForm(forms.ModelForm):
    fecha_produccion = forms.DateInput() 
        
    class Meta:
        model = ProduccionCongEnc
        fields = [ 'planta','linea','shift','horas_turno', 'supervisor','plantilla', 'observaciones', 'fecha_produccion','cantidad','peso','total_utilizado', 'total_produccion','total_merma']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['fecha_produccion'].widget.attrs['readonly'] = True
        self.fields['total_produccion'].widget.attrs['readonly'] = True
        self.fields['total_utilizado'].widget.attrs['readonly'] = True
        self.fields['total_merma'].widget.attrs['readonly'] = True
                
class TiempoMuertoCongEncForm(forms.ModelForm):
    fecha_produccion = forms.DateInput() 
        
    class Meta:
        model = TiempoMuertoCongEnc
        fields = [ 'planta','linea','turno', 'supervisor', 'observaciones', 'fecha_produccion','total_tm']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['fecha_produccion'].widget.attrs['readonly'] = True
        self.fields['total_tm'].widget.attrs['readonly'] = True
             