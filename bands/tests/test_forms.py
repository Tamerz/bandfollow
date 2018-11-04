from django.test import TestCase
from django.utils import timezone
from datetime import datetime

from bands.forms import ArtistCreationForm, VenueCreationForm, EventCreationForm
from bands.models import Artist, Venue, Event


class ArtistCreationFormTest(TestCase):

    def test_form_saves_artist(self):
        form = ArtistCreationForm(data={'name': 'The Melons'})
        new_artist = form.save()
        self.assertEqual(new_artist, Artist.objects.first())
        self.assertEqual(new_artist.name, 'The Melons')


class VenueCreationFormTest(TestCase):

    def test_form_saves_venue(self):
        form = VenueCreationForm(data={'name': 'Super Rock Club'})
        new_venue = form.save()
        self.assertEqual(new_venue, Venue.objects.first())
        self.assertEqual(new_venue.name, 'Super Rock Club')


class EventCreationFormTest(TestCase):

    def test_form_saves_event(self):
        form = EventCreationForm(data={
            'title': 'Big Night Out!',
            'time_and_date': datetime(2019, 3, 22, 18, 30, tzinfo=timezone.utc),
        })
        new_event = form.save()
        self.assertEqual(new_event, Event.objects.first())
        self.assertEqual(new_event.title, 'Big Night Out!')
