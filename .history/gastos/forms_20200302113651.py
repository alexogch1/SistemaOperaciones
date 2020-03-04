from django import forms
from .models import GastosCuenta, GastosSubCuenta

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


