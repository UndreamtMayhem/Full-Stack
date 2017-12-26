# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movietrailer', '0010_auto_20170317_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='latest_arrivals',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='latest_favoritecollection',
            name='movie',
        ),
        migrations.DeleteModel(
            name='Latest_Arrivals',
        ),
        migrations.DeleteModel(
            name='Latest_FavoriteCollection',
        ),
    ]
