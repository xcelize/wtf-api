from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.CategoriesListView.as_view(), name="list_categories"),
    path('films/<int:id_video>', views.RetrieveFilmView.as_view(), name="retrieve_film"),
    path('films', views.ListFilmView.as_view(), name="list_film"),
    path('films/rating', views.CreateRatingFilm.as_view(), name="create_film_rating"),
    path('films/rating/<int:pk>', views.UpdateRatingFilm.as_view(), name="update_film_rating"),
    path('series', views.ListSerieView.as_view(), name="list_serie"),
    path('series/<int:pk>', views.RetrieveSerieView.as_view(), name="retrieve_serie"),
    path('series/saison/rating', views.CreateRatingSaison.as_view(), name="create_rating_saison"),
    path('series/saison/rating/<int:pk>', views.UpdateRatingSaison.as_view(), name="update_rating_saison"),
    path('videos/all', views.VideoAPIView.as_view(), name="list_videos"),
    path('suggestion-rating', views.GetUserSuggestionRating.as_view(), name="suggestion_rating"),
    path('suggestion-favoris', views.GetUserSuggestionFavoris.as_view(), name="suggestion_favoris"),
    path('tendance', views.GetTendanceAPI.as_view(), name="tendance")
]
