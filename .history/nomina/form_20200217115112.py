from django import forms

from django.forms.models import inlineformset_factory
from .models import NominaEnc, NominaDet, ConceptoNomina

class NominaEncForm(forms.ModelForm):
    fecha_nomina =forms.DateInput()
    planta=forms.TextInput()

    class Meta:
        model=NominaEnc
        fields=[
            'fecha_nomina',
            'planta','area',
            'linea','grupo',
            'supervisor',
            'semana',
        
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class NominaDetForm(forms.ModelForm):
    concepto=forms.ModelChoiceField(
        queryset=ConceptoNomina.objects.filter(estado=True).
        order_by("concepto"),
        empty_label="Seleccione un concepto"
    )

    class Meta:
        model=NominaDet
        fields=[
            'concepto',
            'cantidad'
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_cantidad(self):
        cantidad=self.cleaned_data['cantidad']
        if not cantidad:
            raise forms.ValidationError("Cantidad Requerida")
        elif cantidad <0:
            raise forms.ValidationError("Cantidad Incorrecta")
        return cantidad


DetalleNominaFormSet=inlineformset_factory(NominaEnc, NominaDet, form=NominaDetForm, extra=1,max_num=15)