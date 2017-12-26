# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movietrailer', '0004_remove_movie_storyline'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='storyline',
            field=models.TextField(default=None),
        ),
    ]
