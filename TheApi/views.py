from .models import Films, Score
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView, CreateAPIView
from .serializers import FilmSerializer


class RetrieveFilmView(RetrieveAPIView):

    lookup_field = 'id_video'
    serializer_class = FilmSerializer

    def get_queryset(self):
        return Films.objects.all()


class ListFilmView(ListAPIView):
    serializer_class = FilmSerializer

    def get_queryset(self):
        return Films.objects.all()







