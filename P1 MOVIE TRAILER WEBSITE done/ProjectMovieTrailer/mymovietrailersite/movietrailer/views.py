from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Movie, User_Profile, Reviews
from django.contrib.auth.models import User

from movietrailer.custompython.caching import CACHE

from django.contrib.auth import authenticate, login, logout

from django.db import connection
from django.utils import timezone


now = timezone.now().year


# Get CACHE
def getMovieAndReviews(movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
        CACHE['movie'] = movie

        reviews = Reviews.objects.filter(Movie__pk=movie_id).select_related()
        CACHE['reviews'] = reviews

        #review_Registration = ReviewRegistration()
        #CACHE['review_Registration'] = review_Registration

    except Movie.DoesNotExist:
        raise Http404("Question does not exist")


def index(request):
    return render(request, 'movietrailer/index.html', CACHE)


def highestrating(request):
    most_liked = Movie.objects.order_by('-likes_count')[:5]
    context = {'most_liked': most_liked}
    return render(request, 'movietrailer/highest-ratings.html', context)

def mostliked(request):

    return render(request, 'movietrailer/most-liked.html', CACHE)


def mostowned(request):

    return render(request, 'movietrailer/most-owned.html', CACHE)


def hotrightnow(request):

    return render(request, 'movietrailer/hotrightnow.html', CACHE)


def movie(request, movie_id):
    if request.method == 'POST':
        current_user = request.user
        review_title = request.POST.get('review_title')
        review_body = request.POST.get('review_body')
        r = Reviews.objects.create(
            review_title=review_title, review_body=review_body, Movie_id=movie_id, user_id=current_user.id)
        r.save()
        getMovieAndReviews(movie_id)
    else:
        getMovieAndReviews(movie_id)
    return render(request, 'movietrailer/movie.html', CACHE)


# requires  new DB tables or just variable
def favoritecollection(request):
    favoritecollection = Movie.objects.filter(likes_count__gte=7)[:10]
    CACHE['favoritecollection'] = favoritecollection
    return render(request, 'movietrailer/myfavoritecollection.html', CACHE)


def latestcollection(request):

    return render(request, 'movietrailer/latestcollection.html', CACHE)

def top10(request):
    # requires an algorithm

    top10 = Movie.objects.order_by('-likes_count')[:10]
    CACHE['top10'] = top10
    return render(request, 'movietrailer/top10.html', CACHE)


# good
def a_z(request, letter):
    if len(letter) == 0:
        letter = "a"
    movie_table = Movie.objects.filter(title__startswith=letter)[:10]
    CACHE['movie_table'] = movie_table
    CACHE['letter'] = letter.upper()
    return render(request, 'movietrailer/a-z.html', CACHE)
# good seems to be a cache error


def genre(request, genre):
    if len(genre) == 0:
        genre = "action"

    genre = Movie.objects.filter(genres__icontains=genre)[:10]
    CACHE['genre'] = genre
    return render(request, 'movietrailer/genre.html', CACHE)

def genres(request):
    cursor = connection.cursor()
    cursor.execute(
        'SELECT id, title, genres, cover FROM movietrailer_Movie group by genres order by genres')
    row = cursor.fetchall()
    CACHE['available_genres'] = row
    return render(request, 'movietrailer/genres.html', CACHE)


def year(request, year):
    year = Movie.objects.filter(year__contains=year)[:10]
    CACHE['year'] = year

    return render(request, 'movietrailer/year.html', CACHE)


def years(request):
    cursor = connection.cursor()
    cursor.execute(
        'SELECT id, year, title, cover FROM movietrailer_Movie group by year order by year')

    row = cursor.fetchall()
    CACHE['years'] = row
    return render(request, 'movietrailer/years.html', CACHE)

