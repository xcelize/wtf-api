from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    nom = models.CharField(max_length=30, null=True)
    prenom = models.CharField(max_length=30, null=True)
    date_inscription = models.DateTimeField(auto_now=True)
    date_naissance = models.DateTimeField(null=True)
    email = models.EmailField(unique=True)
    genre = models.CharField(max_length=10, null=True)
    telephone = models.CharField(max_length=10, null=True)
    pays = models.CharField(max_length=30, null=True)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = ('user',)
        verbose_name_plural = ('users',)
        db_table = 'user'

    def get_full_name(self):
        return f'{self.nom} - {self.prenom}'


class FilmFavoris(models.Model):

    film = models.ForeignKey("TheApi.Films", models.DO_NOTHING, db_column='id_film')
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_user')
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Film: {self.film.titre} - User: {self.user.email}'

    class Meta:
        verbose_name_plural = "Films Favoris"
        unique_together = ['user', 'film']


class SerieFavoris(models.Model):

    serie = models.ForeignKey("TheApi.Series", models.DO_NOTHING, db_column='id_serie')
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_user')
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Serie: {self.serie.titre} - User: {self.user.email}'

    class Meta:
        unique_together = ['user', 'serie']
