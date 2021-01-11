from django_filters import rest_framework as filters
from .models import Films, Series


# Ce fichier contient tous les filtres personnalisés pour rechercher les films & les séries en GET.

# Filtres de recherche avancée pour les films
class FilmFilters(filters.FilterSet):
    titre = filters.CharFilter(lookup_expr='icontains')  # Champ titre = utilisation d'un 'LIKE' (icontains)
    duree_max = filters.NumberFilter(field_name='duree', lookup_expr='lt')  # Champ duree_max = durée lesser than ...
    start_date = filters.DateFilter(field_name='date_sortie', lookup_expr='gt')  # Champ date de début recherchée
    end_date = filters.DateFilter(field_name='date_sortie', lookup_expr='lt')  # Champ date de fin recherchée

    class Meta:
        model = Films
        fields = ['titre', 'categories', 'date_sortie', 'vo', 'duree']  # Champs en + pour la recherche avancée


# Filtres de recherche avancée pour les séries
class SerieFilters(filters.FilterSet):
    titre = filters.CharFilter(lookup_expr='icontains')  # Champ titre = utilisation d'un 'LIKE' (icontains)
    start_date = filters.DateFilter(field_name='date_sortie', lookup_expr='gt')  # Champ date de début recherchée
    end_date = filters.DateFilter(field_name='date_sortie', lookup_expr='lt')  # Champ date de fin recherchée

    class Meta:
        model = Series
        fields = ['titre', 'categories', 'date_sortie', 'vo']  # Champs en + pour la recherche avancée
