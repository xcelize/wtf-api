from rest_framework import serializers
from .models import Films, Acteurs, Categories, Productions, Score, Series, Saisons


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


class SaisonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Saisons
        fields = [
            'id_saison',
            'nb_episode',
            'nom',
            'num_saison'
        ]


class FilmSerializer(serializers.ModelSerializer):

    categories = CategorieSerializer(many=True)
    productions = ProductionSerializer(many=True)
    scores = ScoreSerializer(many=True)

    class Meta:
        model = Films
        fields = [
            'id_video',
            'titre',
            'date_sortie',
            'poster',
            'plot',
            'vo',
            'scores',
            'duree',
            'categories',
            'productions',
        ]


class SerieSerializer(serializers.ModelSerializer):

    categories = CategorieSerializer(many=True)
    productions = ProductionSerializer(many=True)
    saisons = SaisonSerializer(source='saisons_set', many=True)

    class Meta:
        model = Series
        fields = [
            'id_video',
            'titre',
            'date_sortie',
            'poster',
            'plot',
            'vo',
            'nb_saison',
            'categories',
            'productions',
            'saisons'
        ]








