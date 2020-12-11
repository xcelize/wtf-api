from .models import Films
from rest_framework.generics import RetrieveAPIView, ListAPIView
from .serializers import FilmSerializer
from django_filters.rest_framework import DjangoFilterBackend


class RetrieveFilmView(RetrieveAPIView):

    lookup_field = 'id_video'
    serializer_class = FilmSerializer

    def get_queryset(self):
        return Films.objects.all()


class ListFilmView(ListAPIView):
    serializer_class = FilmSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categories']

    def get_queryset(self):
        return Films.objects.all()

