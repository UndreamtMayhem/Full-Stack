from django.db import models
from django.contrib.auth.models import User
import datetime

"""
filter examples and timed
timeit[Model.objects.filter(date_created__year=today.year, date_created__month=today.month, date_created__day=today.day)]
1000 loops, best of 3: 652 us per loop

timeit[Model.objects.filter(date_created__gte=today)]
1000 loops, best of 3: 631 us per loop

timeit[Model.objects.filter(date_created__startswith=today)]
1000 loops, best of 3: 541 us per loop

timeit[Model.objects.filter(date_created__contains=today)]
1000 loops, best of 3: 536 us per loop

"""
now = datetime.datetime.now()

# blank=True
# Create your models here.


class Movie(models.Model):

    #reviews = models.ForeignKey(Reviews, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    year = models.IntegerField()

    main_actor = models.CharField(max_length=30)
    likes_count = models.IntegerField()
    owned_count = models.IntegerField()
    cover = models.CharField(max_length=200)
    storyline = models.TextField()
    datuploaded = models.DateTimeField('date published')
    ACTION = 'action'
    ADVENTURE = 'adventure'
    ANIMATION = 'animation'
    BIOGRAPHY = 'biography'
    COMEDY = 'comedy'
    CRIME = 'crime'
    DOCUMENTARY = 'documentary'
    DRAMA = 'drama'
    FAMILY = 'family'
    FANTASY = 'fantasy'
    FILM_NOIR = 'film-noir'
    HISTORY = 'history'
    HORROR = 'horror'
    MUSICAL = 'musical'
    MYSTERY = 'mystery'
    ROMANCE = 'romance'
    SCI_Fi = 'sci-fi'
    SPORT = 'sport'
    THRILLER = 'thriller'
    WAR = 'war'
    WESTERN = 'western'

    GENRE_CHOICES = (
        (ACTION, 'action'),
        (ADVENTURE, 'adventure'),
        (ANIMATION, 'animation'),
        (BIOGRAPHY, 'biography'),
        (COMEDY, 'comedy'),
        (CRIME, 'crime'),
        (DOCUMENTARY, 'documentary'),
        (DRAMA, 'drama'),
        (FAMILY, 'family'),
        (FANTASY, 'fantasy'),
        (FILM_NOIR, 'film-noir'),
        (HISTORY, 'history'),
        (HORROR, 'horror'),
        (MUSICAL, 'musical'),
        (MYSTERY, 'mystery'),
        (ROMANCE, 'romance'),
        (SCI_Fi, 'sci-fi'),
        (SPORT, 'sport'),
        (THRILLER, 'thriller'),
        (WAR, 'war'),
        (WESTERN, 'western'),
    )
    genres = models.CharField(
        max_length=12,
        choices=GENRE_CHOICES,
        default=ACTION,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salt = models.CharField(max_length=6)
    dob = models.DateField()

    @classmethod
    def create_profile(cls, user, salt, dob, genders):
        profile = cls(user=user, salt=salt, dob=dob, genders=genders)
        # do something with the book
        return profile


class Movies_liked(models.Model):
    #movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked = models.BooleanField()

    def __str__(self):
        return self.movie.title


class Movies_owned(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.BooleanField()

    def __str__(self):
        return self.movie.title


class Latest_Arrivals(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    chartposition = models.IntegerField()

    def __str__(self):
        return self.movie.title


class Latest_FavoriteCollection(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    chartposition = models.CharField(max_length=50)

    def __str__(self):
        return self.movie.title


class Home_Page_Covers(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    chartposition = models.IntegerField()

    def __str__(self):
        return self.movie.title


class Reviews(models.Model):
    Movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_title = models.CharField(max_length=50)
    review_body = models.TextField()

