from django.contrib import admin

# Register your models here.

from .models import Movie, User_Profile, Reviews, Movies_liked, Movies_owned, Latest_Arrivals, Latest_FavoriteCollection, Home_Page_Covers

admin.site.register(Movie)

admin.site.register(User_Profile)
admin.site.register(Reviews)
admin.site.register(Movies_liked)
admin.site.register(Movies_owned)
admin.site.register(Latest_Arrivals)
admin.site.register(Latest_FavoriteCollection)
admin.site.register(Home_Page_Covers)
