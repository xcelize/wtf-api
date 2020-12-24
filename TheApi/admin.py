from django.contrib import admin
from .models import Films, RatingFilms, FilmProductions, RatingSaison

admin.site.register(Films)
admin.site.register(RatingFilms)
admin.site.register(FilmProductions)
admin.site.register(RatingSaison)
