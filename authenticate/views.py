from rest_framework import permissions
from rest_framework.generics import CreateAPIView, UpdateAPIView
from .serializers import UserSerializer, UpdataUserSerializer
from .models import User


class CreateUser(CreateAPIView):

    serializer_class = UserSerializer


class UpdateUser(UpdateAPIView):

    serializer_class = UpdataUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "pk"

    def get_queryset(self):
        return User.objects.all()





