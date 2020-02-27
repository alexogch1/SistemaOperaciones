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
            
        }

    def filter_by_order(self, queryset, name, value):
        expresion= 'planta' if value =='ascending' else '-planta'
        return queryset.order_by(expresion)


