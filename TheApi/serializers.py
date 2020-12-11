from rest_framework import serializers
from .models import Films, Acteurs


class ActeurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Acteurs
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):

    acteurs = ActeurSerializer(many=True)

    class Meta:
        model = Films
        fields = [
            'id_video',
            'titre',
            "date_sortie",
            "poster",
            'plot',
            'vo',
            'duree',
            'acteurs'
        ]
