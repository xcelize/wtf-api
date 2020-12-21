from .models import Films, Series, RatingFilms
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView, CreateAPIView
from .serializers import FilmSerializer, SerieSerializer, RatingSerializer
from rest_framework import permissions


class isOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print(obj.user)
        print(request.user)
        return obj.user == request.user


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


class CreateRatingFilm(CreateAPIView):

    serializer_class = RatingSerializer

    def get_queryset(self):
        return RatingFilms.objects.all()


class UpdateRatingFilm(UpdateAPIView):

    lookup_field = "pk"
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, isOwnerOrReadOnly]

    def get_queryset(self):
        return RatingFilms.objects.all()












