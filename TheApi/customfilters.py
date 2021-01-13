from django_filters import rest_framework as filters
from .models import Films, Series

'''
Classe qui filre les résultats lié à des attributs de l'objet <Films>
'''
class FilmFilters(filters.FilterSet):
    titre = filters.CharFilter(lookup_expr='icontains')
    duree_max = filters.NumberFilter(field_name='duree', lookup_expr='lt')
    start_date = filters.DateFilter(field_name='date_sortie', lookup_expr='gt')
    end_date = filters.DateFilter(field_name='date_sortie', lookup_expr='lt')

    '''
    Rencense les champs utilsé pour les filtres
    '''
    class Meta:
        model = Films
        fields = ['titre', 'categories', 'date_sortie', 'vo', 'duree']


class SerieFilters(filters.FilterSet):
    titre = filters.CharFilter(lookup_expr='icontains')
    start_date = filters.DateFilter(field_name='date_sortie', lookup_expr='gt')
    end_date = filters.DateFilter(field_name='date_sortie', lookup_expr='lt')

    class Meta:
        model = Series
        fields = ['titre', 'categories', 'date_sortie', 'vo']

