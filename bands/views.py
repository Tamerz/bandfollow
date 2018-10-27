from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from bands.forms import ArtistCreationForm
from bands.models import Artist


def home_page(request):
    return render(request, 'bands/index.html')


def artists(request):
    approved_artists = Artist.objects.filter(is_approved=True)
    return render(request, 'bands/artists.html', {'artists': approved_artists})


def about(request):
    return render(request, 'bands/about.html')


@login_required
def add_artist(request):
    form = ArtistCreationForm()
    if request.method == 'POST':
        new_artist_form = ArtistCreationForm(data=request.POST)
        if new_artist_form.is_valid():
            new_artist_form.save()
            return redirect(artists)
        else:
            return render(request, 'bands/add_artist.html', {'form': form})
    return render(request, 'bands/add_artist.html', {'form': form})


def venues(request):
    return render(request, 'bands/venues.html')


def add_venue(request):
    pass
