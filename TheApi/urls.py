from django.urls import path
from . import views

urlpatterns = [
    path('films/<int:id_video>', views.RetrieveFilmView.as_view(), name="retrieve_film"),
    path('films', views.ListFilmView.as_view(), name="list_film"),
    path('films/rating', views.CreateRatingFilm.as_view(), name="create_film_rating"),
    path('films/rating/<int:pk>', views.UpdateRatingFilm.as_view(), name="update_film_rating"),
    path('series', views.ListSerieView.as_view(), name="list_serie"),
    path('series/<int:pk>', views.RetrieveSerieView.as_view(), name="retrieve_serie"),
]
