# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movietrailer', '0004_auto_20170321_0236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='movie',
            new_name='Movie',
        ),
    ]
