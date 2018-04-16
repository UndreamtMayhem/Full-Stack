# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Home_Page_Covers',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('chartposition', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Latest_Arrivals',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('chartposition', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Latest_FavoriteCollection',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('chartposition', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('main_actor', models.CharField(max_length=30)),
                ('likes_count', models.IntegerField()),
                ('owned_count', models.IntegerField()),
                ('cover', models.CharField(max_length=200)),
                ('storyline', models.TextField()),
                ('datuploaded', models.DateTimeField(verbose_name='date published')),
                ('genres', models.CharField(max_length=12, default='action', choices=[('action', 'action'), ('adventure', 'adventure'), ('animation', 'animation'), ('biography', 'biography'), ('comedy', 'comedy'), ('crime', 'crime'), ('documentary', 'documentary'), ('drama', 'drama'), ('family', 'family'), ('fantasy', 'fantasy'), ('film-noir', 'film-noir'), ('history', 'history'), ('horror', 'horror'), ('musical', 'musical'), ('mystery', 'mystery'), ('romance', 'romance'), ('sci-fi', 'sci-fi'), ('sport', 'sport'), ('thriller', 'thriller'), ('war', 'war'), ('western', 'western')])),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Movie_reviews',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('review_title', models.CharField(max_length=50)),
                ('review_body', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movies_liked',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('liked', models.BooleanField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movies_owned',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('owner', models.BooleanField()),
                ('movie', models.ForeignKey(to='movietrailer.Movie')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('salt', models.CharField(max_length=6)),
                ('dob', models.DateField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='latest_favoritecollection',
            name='movie',
            field=models.ForeignKey(to='movietrailer.Movie'),
        ),
        migrations.AddField(
            model_name='latest_arrivals',
            name='movie',
            field=models.ForeignKey(to='movietrailer.Movie'),
        ),
        migrations.AddField(
            model_name='home_page_covers',
            name='movie',
            field=models.ForeignKey(to='movietrailer.Movie'),
        ),
    ]
