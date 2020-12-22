from django_filters import rest_framework as filters
from .models import Films


class FilmFilters(filters.FilterSet):
    titre = filters.CharFilter(lookup_expr='icontains')
    duree_max = filters.NumberFilter(field_name='duree', lookup_expr='lt')
    end_date = filters.DateFilter(field_name='date_sortie', lookup_expr='gt')
    start_date = filters.DateFilter(field_name='date_sortie', lookup_expr='lt')

    class Meta:
        model = Films
        fields = ['titre', 'categories', 'date_sortie', 'vo', 'duree']
