# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('year', models.DateField()),
                ('main_actor', models.CharField(max_length=30)),
                ('likes_count', models.IntegerField()),
                ('owned_count', models.IntegerField()),
                ('cover', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie_reviews',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('review', models.TextField()),
                ('movie', models.ForeignKey(to='movietrailer.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Movies_liked',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('liked', models.BooleanField()),
                ('movie', models.ForeignKey(to='movietrailer.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Movies_owned',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('owner', models.BooleanField()),
                ('movie', models.ForeignKey(to='movietrailer.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('salt', models.CharField(max_length=6)),
                ('year', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='movies_owned',
            name='user',
            field=models.ForeignKey(to='movietrailer.User'),
        ),
        migrations.AddField(
            model_name='movies_liked',
            name='user',
            field=models.ForeignKey(to='movietrailer.User'),
        ),
        migrations.AddField(
            model_name='movie_reviews',
            name='user',
            field=models.ForeignKey(to='movietrailer.User'),
        ),
    ]
