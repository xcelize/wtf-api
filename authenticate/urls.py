from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('inscription', views.CreateUser.as_view(), name='inscription'),
    path('profil/<int:pk>', views.UpdateUser.as_view(), name='update_user'),
    path('user/<int:pk>', views.RetrieveUser.as_view(), name='test'),
    path('favoris/film', views.CreateFavorisFilmView.as_view(), name='create_favoris_film'),
    path('favoris/film/<int:pk>', views.UpdateFavorisFilm.as_view(), name='update_favoris_film'),
    path('favoris/serie', views.CreateFavorisSerieView.as_view(), name='create_favoris_serie'),
    path('favoris/serie/<int:pk>', views.UpdateFavorisSerie.as_view(), name='update_favoris_serie')
]
