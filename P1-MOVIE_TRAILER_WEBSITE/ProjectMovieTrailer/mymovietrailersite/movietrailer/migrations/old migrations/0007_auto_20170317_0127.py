# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movietrailer', '0006_auto_20170317_0107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='year',
            new_name='dob',
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.CharField(default='action', max_length=6, choices=[('action', 'action'), ('adventure', 'adventure'), ('animation', 'animation'), ('biography', 'biography'), ('comedy', 'comedy'), ('crime', 'crime'), ('documentary', 'documentary'), ('drama', 'drama'), ('family', 'family'), ('fantasy', 'fantasy'), ('film-noir', 'film-noir'), ('history', 'history'), ('horror', 'horror'), ('musical', 'musical'), ('mystery', 'mystery'), ('romance', 'romance'), ('sci-fi', 'sci-fi'), ('sport', 'sport'), ('thriller', 'thriller'), ('war', 'war'), ('western', 'western')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='genders',
            field=models.CharField(default='other', max_length=6, choices=[('male', 'male'), ('female', 'female'), ('other', 'other')]),
        ),
    ]
