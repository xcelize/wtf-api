from .models import Films, Score, Series
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView, CreateAPIView
from .serializers import FilmSerializer, SerieSerializer


class RetrieveFilmView(RetrieveAPIView):

    lookup_field = 'id_video'
    serializer_class = FilmSerializer

    def get_queryset(self):
        return Films.objects.all()


class ListFilmView(ListAPIView):
    serializer_class = FilmSerializer

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







