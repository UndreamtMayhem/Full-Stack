from movietrailer.models import Movie, Latest_Arrivals, Latest_FavoriteCollection, Home_Page_Covers
from django.utils import timezone
from datetime import date, datetime, timedelta

this_year = date.today()


class CacheStore(object):
    def fetch_cache(self):
        latest_movies = Movie.objects.order_by('-likes_count')[:5]
        most_owned = Movie.objects.order_by('-owned_count')[:5]
        most_liked = Movie.objects.order_by('-likes_count')[:5]
        latestuploads = Movie.objects.filter(
            datuploaded__year=this_year.year)[:5]
        ten_latest_uploads = Movie.objects.order_by(
            'title').filter(datuploaded__year=this_year.year)[:10]
        #newest_arrival = Movie.objects.filter(datuploaded__lte=now)[:5]
        #newest_arrival= Latest_Arrivals.objects.order_by('-chartposition')
        my_fave_collection = Latest_FavoriteCollection.objects.order_by(
            'chartposition')
        #my_fave_collection = Latest_FavoriteCollection.objects.all()
        # Venue.objects.all()
        home_page_covers = Home_Page_Covers.objects.order_by('-chartposition')
        movie_table = Movie.objects.filter(title__startswith="a")[:10]
        all_categories = ['action', 'adventure', 'animation', 'biography', 'comedy', 'crime', 'documentary', 'drama', 'family',
                          'fantasy', 'film-noir', 'history', 'horror', 'musical', 'mystery', 'romance',  'sci-fi', 'sport', 'thriller', 'war', 'western']

        CACHE = {
            'all_categories': all_categories,
            'latest_movies': latest_movies,
            'ten_latest_uploads': ten_latest_uploads,
            'most_owned': most_owned,
            'most_liked': most_liked,
            'latestuploads': latestuploads,
            'my_fave_collection': my_fave_collection,
            'home_page_covers': home_page_covers,
            'movie_table': movie_table
        }
        return CACHE


cache_store = CacheStore()
CACHE = cache_store.fetch_cache()
