from django.urls import path
from . import views

urlpatterns = [
    path('films/<int:id_video>', views.RetrieveFilmView.as_view(), name="retrieve_film"),
    path('films', views.ListFilmView.as_view(), name="list_film")
]
