# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movietrailer', '0024_auto_20170321_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie_reviews',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='reviews',
            field=models.ForeignKey(default=1, to='movietrailer.Movie_reviews'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='datuploaded',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2017, 3, 21, 0, 49, 21, 93900)),
        ),
    ]
