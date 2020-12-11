# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acteurs(models.Model):
    id_personne = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=254, blank=True, null=True)
    photo_profil = models.CharField(max_length=254, blank=True, null=True)
    popularite = models.TextField(blank=True, null=True)  # This field type is a guess.
    personnage = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acteurs'


class Categories(models.Model):
    id_categ = models.IntegerField(primary_key=True)
    libelle = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'

    def __str__(self):
        return f'{self.libelle}'


class Equipe(models.Model):
    id_personne = models.IntegerField()
    nom = models.CharField(max_length=254, blank=True, null=True)
    photo_profil = models.CharField(max_length=254, blank=True, null=True)
    popularite = models.TextField(blank=True, null=True)  # This field type is a guess.
    departement = models.CharField(max_length=254, blank=True, null=True)
    job = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipe'


class Equipes(models.Model):
    id_personne = models.IntegerField()
    nom = models.CharField(max_length=254, blank=True, null=True)
    photo_profil = models.CharField(max_length=254, blank=True, null=True)
    popularite = models.TextField(blank=True, null=True)  # This field type is a guess.
    departement = models.CharField(max_length=254, blank=True, null=True)
    job = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipes'


class FilmActeurs(models.Model):
    film = models.ForeignKey('Films', models.DO_NOTHING, blank=True, null=True)
    acteur = models.ForeignKey(Acteurs, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film_acteurs'


class FilmCategories(models.Model):
    film = models.ForeignKey('Films', models.DO_NOTHING, blank=True, null=True)
    categorie = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film_categories'


class FilmEquipes(models.Model):
    film = models.ForeignKey('Films', models.DO_NOTHING, blank=True, null=True)
    equipe = models.ForeignKey(Equipe, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film_equipes'


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
    duree = models.CharField(max_length=254, blank=True, null=True)
    acteurs = models.ManyToManyField(to=Acteurs, through=FilmActeurs, symmetrical=False)
    productions = models.ManyToManyField(to="Productions", through=FilmProductions, symmetrical=False)
    categories = models.ManyToManyField(to=Categories, through=FilmCategories, symmetrical=False)

    class Meta:
        managed = False
        db_table = 'films'
        verbose_name = 'Film'
        verbose_name_plural = 'Films'

    def __str__(self):
        return f'{self.titre}'


class Productions(models.Model):
    id_production = models.IntegerField(primary_key=True)
    logo = models.CharField(max_length=254, blank=True, null=True)
    nom = models.CharField(max_length=254, blank=True, null=True)
    pays = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productions'
