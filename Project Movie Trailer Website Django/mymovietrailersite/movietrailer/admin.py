from django.contrib import admin

# Register your models here.

from .models import Movie, User, Movie_reviews, Movies_liked, Movies_owned

admin.site.register(Movie)
admin.site.register(User)
admin.site.register(Movie_reviews)
admin.site.register(Movies_liked)
admin.site.register(Movies_owned)