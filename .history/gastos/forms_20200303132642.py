from django import forms
from .models import GastosCuenta, GastosSubCuenta, GastoEnc, GastoDet

class CuentaGastosForm(forms.ModelForm):
    class Meta:
        model = GastosCuenta
        fields = ['descripcion_cuenta_gasto', 'id_cuenta_gasto', 'estado']
        labels = {'descripcion_cuenta_gasto': 'Descripción ',
        'id_cuenta_gasto':'id ',
        'estado': 'Estado'}
        widget = {'descripcion_cuenta_gasto':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class SubCuentaGastosForm(forms.ModelForm):
    cuenta = forms.ModelChoiceField(
        queryset=GastosCuenta.objects.filter(estado=True)
        .order_by('descripcion_cuenta_gasto')
    )
    class Meta:
        model = GastosSubCuenta
        fields = ['cuenta','descripcion_subcuenta_gasto', 'id_subcuenta_gasto','estado']
        labels = {'descripcion_subcuenta_gasto': 'Descripción',
        'id_subcuenta_gasto':'ID',
        'estado': 'Estado'}
        widget = {'descripcion_subcuenta_gasto':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

        self.fields['cuenta'].empty_label = 'Seleccione la cuenta'



class GastosEncForm(forms.ModelForm):
    fecha_registro =forms.DateInput()
    unidad_negocio=forms.TextInput()
    area=forms.TextInput()


    class Meta:
        model=GastoEnc
        fields=[
            'fecha_registro',
            'unidad_negocio','area',
 
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class GastosDetForm(forms.ModelForm):
    subcuenta=forms.ModelChoiceField(
        queryset=GastosSubCuenta.objects.filter(estado=True).
        order_by("descripcion_subcuenta_gasto"),
        empty_label="Seleccione una cuenta"
    )

    class Meta:
        model=GastoDet
        fields=[
            'grupo',
            'subcuenta',
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


DetalleGastosFormSet=inlineformset_factory(GastoDet, GastoDet, form=GastosDetForm, extra=1,max_num=200)