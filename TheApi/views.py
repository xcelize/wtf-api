from .models import Films, Score, Series
from .serializers import FilmSerializer, SerieSerializer
from .customfilters import FilmFilters
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from drf_multiple_model.views import ObjectMultipleModelAPIView
from django_filters import rest_framework as filters


class RetrieveFilmView(RetrieveAPIView):
    lookup_field = 'id_video'
    serializer_class = FilmSerializer

    def get_queryset(self):
        return Films.objects.all()


class ListFilmView(ListAPIView):
    serializer_class = FilmSerializer
    filterset_class = FilmFilters

    def get_queryset(self):
        return Films.objects.all()


class ListSerieView(ListAPIView):
    serializer_class = SerieSerializer

    def get_queryset(self):
        return Series.objects.all()


class RetrieveSerieView(RetrieveAPIView):
    serializer_class = SerieSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Series.objects.all()


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
