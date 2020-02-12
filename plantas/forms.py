from django import forms
from .models import Planta, Linea, Supervisor, Operador, Bascula, \
    Formadora

class PlantaForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = ['descripcion', 'id_planta', 'estado']
        labels = {'descripcion': 'Descripcioón de la Planta',
        'id_planta':'id_planta',
        'estado': 'Estado'}
        widget = {'descripcion':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class LineaForm(forms.ModelForm):
    planta = forms.ModelChoiceField(
        queryset=Planta.objects.filter(estado=True)
        .order_by('descripcion')
    )

    class Meta:
        model = Linea
        fields = ['planta','descripcion','id_linea' ,'estado']
        labels = {'descripcion': 'Linea',
        'id_linea':'id_linea',
        'estado': 'Estado'}
        widget = {'descripcion':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['planta'].empty_label = 'Seleccione la Planta'
        
       

class SupervisorForm(forms.ModelForm):
    planta = forms.ModelChoiceField(
        queryset=Planta.objects.filter(estado=True)
        .order_by('descripcion')
    )
    class Meta:
        model = Supervisor
        fields = ['planta', 'descripcion','id_supervisor' ,'estado']
        labels = {'planta':'planta',
            'descripcion': 'supervisor',
        'id_supervisor':'id_supervisor',
        'estado': 'Estado'}
        widget = {'descripcion':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

        self.fields['planta'].empty_label = 'Seleccione la Planta'

class OperadorForm(forms.ModelForm):
    planta = forms.ModelChoiceField(
        queryset=Planta.objects.filter(estado=True)
        .order_by('descripcion')
    )
    class Meta:
        model = Operador
        fields = ['planta','descripcion','id_operador' ,'estado']
        labels = {
            'descripcion': 'Operador',
        'id_operador':'id_operador',
        'estado': 'Estado'}
        widget = {'descripcion':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

        self.fields['planta'].empty_label = 'Seleccione la Planta'

class BasculaForm(forms.ModelForm):
    linea = forms.ModelChoiceField(
        queryset=Linea.objects.filter(estado=True)
        .order_by('descripcion')
    )

    class Meta:
        model = Bascula
        fields = ['linea','descripcion','id_bascula','celdas','modelo' ,'estado']
        labels = {'descripcion': 'Bascula',
        'id_bascula':'id_bascula',
        'celdas':'celdas',
        'modelo':'modelo',
        'estado': 'Estado'}
        widget = {'descripcion':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['linea'].empty_label = 'Seleccione la Línea'

class FormadoraForm(forms.ModelForm):
    linea = forms.ModelChoiceField(
        queryset=Linea.objects.filter(estado=True)
        .order_by('descripcion')
    )

    class Meta:
        model = Formadora
        fields = ['linea','descripcion','id_formadora','modelo' ,'estado']
        labels = {'descripcion': 'Formadora',
        'id_formadora':'id_formadora',
        'modelo':'modelo',
        'estado': 'Estado'}
        widget = {'descripcion':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['linea'].empty_label = 'Seleccione la Línea'
        