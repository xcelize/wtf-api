import random
from celery import Task, current_app
from django.conf import settings
import os
from celery.utils.log import get_task_logger
from .Suggestion.SuggestionRatings import SuggestionRatings
from .Suggestion.RecommandationFavoris import RecommandationFavoris
from .Suggestion.Tendance import Tendance


class MakeSuggestion(Task):

    name = 'SuggestionTasks'
    ignore_result = False

    def run(self):
        recommandation_favoris = RecommandationFavoris()
        suggestion_rating = SuggestionRatings()
        tendance = Tendance()
        recommandation_favoris.get_list_recommand_favoris()
        suggestion_rating.get_similar_score_films()
        tendance.get_top()


current_app.tasks.register(MakeSuggestion())

