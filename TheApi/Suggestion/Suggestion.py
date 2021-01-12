from WtfApi.TheApi.models import Films
from authenticate.models import User


class Suggestion:

    def __init__(self, user: User, film_suggestion_rating: [Films]):

        self.user = User
        self.films_suggestion = film_suggestion_rating

    def to_json(self):
        pass
