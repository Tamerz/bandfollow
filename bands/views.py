from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from bands.forms import ArtistCreationForm
from bands.models import Artist


def home_page(request):
    return render(request, 'bands/index.html')


def artists(request):
    all_artists = Artist.objects.all()
    return render(request, 'bands/artists.html', {'artists': all_artists})


@login_required
def add_artist(request):
    form = ArtistCreationForm()
    return render(request, 'bands/add_artist.html', {'form': form})
