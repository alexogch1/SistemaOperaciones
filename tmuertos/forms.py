from django import forms
from .models import CategoriaTM, CausaTM

class CategoriaTMForm(forms.ModelForm):
    class Meta:
        model = CategoriaTM
        fields = ['descripcion', 'id_categoriaTM', 'estado']
        labels = {'descripcion': 'Descripcioón de la Categoria',
        'id_categoriaTM':'id_categoriaTM',
        'estado': 'Estado'}
       

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class CausaTMForm(forms.ModelForm):
    categoriaTM = forms.ModelChoiceField(
        queryset=CategoriaTM.objects.filter(estado=True)
        .order_by('descripcion')
    )
    class Meta:
        model = CausaTM
        fields = ['categoriaTM','descripcion','id_causaTM', 'tipo','tolerancia','estado']
        labels = {'descripcion': 'Categoria',
        'id_causaTM':'id_causaTM',
        'tolerancia':'Tolerancia',
        'tipo':'tipo',
        'estado': 'Estado'}
        #widget = {'descripcion':forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

        self.fields['categoriaTM'].empty_label = 'Seleccione la Categoria de TM'