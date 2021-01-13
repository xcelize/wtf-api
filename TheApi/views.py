import json
import os
import itertools
from django.conf import settings
from django.core.files.storage import default_storage
from django_filters import rest_framework as filters
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework import permissions, status
from rest_framework.exceptions import APIException
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .ServiceUnreachable import ServiceUnavailable
from .Suggestion.RecommandationFavoris import RecommandationFavoris
from .Suggestion.Tendance import Tendance
from .Suggestion.SuggestionRatings import SuggestionRatings

from .customfilters import FilmFilters, SerieFilters
from .models import Films, Series, RatingFilms, RatingSaison, Categories
from .serializers import CategorieSerializer, FilmSerializer, SerieSerializer, RatingSerializer, RatingSaisonSerializer
from .tasks import MakeSuggestion



class isOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print(obj.user)
        print(request.user)
        return obj.user == request.user


class RetrieveFilmView(RetrieveAPIView):

    lookup_field = 'id_video'
    serializer_class = FilmSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Films.objects.all()


class CategoriesListView(ListAPIView):

    serializer_class = CategorieSerializer

    def get_queryset(self):
        return Categories.objects.all()


class ListFilmView(ListAPIView):

    serializer_class = FilmSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = FilmFilters

    def get_queryset(self):
        return Films.objects.all()


class ListSerieView(ListAPIView):

    serializer_class = SerieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = SerieFilters

    def get_queryset(self):
        return Series.objects.all()


class RetrieveSerieView(RetrieveAPIView):

    serializer_class = SerieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'

    def get_queryset(self):
        return Series.objects.all()


class CreateRatingFilm(CreateAPIView):

    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return RatingFilms.objects.all()


class UpdateRatingFilm(UpdateAPIView):

    lookup_field = "pk"
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, isOwnerOrReadOnly]

    def get_queryset(self):
        return RatingFilms.objects.all()


class CreateRatingSaison(CreateAPIView):

    serializer_class = RatingSaisonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return RatingSaison.objects.all()


class UpdateRatingSaison(UpdateAPIView):

    lookup_field = "pk"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, isOwnerOrReadOnly]
    serializer_class = RatingSaisonSerializer

    def get_queryset(self):
        return RatingSaison.objects.all()



class GetUserSuggestionRating(APIView):

    gs_filename = "RecommandationFavoris.json"
    file_path = settings.FILE_PATH_SUGGESTION_RATING
    permission_classes = [permissions.IsAuthenticated]

    # ouvrir le fichier
    # chercher l'utilisateur connecté
    # recuperer son objet
    # servir son objet
    def get(self, request, format=None):
        if not default_storage.exists(self.gs_filename) or not os.path.exists(self.file_path):
            return Response(status=status.HTTP_404_NOT_FOUND)
        user = request.user
        if settings.GS:
            with default_storage.open(self.gs_filename) as f:
                json_data = json.load(f)
        else:
            with open(self.file_path, 'r') as f:
                json_data = json.load(f)
        li = [element for element in filter(lambda x: (x['user']['id'] is user.id), json_data)]
        return Response(li[0])


class GetUserSuggestionFavoris(APIView):

    gs_filename = "SuggestionRatings.json"
    file_path = settings.FILE_PATH_RECOMMANDATION_FAVORIS
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        if not default_storage.exists(self.gs_filename) or not os.path.exists(self.file_path):
            return Response(status=status.HTTP_404_NOT_FOUND)
        user = request.user
        if settings.GS:
            with default_storage.open(self.gs_filename) as f:
                json_data = json.load(f)
        else:
            with open(self.file_path, 'r') as f:
                json_data = json.load(f)
        li = [element for element in filter(lambda x: (x['user']['id'] is user.id), json_data)]
        return Response(li[0])


class GetTendanceAPI(APIView):

    file_path = settings.FILE_PATH_TENDANCE
    gs_filename = "Tendance.json"

    def get(self, request, format=None):
        if not default_storage.exists(self.gs_filename) or not os.path.exists(self.file_path):
            return Response(status=status.HTTP_404_NOT_FOUND)
        if settings.GS:
            with default_storage.open(self.gs_filename) as f:
                json_data = json.load(f)
        else:
            with open(self.file_path, 'r') as f:
                json_data = json.load(f)
        return Response(json_data)

# TODO
class VideoAPIView(ObjectMultipleModelAPIView):
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['titre']

    def get_querylist(self):
        pass
        # titre = self.request.query_params['titre'].replace('-', ' ')
        # querylist = [
        #     {'queryset': Films.objects.exclude(titre__icontains=titre), 'serializer_class': FilmSerializer},
        #     {'queryset': Series.objects.exclude(titre__icontains=titre), 'serializer_class': SerieSerializer}
        # ]
        # return querylist








