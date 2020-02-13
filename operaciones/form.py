from django import forms
from .models import TipoCambio

class TipoCambioForm(forms.ModelForm):
    class Meta:
        model=TipoCambio
        fields=[
            'fecha',
            'tipo_cambio',
            'estado'
            ]
        labels={
            'fecha':'fecha'
            'tipo_cambio','Tipo Cambio'
            'estado':'Estado'
        }

        widget={'tipo_cambio':forms.TextInput}

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })