# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movietrailer', '0020_auto_20170320_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='datuploaded',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2017, 3, 20, 22, 33, 41, 88441)),
        ),
    ]
