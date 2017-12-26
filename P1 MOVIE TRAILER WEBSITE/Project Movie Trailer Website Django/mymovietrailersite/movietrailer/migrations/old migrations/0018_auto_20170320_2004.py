# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movietrailer', '0017_auto_20170320_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies_watched',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('owner', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='movies_owned',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='movies_owned',
            name='user',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='owned_count',
            new_name='watch_count',
        ),
        migrations.AlterField(
            model_name='movie',
            name='datuploaded',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 20, 20, 4, 50, 914501), verbose_name='date published'),
        ),
        migrations.DeleteModel(
            name='Movies_owned',
        ),
        migrations.AddField(
            model_name='movies_watched',
            name='movie',
            field=models.ForeignKey(to='movietrailer.Movie'),
        ),
        migrations.AddField(
            model_name='movies_watched',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
