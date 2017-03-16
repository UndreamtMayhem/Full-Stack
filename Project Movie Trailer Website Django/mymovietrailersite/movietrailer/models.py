from django.db import models


#char needs max length
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField()
    year = models.DateField()
    #//add choice 
    #//genre = models.CharField()//choicefield
    main_actor = models.CharField(max_length=30)
    likes_count = models.IntegerField()
    owned_count = models.IntegerField()
    cover = models.CharField(max_length=200)

class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=30) #//must salt
    salt = models.CharField(max_length=6)
    year = models.DateField()
    #gender = choice

class Movie_reviews(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    review = models.TextField()

class Movies_liked(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked = models.BooleanField()


class Movies_owned(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.BooleanField()
