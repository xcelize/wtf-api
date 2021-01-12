from django_pandas.io import read_frame, pd, get_related_model
from ..models import RatingFilms, Films
from django.core import serializers
from django.conf import settings
import os
from ..serializers import FilmSerializer
from rest_framework.renderers import JSONRenderer
import json
import ast

class Tendance:
    """
    Les films tendances s'affichent de manière permanente à la page d'acceuil.
    Il s'agit des n films qui ont la meilleure moyenne des scores et qui obtiennent le plus grande nombre de votes.
    """

    def __init__(self):
        self.list_film_tendance = list()

    def get_top(self):
        """
        :param n: nombre de films/saisons souhaité à retourner
        :return: la liste des n films/saisons qui ont la tendance.
        """
        qs = RatingFilms.objects.all()
        df = pd.DataFrame.from_records(
            qs.values("film__id_video", 'user__id', 'note')
        ).rename(
            columns={
                'film__id_video': 'film_id',
                'user__id': 'user_id',
                'note': 'note'
            }
        )
        # matrice d'interaction user - item
        user_movie_df = df.pivot_table(index=['user_id'], columns=['film_id'], values='note')
        nb_ratings_df = self.nb_ratings_df(user_movie_df)
        moy_ratings_df = self.moy_ratings_df(user_movie_df)
        combine_df = pd.concat([nb_ratings_df, moy_ratings_df], axis=1)
        combine_df['rating_tendance'] = combine_df['nb_ratings'] * combine_df['moyenne']
        top_n_movies = combine_df.sort_values('rating_tendance', ascending=False).head(10)
        l = [Films.objects.get(id_video=id_movie) for id_movie in top_n_movies.index]
        liste = []
        for i in l:
            filmSerializer = FilmSerializer(i)
            json_data = JSONRenderer().render(filmSerializer.data)
            liste.append(json.loads(json_data.decode("utf-8")))
        path_file = os.path.join(settings.BASE_DIR, 'tendance.json')
        with open(path_file, 'w') as f:
            json.dump(liste, f, indent=4)

    def nb_ratings_df(self, df):
        return df.count().to_frame(name='nb_ratings')

    def moy_ratings_df(self, df):
        return df.mean().to_frame(name='moyenne')
