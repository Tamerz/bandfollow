from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from bands.forms import ArtistCreationForm, VenueCreationForm, EventCreationForm
from bands.models import Artist, Venue, Event


def home_page(request):
    return render(request, 'bands/index.html')


def artists(request):
    approved_artists = Artist.objects.filter(is_approved=True)
    return render(request, 'bands/artists.html', {'artists': approved_artists})


def artist_detail(request, name):
    artist = get_object_or_404(Artist, name=name)
    return render(request, 'bands/artist_detail.html', {'artist': artist})


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


def venue_detail(request, name):
    venue = get_object_or_404(Venue, name=name)
    return render(request, 'bands/venue_detail.html', {'venue': venue})


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
    if request.method == 'POST':
        new_event_form = EventCreationForm(data=request.POST)
        if new_event_form.is_valid():
            new_event_form.save()
            return redirect(events)
        else:
            return render(request, 'bands/add_event.html', {'form': new_event_form})

    return render(request, 'bands/add_event.html', {'form': EventCreationForm()})
