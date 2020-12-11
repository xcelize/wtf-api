from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer


class CreateUser(CreateAPIView):

    serializer_class = UserSerializer
