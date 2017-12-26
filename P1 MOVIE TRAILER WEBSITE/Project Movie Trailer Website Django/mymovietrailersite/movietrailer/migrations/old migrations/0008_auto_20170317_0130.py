# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movietrailer', '0007_auto_20170317_0127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='latest_arrivals',
            old_name='chartPosition',
            new_name='chartposition',
        ),
        migrations.RenameField(
            model_name='latest_favoritecollection',
            old_name='chartPosition',
            new_name='chartposition',
        ),
    ]
