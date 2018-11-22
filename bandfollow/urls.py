"""bandfollow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from bands import views as bands_views
from accounts import views as accounts_views


urlpatterns = [
    path('', bands_views.home_page, name='home'),
    path('artists/', bands_views.artists, name='artists'),
    path('artists/<str:name>', bands_views.artist_detail, name='artist_detail'),
    path('add_artist/', bands_views.add_artist, name='add_artist'),
    path('set_favorite_artist/', bands_views.set_favorite_artist, name='set_favorite_artist'),
    path('venues/', bands_views.venues, name='venues'),
    path('venues/<str:name>', bands_views.venue_detail, name='venue_detail'),
    path('add_venue/', bands_views.add_venue, name='add_venue'),
    path('events/', bands_views.events, name='events'),
    path('event_detail/<int:id>', bands_views.event_detail, name='event_detail'),
    path('set_favorite_venue/', bands_views.set_favorite_venue, name='set_favorite_venue'),
    path('add_event/', bands_views.add_event, name='add_event'),
    path('about/', bands_views.about, name='about'),
    path('admin/', admin.site.urls),
    path('create_account/', accounts_views.create_account, name='create_account'),
    path('search/', bands_views.search, name='search'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('approve_artists/', bands_views.approve_artists, name='approve_artists'),
]
