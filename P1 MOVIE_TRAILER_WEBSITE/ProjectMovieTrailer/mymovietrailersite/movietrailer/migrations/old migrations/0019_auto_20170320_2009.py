# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movietrailer', '0018_auto_20170320_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies_owned',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('owner', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='movies_watched',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='movies_watched',
            name='user',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='watch_count',
            new_name='owned_count',
        ),
        migrations.AlterField(
            model_name='movie',
            name='datuploaded',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2017, 3, 20, 20, 9, 19, 58927)),
        ),
        migrations.DeleteModel(
            name='Movies_watched',
        ),
        migrations.AddField(
            model_name='movies_owned',
            name='movie',
            field=models.ForeignKey(to='movietrailer.Movie'),
        ),
        migrations.AddField(
            model_name='movies_owned',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
