# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movietrailer', '0021_auto_20170320_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie_reviews',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='movies_liked',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='reviews',
            field=models.ForeignKey(to='movietrailer.Movie_reviews', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='datuploaded',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2017, 3, 21, 0, 45, 7, 41945)),
        ),
    ]
