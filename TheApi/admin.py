from django.contrib import admin
from .models import Films, RatingFilms, FilmProductions

admin.site.register(Films)
admin.site.register(RatingFilms)
admin.site.register(FilmProductions)
