# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movietrailer', '0023_auto_20170321_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='reviews',
        ),
        migrations.AddField(
            model_name='movie_reviews',
            name='movie',
            field=models.ForeignKey(default=1, to='movietrailer.Movie'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='datuploaded',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2017, 3, 21, 0, 47, 10, 533923)),
        ),
    ]
