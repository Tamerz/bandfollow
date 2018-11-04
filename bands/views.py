from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from bands.forms import ArtistCreationForm, VenueCreationForm
from bands.models import Artist, Venue, Event


def home_page(request):
    return render(request, 'bands/index.html')


def artists(request):
    approved_artists = Artist.objects.filter(is_approved=True)
    return render(request, 'bands/artists.html', {'artists': approved_artists})


def about(request):
    return render(request, 'bands/about.html')


@login_required
def add_artist(request):
    if request.method == 'POST':
        new_artist_form = ArtistCreationForm(data=request.POST)
        if new_artist_form.is_valid():
            new_artist_form.save()
            return redirect(artists)
        else:
            return render(request, 'bands/add_artist.html', {'form': new_artist_form})
    return render(request, 'bands/add_artist.html', {'form': ArtistCreationForm()})


def venues(request):
    approved_venues = Venue.objects.filter(is_approved=True)
    return render(request, 'bands/venues.html', {'venues': approved_venues})


@login_required
def add_venue(request):
    if request.method == 'POST':
        new_venue_form = VenueCreationForm(data=request.POST)
        if new_venue_form.is_valid():
            new_venue_form.save()
            return redirect(venues)
        else:
            return render(request, 'bands/add_venue.html', {'form': new_venue_form})
    return render(request, 'bands/add_venue.html', {'form': VenueCreationForm()})


def events(request):
    approved_events = Event.objects.filter(is_approved=True)
    return render(request, 'bands/events.html', {'events': approved_events})


@login_required
def add_event(request):
    pass
