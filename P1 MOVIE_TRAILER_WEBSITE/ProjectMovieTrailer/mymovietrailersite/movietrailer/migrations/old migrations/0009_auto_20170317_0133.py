# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movietrailer', '0008_auto_20170317_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latest_favoritecollection',
            name='chartposition',
            field=models.CharField(max_length=50),
        ),
    ]
