"""mymovietrailersite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from movietrailer import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

app_name = 'movietrailer'
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^index/', RedirectView.as_view(url='/')),
    url(r'^genre/(?P<genre>[a-z]+)', views.genre),
    url(r'^genres/', views.genres),
    url(r'^a-z/(?P<letter>[a-z]?)', views.a_z),
    url(r'^highestrating/', views.highestrating),
    url(r'^hotrightnow/', views.hotrightnow),
    url(r'^mostliked/', views.mostliked),
    url(r'^mostowned/', views.mostowned),
    url(r'^movie/(?P<movie_id>[0-9]+)/$', views.movie),
    url(r'^top10/', views.top10),
    url(r'^year/(?P<year>[0-9]{4})/$', views.year),
    url(r'^years/$', views.years),

]
