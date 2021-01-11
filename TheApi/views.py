from .models import Films, Series, RatingFilms, RatingSaison, Categories
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView, CreateAPIView
from .serializers import CategorieSerializer, FilmSerializer, SerieSerializer, RatingSerializer, RatingSaisonSerializer
from rest_framework import permissions
from .customfilters import FilmFilters, SerieFilters
from drf_multiple_model.views import ObjectMultipleModelAPIView
from django_filters import rest_framework as filters


# Ce fichier contient les vues : elles vont permettre d'afficher le contenu qu'on veut quand elle sont appelées.
# Elles peuvent être appelées depuis le fichier des routes (urls.lpy)

# Vérifie les permissions de l'utilisateur connecté (admin ou user)
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj.user)
        print(request.user)
        return obj.user == request.user


# Récupère les films.
class RetrieveFilmView(RetrieveAPIView):
    lookup_field = 'id_video'
    serializer_class = FilmSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Films.objects.all()


# Affiche les catégories.
class CategoriesListView(ListAPIView):
    serializer_class = CategorieSerializer

    def get_queryset(self):
        return Categories.objects.all()


# Affiche les films.
class ListFilmView(ListAPIView):
    serializer_class = FilmSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = FilmFilters

    def get_queryset(self):
        return Films.objects.all()


# Affiche les séries.
class ListSerieView(ListAPIView):
    serializer_class = SerieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = SerieFilters

    def get_queryset(self):
        return Series.objects.all()


# Récupère les séries.
class RetrieveSerieView(RetrieveAPIView):
    serializer_class = SerieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'

    def get_queryset(self):
        return Series.objects.all()


# Créer une note sur un film.
class CreateRatingFilm(CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return RatingFilms.objects.all()


# Update une note sur un film.
class UpdateRatingFilm(UpdateAPIView):
    lookup_field = "pk"
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return RatingFilms.objects.all()


# Créer une note sur une saison.
class CreateRatingSaison(CreateAPIView):
    serializer_class = RatingSaisonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return RatingSaison.objects.all()


# Update une note sur une saison.
class UpdateRatingSaison(UpdateAPIView):
    lookup_field = "pk"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = RatingSaisonSerializer

    def get_queryset(self):
        return RatingSaison.objects.all()
