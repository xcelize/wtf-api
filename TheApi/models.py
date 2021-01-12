# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth import get_user_model


class Acteurs(models.Model):
    id_personne = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=254, blank=True, null=True)
    photo_profil = models.CharField(max_length=254, blank=True, null=True)
    popularite = models.FloatField(blank=True, null=True)  # This field type is a guess.
    personnage = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acteurs'


class Directeurs(models.Model):

    id_personne = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=254, blank=True, null=True)
    photo_profil = models.CharField(max_length=254, blank=True, null=True)
    popularite = models.FloatField(max_length=254, blank=True, null=True)
    departement = models.CharField(max_length=254, blank=True, null=True)
    job = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'directeurs'



class Categories(models.Model):
    id_categ = models.IntegerField(primary_key=True)
    libelle = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'

    def __str__(self):
        return f'{self.libelle}'


class FilmActeurs(models.Model):
    film = models.ForeignKey('Films', models.DO_NOTHING, blank=True, null=True)
    acteur = models.ForeignKey(Acteurs, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film_acteurs'


class FilmDirecteurs(models.Model):
    film = models.ForeignKey('Films', models.DO_NOTHING, blank=True, null=True)
    directeur = models.ForeignKey(Directeurs, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film_directeurs'


class FilmCategories(models.Model):
    film = models.ForeignKey('Films', models.DO_NOTHING, blank=True, null=True)
    categorie = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film_categories'


class FilmProductions(models.Model):
    film = models.ForeignKey('Films', models.DO_NOTHING, blank=True, null=True)
    production = models.ForeignKey('Productions', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film_productions'


class Films(models.Model):

    id_video = models.IntegerField(primary_key=True)
    titre = models.CharField(max_length=254, blank=True, null=True)
    date_sortie = models.CharField(max_length=254, blank=True, null=True)
    poster = models.CharField(max_length=254, blank=True, null=True)
    plot = models.CharField(max_length=254, blank=True, null=True)
    vo = models.CharField(max_length=254, blank=True, null=True)
    duree = models.IntegerField(blank=True, null=True)
    categories = models.ManyToManyField(to=Categories, through=FilmCategories, symmetrical=False)
    productions = models.ManyToManyField(to='Productions', through=FilmProductions, symmetrical=False)
    acteurs = models.ManyToManyField(to=Acteurs, through=FilmActeurs, symmetrical=False)
    directeurs = models.ManyToManyField(to=Directeurs, through=FilmDirecteurs, symmetrical=False)

    class Meta:
        managed = False
        db_table = 'films'



class RatingFilms(models.Model):

    id = models.AutoField(primary_key=True, auto_created=True)
    film = models.ForeignKey(Films, models.DO_NOTHING, db_column='id_film')
    user = models.ForeignKey(get_user_model(), models.DO_NOTHING, db_column='id_user')
    note = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'rating_films'
        unique_together = ['film', 'user']


class RatingSaison(models.Model):

    saison = models.ForeignKey("Saisons", models.DO_NOTHING, db_column='id_saison')
    user = models.ForeignKey(get_user_model(), models.DO_NOTHING, db_column='id_user')
    note = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'rating_series'
        unique_together = ['saison', 'user']


class Productions(models.Model):
    id_production = models.IntegerField(primary_key=True)
    logo = models.CharField(max_length=254, blank=True, null=True)
    nom = models.CharField(max_length=254, blank=True, null=True)
    pays = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productions'


class Saisons(models.Model):
    id_saison = models.IntegerField(primary_key=True)
    nb_episode = models.CharField(max_length=254, blank=True, null=True)
    nom = models.CharField(max_length=254, blank=True, null=True)
    num_saison = models.IntegerField(blank=True, null=True)
    id_serie = models.ForeignKey('Series', models.DO_NOTHING, db_column='id_serie', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saisons'


class SerieCategories(models.Model):
    serie = models.ForeignKey('Series', models.DO_NOTHING, blank=True, null=True)
    categorie = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serie_categories'


class Plateformes(models.Model):
    id_plateforme = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=254, blank=True, null=True)
    logo = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plateformes'


class SeriePlateformes(models.Model):
    serie = models.ForeignKey('Series', models.DO_NOTHING, blank=True, null=True)
    plateforme = models.ForeignKey(Plateformes, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serie_plateformes'


class SerieProductions(models.Model):
    serie = models.ForeignKey('Series', models.DO_NOTHING, blank=True, null=True)
    production = models.ForeignKey(Productions, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serie_productions'


class Series(models.Model):

    id_video = models.IntegerField(primary_key=True)
    titre = models.CharField(max_length=254, blank=True, null=True)
    date_sortie = models.CharField(max_length=254, blank=True, null=True)
    poster = models.CharField(max_length=254, blank=True, null=True)
    plot = models.CharField(max_length=254, blank=True, null=True)
    vo = models.CharField(max_length=254, blank=True, null=True)
    nb_saison = models.IntegerField(blank=True, null=True)
    categories = models.ManyToManyField(to=Categories, through=SerieCategories, symmetrical=False)
    plateformes = models.ManyToManyField(to=Plateformes, through=SeriePlateformes, symmetrical=False)
    productions = models.ManyToManyField(to='Productions', through=SerieProductions, symmetrical=False)
    acteurs = models.ManyToManyField(to=Acteurs, through="SerieActeurs", symmetrical=False)
    directeurs = models.ManyToManyField(to=Directeurs, through="SerieDirecteurs", symmetrical=False)

    class Meta:
        managed = False
        db_table = 'series'


class SerieActeurs(models.Model):
    serie = models.ForeignKey('Series', models.DO_NOTHING, blank=True, null=True)
    acteur = models.ForeignKey(Acteurs, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serie_acteurs'

class SerieDirecteurs(models.Model):
    serie = models.ForeignKey('Series', models.DO_NOTHING, blank=True, null=True)
    directeur = models.ForeignKey(Directeurs, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serie_directeurs'
