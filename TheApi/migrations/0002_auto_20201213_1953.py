# Generated by Django 3.1.4 on 2020-12-13 18:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TheApi', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Scorer',
            new_name='Score',
        ),
    ]
