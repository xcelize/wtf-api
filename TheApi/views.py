from .models import Films, Series, RatingFilms
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView, CreateAPIView
from .serializers import FilmSerializer, SerieSerializer, RatingSerializer
from rest_framework import permissions
from .customfilters import FilmFilters, SerieFilters
from drf_multiple_model.views import ObjectMultipleModelAPIView
from django_filters import rest_framework as filters


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








