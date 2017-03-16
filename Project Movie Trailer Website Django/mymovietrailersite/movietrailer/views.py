from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    
    return render(request,'movietrailer/index.html')
    #return HttpResponse("welcome index")

def genre(request):

    return render(request,'movietrailer/genre.html')

def highestrating(request):
     return render(request,'movietrailer/highestrating.html')


def latestcollection(request):
     return render(request,'movietrailer/latestcollection.html')

def mostliked(request):
    return render(request,'movietrailer/mostliked.html')

def mostowned(request):
    return render(request,'movietrailer/mostowned.html')


def hotrightnow(request):
     return render(request,'movietrailer/hotrightnow.html')

def movie(request):
     return render(request,'movietrailer/movie.html')

def favoritecollection(request):
     return render(request,'movietrailer/latestcfavoritecollectionollection.html')

def top10(request):
     return render(request,'movietrailer/top10.html')


