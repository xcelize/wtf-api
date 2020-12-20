from .models import Films, Score, Series
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView, CreateAPIView
from .serializers import FilmSerializer, SerieSerializer
from rest_framework import permissions


class RetrieveFilmView(RetrieveAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id_video'
    serializer_class = FilmSerializer

    def get_queryset(self):
        return Films.objects.all()


class ListFilmView(ListAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FilmSerializer

    def get_queryset(self):
        return Films.objects.all()


class ListSerieView(ListAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SerieSerializer

    def get_queryset(self):
        return Series.objects.all()


class RetrieveSerieView(RetrieveAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SerieSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Series.objects.all()







