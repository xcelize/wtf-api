from .models import User, FilmFavoris, SerieFavoris
from rest_framework import serializers, exceptions
from TheApi.serializers import FilmSerializer, SerieSerializer
from TheApi.models import Films
import django.contrib.auth.password_validation as validators

class FilmFavorisSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FilmFavoris
        fields = ['id', 'film', 'user', 'date_ajout']
        extra_kwargs = {
            'user': {'write_only': True}
        }

    def to_representation(self, instance):
        self.fields['film'] = FilmSerializer()
        return super(FilmFavorisSerializer, self).to_representation(instance)



class SerieFavorisSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = SerieFavoris
        fields = ['id', 'serie', 'user', 'date_ajout']
        extra_kwargs = {
            'user': {'write_only': True}
        }

    def to_representation(self, instance):
        self.fields['serie'] = SerieSerializer()
        return super(SerieFavorisSerializer, self).to_representation(instance)


class FilmFavorisForGet(serializers.ModelSerializer):

    film = FilmSerializer()

    class Meta:
        model = FilmFavoris
        fields = [
            'id',
            'film',
            'date_ajout'
        ]


class SerieFavorisForGet(serializers.ModelSerializer):

    serie = SerieSerializer()

    class Meta:
        model = SerieFavoris
        fields = [
            'id',
            'serie',
            'date_ajout'
        ]


class SpecificUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'nom',
            'prenom',
            'date_inscription',
            'date_naissance',
            'email',
            'genre',
            'telephone',
            'pays'
        ]


class UserSerializer(serializers.ModelSerializer):

    film_favoris = FilmFavorisForGet(source="filmfavoris_set", many=True, read_only=True)
    serie_favoris = SerieFavorisSerializer(source='seriefavoris_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
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
            'film_favoris',
            'serie_favoris'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    def validate(self, attrs):
        validators.validate_password(attrs['password'])
        return attrs


class UpdataUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'email',
            'nom',
            'prenom',
            'date_naissance',
            'genre',
            'telephone'
        ]




