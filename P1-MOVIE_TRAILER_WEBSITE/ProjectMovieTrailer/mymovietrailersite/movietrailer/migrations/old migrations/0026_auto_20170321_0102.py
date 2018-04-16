# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movietrailer', '0025_auto_20170321_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='datuploaded',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2017, 3, 21, 1, 2, 3, 704483)),
        ),
    ]
