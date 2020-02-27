import django_filters
from .models import NominaEnc


class NominaFiltro(django_filters.FilterSet):
    

    CHOICES = (('ascending', 'Ascending'),
    ('descending','Descending'))
        
    

    ordering = django_filters.ChoiceFilter(label='ordering', choices = CHOICES, method = 'filter_by_order')
    
    class Meta:
        Model=NominaEnc
        fields={
            'planta':['icontains'],
            'semana':['icontains']
        }

    def filter_by_order(self, queryset, name, value):
        expresion= 'created' if value =='ascending' else '-created'
        return queryset.order_by(expresion)


