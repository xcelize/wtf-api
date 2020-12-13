from rest_framework import serializers
from .models import Films, Acteurs, Categories, Productions, Score


class ActeurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Acteurs
        fields = '__all__'


class CategorieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'


class ProductionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Productions
        fields = '__all__'


class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):

    acteurs = ActeurSerializer(many=True)
    categories = CategorieSerializer(many=True)
    productions = ProductionSerializer(many=True)
    scores = ScoreSerializer(many=True)

    class Meta:
        model = Films
        fields = [
            'id_video',
            'titre',
            "date_sortie",
            "poster",
            'plot',
            'vo',
            "scores",
            'duree',
            'categories',
            'productions',
            'acteurs'
        ]





