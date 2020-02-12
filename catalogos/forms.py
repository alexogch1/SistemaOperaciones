from django import forms
from .models import Cliente, Marca, Ingred, Corte, CasoEsp, Presentacion, \
    Producto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['descripcion_cliente', 'id_cliente', 'estado']
        labels = {'descripcion_cliente': 'Descripcioón del Cliente  ',
        'id_cliente':'id_cliente',
        'estado': 'Estado'}
        widget = {'descripcion_cliente':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class MarcaForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.filter(estado=True)
        .order_by('descripcion_cliente')
    )
    class Meta:
        model = Marca
        fields = ['cliente','descripcion_marca', 'id_marca','estado']
        labels = {'descripcion_marca': 'Marca',
        'id_marca':'ID',
        'estado': 'Estado'}
        widget = {'descripcion_marca':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

        self.fields['cliente'].empty_label = 'Seleccione el cliente'

class IngredForm(forms.ModelForm):
    class Meta:
        model = Ingred
        fields = ['descripcion_ing', 'id_ingred', 'estado']
        labels = {'descripcion_ing': 'Descripción ',
        'id_ingred':'id ',
        'estado': 'Estado'}
        widget = {'descripcion_ing':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class CorteForm(forms.ModelForm):

    class Meta:
        model = Corte
        fields = ['descripcion_corte', 'id_corte', 'estado']
        labels = {'descripcion_corte': 'Corte',
        'id_corte':'id',
        'estado': 'Estado'}
        widget = {'descripcion_corte':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
    
class PresentacionForm(forms.ModelForm):
    class Meta:
        model = Presentacion
        fields = [
            'descripcion_presenta', 
            'id_presentacion',
            'paqs',
            'peso',
            'unidad', 
            'peso_caja',  
            'estado'
            ]

        labels = {
            'descripcion_presenta': 'Descripcioón de la Presentacion',
            'id_presentacion':'id Presentacion',
            'paqs':'Paquetes',
            'peso':'Peso',
            'unidad':'medida',
            'peso_caja':'peso caja (lbs)',
            'estado': 'Estado'
        }
        
        
        widgets = {
            'id_presentacion':forms.TextInput(attrs={'class':'form-control', 'label':'id_presentacion'}),
            'descripcion_presenta':forms.TextInput(attrs={'class':'form-control', 'label':'descripcion_presenta'}),
            'paqs':forms.TextInput(attrs={'class':'form-control', 'label':'paqs'}),
            'peso':forms.TextInput(attrs={'class':'form-control', 'label':'peso'}),
            'peso_caja':forms.TextInput(attrs={'class':'form-control', 'label':'peso_caja'})

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['peso_caja'].widget.attrs["readonly"]=True

class CasoEspForm(forms.ModelForm):
    class Meta:
        model = CasoEsp
        fields = ['descripcion_ce', 'id_ce', 'estado']
        labels = {'descripcion_ce': 'Descripcioón del Caso Especial',
        'id_ce':' id',
        'estado': 'Estado'}
        widget = {'descripcion_ce':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['descripcion_prod', 'id_producto','peso_caja','estado']
        labels = {'descripcion_prod': 'producto',
        'id_producto':'Id Producto',
        'descripcion_prod':'descripcion prod',
        'peso_caja':'peso_caja',
        'estado': 'Estado'}

        widgets = {
            'id_producto':forms.TextInput(attrs={'class':'form-control', 'label':'id_producto'}),
        'descripcion_prod':forms.TextInput(attrs={'class':'form-control', 'label':'descripcion_prod'}),
        'peso':forms.TextInput(attrs={'class':'form-control', 'label':'peso'})
        }
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

