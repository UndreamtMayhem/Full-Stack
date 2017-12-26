# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movietrailer', '0005_movie_storyline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Latest_Arrivals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chartPosition', models.IntegerField()),
                ('movie', models.ForeignKey(to='movietrailer.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Latest_FavoriteCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chartPosition', models.IntegerField()),
                ('movie', models.ForeignKey(to='movietrailer.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='genders',
            field=models.CharField(choices=[('male', 'Freshman'), ('female', 'Sophomore'), ('other', 'Other')], max_length=6, default='other'),
        ),
    ]
