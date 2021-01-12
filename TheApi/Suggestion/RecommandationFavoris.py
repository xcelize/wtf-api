import json
import os

from authenticate.models import FilmFavoris
from django.conf import settings

from ..models import Films
from ..serializers import SpecificFilmSerializer
from django_pandas.io import read_frame, pd, get_related_model
from authenticate.serializers import SpecificUserSerializer
from authenticate.models import User
from rest_framework.renderers import JSONRenderer


class RecommandationFavoris:

    def __init__(self):
        self.id_users = list()
        self.list_favoris_recommand = dict()
        self.last_id_movie_favoris = None

    def get_top_10(self, id_user):
        """
        :param n: nombre de films/séries souhaités
        :param id_user: id de l'utilisateur
        :return: la liste des n top films/séries à recommander pour l'utilisateur
        """
        qs = FilmFavoris.objects.all()
        df = pd.DataFrame.from_records(
            qs.values("film__id_video", "user__id", "date_ajout")
        ).rename(
            columns={
                'film__id_video': 'film_id',
                'user__id': 'user_id',
                'date_ajout': 'date_ajout'
            }
        )
        df['like'] = 1

        matrix_users_videos = df.pivot_table(index='user_id', columns='film_id', values='like').fillna(0)

        # chercher le dernier ID vidéo ajouté
        last_id_favoris = self.get_last_id_favoris(id_user)
        # la colonne du dernier ID vidéo ajouté
        last_id_fav_col = matrix_users_videos[last_id_favoris]
        # regarder les colonnes et chercher les films/séries similaires que ce dernier
        similar_videos = matrix_users_videos.corrwith(last_id_fav_col).sort_values(ascending=False)

        # supprimer les films/séries déjà ajoutés dans le Favoris
        id_videos = matrix_users_videos.columns
        added_videos = list()
        for _id in id_videos:
            if matrix_users_videos.loc[id_user, _id] == 1:
                added_videos.append(_id)

        similar_videos_df = similar_videos.drop(added_videos).head(10).to_frame(name='similarite')
        return [Films.objects.get(id_video=id_movie) for id_movie in similar_videos_df.index]


    def get_id_user(self):
        list_ids = sorted(set([favoris.user.id for favoris in FilmFavoris.objects.all()]))
        return list_ids

    def get_last_id_favoris(self, id_user):
        last_id = FilmFavoris.objects.filter(id=id_user).latest('date_ajout').film.id_video
        return last_id

    def get_list_recommand_favoris(self):
        self.id_users = self.get_id_user()
        liste_object = []
        for _id in self.id_users:
            base_object = {}
            user = User.objects.get(id=_id)
            user_serializer = SpecificUserSerializer(user)
            json_data_user = JSONRenderer().render(user_serializer.data)
            base_object['user'] = json.loads(json_data_user.decode("utf-8"))
            top_10 = self.get_top_10(_id)
            liste_film = []
            for data in top_10:
                film_serializer = SpecificFilmSerializer(data)
                json_data_film = JSONRenderer().render(film_serializer.data)
                liste_film.append(json.loads(json_data_film.decode("utf-8")))
            base_object['favoris_suggestion'] = liste_film
            liste_object.append(base_object)
        path_file = os.path.join(os.path.join(settings.BASE_DIR, 'store'), 'RecommandationFavoris.json')
        with open(path_file, 'w') as f:
            json.dump(liste_object, f, indent=4)
        # self.list_favoris_recommand[_id] = top_10

        return self.list_favoris_recommand
