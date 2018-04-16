# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movietrailer', '0003_auto_20170316_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='storyline',
        ),
    ]
