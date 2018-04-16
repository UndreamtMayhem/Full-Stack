# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movietrailer', '0003_auto_20170321_0227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='reviews',
        ),
        migrations.AddField(
            model_name='reviews',
            name='movie',
            field=models.ForeignKey(to='movietrailer.Movie', default=''),
            preserve_default=False,
        ),
    ]
