from django.test import TestCase

from bands.models import Artist, Venue


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
