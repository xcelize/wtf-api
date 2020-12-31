from rest_framework import permissions
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView
from .serializers import UserSerializer, UpdataUserSerializer, FilmFavorisSerializer, SerieFavorisSerializer
from .models import User, SerieFavoris, FilmFavoris


class isOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print(obj.user)
        print(request.user)
        return obj.user == request.user


class CreateUser(CreateAPIView):

    serializer_class = UserSerializer


class UpdateUser(UpdateAPIView):

    serializer_class = UpdataUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "pk"

    def get_queryset(self):
        return User.objects.all()


class RetrieveUser(RetrieveAPIView):

    lookup_field = "pk"
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateFavorisFilmView(CreateAPIView):

    queryset = FilmFavoris.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, isOwnerOrReadOnly]
    serializer_class = FilmFavorisSerializer

    def get_queryset(self):
        return FilmFavoris.objects.all()


class UpdateFavorisFilm(UpdateAPIView):

    lookup_field = "pk"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, isOwnerOrReadOnly]
    serializer_class = FilmFavorisSerializer

    def get_queryset(self):
        return FilmFavoris.objects.all()


class CreateFavorisSerieView(CreateAPIView):

    queryset = FilmFavoris.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, isOwnerOrReadOnly]
    serializer_class = SerieFavorisSerializer

    def get_queryset(self):
        return SerieFavoris.objects.all()


class UpdateFavorisSerie(UpdateAPIView):

    lookup_field = "pk"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, isOwnerOrReadOnly]
    serializer_class = SerieFavorisSerializer

    def get_queryset(self):
        return SerieFavoris.objects.all()






