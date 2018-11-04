from django.test import TestCase
from django.utils import timezone
from datetime import datetime

from bands.models import Artist, Venue, Event


class ArtistTest(TestCase):

    def test_saving_and_retrieving_artists(self):
        artist = Artist()
        artist.name = 'The Melons'
        artist.save()

        new_artist = Artist.objects.first()

        self.assertEqual(new_artist.name, 'The Melons')
        self.assertEqual(new_artist.is_approved, False)


class VenueTest(TestCase):

    def test_saving_and_retrieving_venues(self):
        venue = Venue()
        venue.name = 'Super Rock Club'
        venue.save()

        new_venue = Venue.objects.first()

        self.assertEqual(new_venue.name, 'Super Rock Club')
        self.assertEqual(new_venue.is_approved, False)


class EventTest(TestCase):

    def test_saving_and_retrieving_events(self):
        artist = Artist.objects.create(name='The Melons')
        venue = Venue.objects.create(name='Super Rock Club')

        event = Event()
        event.title = 'Big Night Out!'
        event.date_and_time = datetime(2018, 12, 13, 18, 00, tzinfo=timezone.utc)
        event.venue = venue
        event.save()
        event.artists.add(artist)
        event.save()

        new_event = Event.objects.first()

        self.assertEqual(new_event.title, 'Big Night Out!')
        self.assertEqual(new_event.venue.name, 'Super Rock Club')
        self.assertEqual(len(new_event.artists.all()), 1)
        artist = Artist.objects.create(name='Big Grant')
        event.artists.add(artist)
        event.save()

        new_event = Event.objects.first()

        self.assertEqual(len(new_event.artists.all()), 2)
