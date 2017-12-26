# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movietrailer', '0013_auto_20170317_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home_Page_Covers',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('chartposition', models.IntegerField()),
                ('movie', models.ForeignKey(to='movietrailer.Movie')),
            ],
        ),
    ]
