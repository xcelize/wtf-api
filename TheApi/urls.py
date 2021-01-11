from django.urls import path
from . import views

# Ce fichier répertorie toutes les routes de l'API.
# Elles vont permettre une fois dessus d'afficher les vues correspondantes (views.py)

urlpatterns = [
    path('categories', views.CategoriesListView.as_view(), name="list_categories"),  # Affiche les catégories & leur id
    path('films/<int:id_video>', views.RetrieveFilmView.as_view(), name="retrieve_film"),  # Affiche le film avec cet id
    path('films', views.ListFilmView.as_view(), name="list_film"),  # Affiche tous les films de la base (pagination)
    path('films/rating', views.CreateRatingFilm.as_view(), name="create_film_rating"),  # Créer une note (rating)
    path('films/rating/<int:pk>', views.UpdateRatingFilm.as_view(), name="update_film_rating"),  # Update une note
    path('series', views.ListSerieView.as_view(), name="list_serie"),  # Affiche toutes les séries de la base
    path('series/<int:pk>', views.RetrieveSerieView.as_view(), name="retrieve_serie"),  # Affiche la série avec cet id
    path('series/saison/rating', views.CreateRatingSaison.as_view(), name="create_rating_saison"), # Crée une note
    path('series/saison/rating/<int:pk>', views.UpdateRatingSaison.as_view(), name="update_rating_saison"),  # Update
]
