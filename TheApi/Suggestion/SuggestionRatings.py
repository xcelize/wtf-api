import json
import os

from django.conf import settings
from django.core.files.storage import default_storage
from django_pandas.io import read_frame, pd, get_related_model
from rest_framework.renderers import JSONRenderer

from ..models import RatingFilms, Films
from authenticate.models import User

from ..serializers import SpecificFilmSerializer
from authenticate.serializers import SpecificUserSerializer


class SuggestionRatings:

    def __init__(self):
        self.id_users = list()
        self.id_top_n_films = list()
        self.list_suggest_score_films = dict()

    def get_top_10(self, id_user):
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
        note_moyenne = df['note'].mean()
        ratings = df.pivot_table(index=['user_id'], columns=['film_id'], values='note')
        nb_users = User.objects.all().count()
        thresh_user = self.control_thresh(nb_users)
        ratings = ratings.dropna(thresh=thresh_user, axis=1).fillna(0)
        self.id_top_n_films = self.recommended_films_for_user(ratings, note_moyenne, id_user)
        return [Films.objects.get(id_video=id_movie['id_film']) for id_movie in self.id_top_n_films]
        #return self.id_top_n_films

    def control_thresh(self, nb_users):
        if nb_users <= 10:
            thresh_user = 1
        elif 10 < nb_users <= 50:
            thresh_user = 2
        elif 50 < nb_users <= 500:
            thresh_user = 5
        elif 500 < nb_users <= 2000:
            thresh_user = 10
        elif 2000 < nb_users <= 5000:
            thresh_user = 15
        else:
            thresh_user = 20
        return thresh_user

    def recommended_films_for_user(self, df, note_moy, id_user):
        """
        :param df: la table ratings
        :param note_moy: la note moyenne de tous les films/séries
        :param id_user: id de l'utilisateur
        :return: les IDs des 10 films recommandés à cet utilisateur
        """
        # list des id des films/saisons
        ids = df.columns.tolist()


        # la liste des couples (id_movie, note), avec note > 0,
        # est la liste des films/séries déjà notés par l'utilisateur
        ids_et_notes = list()
        # scored_ids est la liste ids des films/saisons déjà scorés
        scored_ids = list()
        for _id in ids:
            note = df.loc[id_user, _id]
            print(note)
            # on veut la liste des films/saisons que cet utilisateur a scorés:
            # tous les films/saisons dont la note = 0 seront éliminés
            if note > 0:
                id_et_note = (_id, note)
                ids_et_notes.append(id_et_note)
                scored_ids.append(_id)

        # la liste des films/saisons similaires à ceux/celles scorés (y compris les films déjà scorés !)
        similar_films = pd.DataFrame()
        for _id, note in ids_et_notes:
            similar_films = similar_films.append(self.get_similar_score(_id, note, df, note_moy), ignore_index=True)

        # en éliminant les films déjà scorés, on obtient les films finaux à recommander à l'utilisateur
        similar_films = similar_films.drop(scored_ids, axis=1)

        # la liste des n films recommandés (dans l'ordre décroissante des scores similaires)
        top_n = similar_films.sum().sort_values(ascending=False).head(10)

        top_n_films = list()
        for _id in top_n.index:
            id_dict = dict()
            id_dict['id_film'] = _id
            top_n_films.append(id_dict)
        return top_n_films

    def get_similar_score_films(self):
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
            base_object['rating_suggestion'] = liste_film
            liste_object.append(base_object)
        if settings.GS:
            self._to_google(liste_object)
        else:
            self._to_local(liste_object)
        return self.list_suggest_score_films

    def _to_google(self, liste_object):
        with default_storage.open('SuggestionRatings.json', 'w') as f:
            json.dump(liste_object, f, indent=4)

    def _to_local(self, liste_object):
        with open(settings.FILE_PATH_SUGGESTION_RATING, 'w') as f:
            json.dump(liste_object, f, indent=4)

    def get_id_user(self):
        list_ids = sorted(set([rating.user.id for rating in RatingFilms.objects.all()]))
        return list_ids

    def get_similar_score(self, titre, note, dataframe, note_moy):
        """
        Fonction de calcul des scores des films qui sont jugés 'similaires'
        :param titre: titre du film
        :param note: note de l'utilistateur pour ce film/séries
        :param dataframe: table ratings
        :param note_moy: la note moyenne de tous les films/séries
        :return: prédiction du score similaire
        """
        # Similarity matrix - standardisation les valeurs  ==> entre -1 et 1
        # CORRELATION DE PEARSON = Méthode Similarité de Cosinus centré
        # -- Soustraire les valeurs dans une ligne (à l'exception de 0) par la moyenne de leur ligne
        # -- Les valeurs résultats se stardardisent entre -1 et 1. Total des valeurs résultats dans une ligne = 0.
        # -- On a centré le rating de chaque utisateur au tour de 0 (rating initialement manquant):
        # --   + Positif rating ==> l'utilisateur aime le film plus que la moyenne
        # --   + Négatif rating ==> l'utilisateur aime le film moins que la moyenne
        item_similarity_df = dataframe.corr(method='pearson')
        similar_score = item_similarity_df[titre] * (note - note_moy)
        return similar_score
