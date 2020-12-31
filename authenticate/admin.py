from django.contrib import admin
from .models import User, FilmFavoris, SerieFavoris

admin.site.register(User)
admin.site.register(FilmFavoris)
admin.site.register(SerieFavoris)
