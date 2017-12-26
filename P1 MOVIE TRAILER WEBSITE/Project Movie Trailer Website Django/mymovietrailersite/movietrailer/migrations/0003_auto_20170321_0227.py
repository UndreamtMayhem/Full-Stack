# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movietrailer', '0002_auto_20170321_0224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='reviews',
            field=models.ForeignKey(to='movietrailer.Reviews', default=1),
            preserve_default=False,
        ),
    ]
