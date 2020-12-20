from rest_framework.generics import CreateAPIView, UpdateAPIView
from .serializers import UserSerializer, UpdataUserSerializer
from .models import User
from rest_framework import permissions

class CreateUser(CreateAPIView):

    serializer_class = UserSerializer



class UpdateUser(UpdateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UpdataUserSerializer
    lookup_field = "pk"

    def get_queryset(self):
        return User.objects.all()





