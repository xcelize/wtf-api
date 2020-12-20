from django.urls import path
from . import views

urlpatterns = [
    path('film/<int:id_video>', views.RetrieveFilmView.as_view(), name="retrieve_film"),
    path('films', views.ListFilmView.as_view(), name="list_film"),
    path('series', views.ListSerieView.as_view(), name="list_serie"),
    path('serie/<int:pk>', views.RetrieveSerieView.as_view(), name="retrieve_serie")
]
