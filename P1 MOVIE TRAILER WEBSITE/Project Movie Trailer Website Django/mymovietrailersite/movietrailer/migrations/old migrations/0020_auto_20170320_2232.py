# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movietrailer', '0019_auto_20170320_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie_reviews',
            name='review',
        ),
        migrations.AddField(
            model_name='movie_reviews',
            name='review_body',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='movie_reviews',
            name='review_title',
            field=models.CharField(default=datetime.datetime(2017, 3, 20, 22, 32, 53, 321006, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='datuploaded',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2017, 3, 20, 22, 32, 31, 388532)),
        ),
    ]
