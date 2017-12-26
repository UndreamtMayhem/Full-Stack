# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movietrailer', '0009_auto_20170317_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.CharField(default='action', choices=[('action', 'action'), ('adventure', 'adventure'), ('animation', 'animation'), ('biography', 'biography'), ('comedy', 'comedy'), ('crime', 'crime'), ('documentary', 'documentary'), ('drama', 'drama'), ('family', 'family'), ('fantasy', 'fantasy'), ('film-noir', 'film-noir'), ('history', 'history'), ('horror', 'horror'), ('musical', 'musical'), ('mystery', 'mystery'), ('romance', 'romance'), ('sci-fi', 'sci-fi'), ('sport', 'sport'), ('thriller', 'thriller'), ('war', 'war'), ('western', 'western')], max_length=12),
        ),
    ]
