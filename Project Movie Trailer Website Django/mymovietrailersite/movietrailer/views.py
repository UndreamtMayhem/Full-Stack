from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movie

# Create your views here.
def index(request):
    #requires an algo and i need to cache these, there is a lot of recycling
    latest_movies = Movie.objects.order_by('-likes_count')
    most_owned = Movie.objects.order_by('-owned_count')
    most_liked = Movie.objects.order_by('-likes_count')
    context = {'latest_movies': latest_movies, 'most_owned': most_owned, 'most_liked': most_liked}
    return render(request,'movietrailer/index.html', context)

def highestrating(request):
     most_liked = Movie.objects.order_by('-likes_count')
     context = {'most_liked': most_liked}
     return render(request,'movietrailer/highest-ratings.html', context)


def mostliked(request):
    latest_movies = Movie.objects.order_by('-likes_count')
    most_owned = Movie.objects.order_by('-owned_count')
    most_liked = Movie.objects.order_by('-likes_count')
    context = {'latest_movies': latest_movies, 'most_owned': most_owned, 'most_liked': most_liked}
    return render(request,'movietrailer/most-liked.html',context)

def mostowned(request):
    latest_movies = Movie.objects.order_by('-likes_count')
    most_owned = Movie.objects.order_by('-owned_count')
    most_liked = Movie.objects.order_by('-likes_count')
    context = {'latest_movies': latest_movies, 'most_owned': most_owned, 'most_liked': most_liked}
    return render(request,'movietrailer/most-owned.html',context)


def hotrightnow(request):
    latest_movies = Movie.objects.order_by('-likes_count')
    most_owned = Movie.objects.order_by('-owned_count')
    most_liked = Movie.objects.order_by('-likes_count')
    context = {'latest_movies': latest_movies, 'most_owned': most_owned, 'most_liked': most_liked}
    return render(request,'movietrailer/hotrightnow.html', context)


def movie(request, movie_id):
     try:
        movie = Movie.objects.get(pk=movie_id)
        context = {'movie': movie}
     except Movie.DoesNotExist:
        raise Http404("Question does not exist")
     return render(request,'movietrailer/movie.html', context)

#requires  new DB tables or just variable
def favoritecollection(request):
     return render(request,'movietrailer/latestcfavoritecollectionollection.html')
def latestcollection(request):
     return render(request,'movietrailer/latestcollection.html')
#requires an algorithm
def top10(request):
     return render(request,'movietrailer/top10.html')






######work on 



def a_z(request):
     return render(request,'movietrailer/a-z.html')


def genre(request):

    return render(request,'movietrailer/genre.html')
