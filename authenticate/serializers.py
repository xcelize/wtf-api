from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'email',
            'password',
             'nom',
             'prenom',
             'date_inscription',
             'date_naissance',
             'email',
             'genre',
             'telephone',
             'pays',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }



