from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Movie, User_Profile, Reviews
from django.contrib.auth.models import User

from movietrailer.custompython.forms import RegistrationForm, ReviewRegistration
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
        review_Registration = ReviewRegistration()
        CACHE['review_Registration'] = review_Registration
    except Movie.DoesNotExist:
        raise Http404("Question does not exist")


def index(request):
    # print(CACHE)
    return render(request, 'movietrailer/index.html', CACHE)


def highestrating(request):
    most_liked = Movie.objects.order_by('-likes_count')[:5]
    context = {'most_liked': most_liked}
    return render(request, 'movietrailer/highest-ratings.html', context)


def register(request):
    # If it's a HTTP POST, we're interested in processing form data.
    registered = False
    if request.method == 'POST':
        '''
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        '''
        # if login
        user_form = RegistrationForm(request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            #user = user_form.save()
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']
            user_form.clean_password()
            email = user_form.cleaned_data['email']
            user = User.objects.create_user(username, email, password)
            user.save()
            # Update our variable to tell the template registration was successful.
            registered = True
            return HttpResponseRedirect("../")
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = RegistrationForm()
        CACHE['user_form'] = user_form
        #profile_form = UserProfileForm()
    return render(request, 'movietrailer/signupsignin.html', CACHE)


def authenticates(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        loginusername = request.POST.get('username')
        loginpassword = request.POST.get('loginpassword')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=loginusername, password=loginpassword)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            if user.is_active:
                login(request, user)
            #request.session['username'] = username
                return HttpResponseRedirect('/')
        else:
            # Bad login details were provided. So we can't log the user in.

            return HttpResponse('invalid form')
            # return HttpResponseRedirect('../../index')


# done
def mostliked(request):

    return render(request, 'movietrailer/most-liked.html', CACHE)


def mostowned(request):
    return render(request, 'movietrailer/most-owned.html', CACHE)


def hotrightnow(request):
    return render(request, 'movietrailer/hotrightnow.html', CACHE)


# on it
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

# requires an algorithm


def top10(request):
    top10 = Movie.objects.order_by('-likes_count')[:10]
    CACHE['top10'] = top10
    return render(request, 'movietrailer/top10.html', CACHE)


# Use the login_required() decorator to ensure only those logged in can access the view.
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage. display logged out
    return HttpResponseRedirect('/index/')


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
# good


def genres(request):
    cursor = connection.cursor()
    cursor.execute(
        'SELECT id, title, genres, cover FROM movietrailer_Movie group by genres order by genres')
    row = cursor.fetchall()
    CACHE['available_genres'] = row
    return render(request, 'movietrailer/genres.html', CACHE)


def year(request, year):
    year = Movie.objects.filter(year__contains=year)[:10]
    # print(movie_table)
    CACHE['year'] = year

    # return HttpResponse("i worked")
    return render(request, 'movietrailer/year.html', CACHE)


def years(request):
    cursor = connection.cursor()
    cursor.execute(
        'SELECT id, year, title, cover FROM movietrailer_Movie group by year order by year')

    row = cursor.fetchall()
    CACHE['years'] = row
    #context = {'row': row}
    print(row)
    return render(request, 'movietrailer/years.html', CACHE)

    # return render(request,'movietrailer/genre.html')
