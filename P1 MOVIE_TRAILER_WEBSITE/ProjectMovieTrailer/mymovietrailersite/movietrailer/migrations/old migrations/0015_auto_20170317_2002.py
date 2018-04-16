# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movietrailer', '0014_home_page_covers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='url',
            field=models.CharField(max_length=50),
        ),
    ]
