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
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return f'{self.nom} - {self.prenom}'

