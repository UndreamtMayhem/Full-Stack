# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movietrailer', '0002_auto_20170316_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='storyline',
            field=models.TextField(default=None),
        ),
    ]
