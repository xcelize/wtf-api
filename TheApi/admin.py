from django.contrib import admin
from .models import Films, ScoreFilm, Score

admin.site.register(Films)
admin.site.register(Score)
admin.site.register(ScoreFilm)
