from django.test import TestCase

from bands.models import Artist


class ArtistTest(TestCase):

    def test_saving_and_retrieving_artists(self):
        artist = Artist()
        artist.name = 'The Melons'
        artist.is_approved = True
        artist.save()

        new_artist = Artist.objects.first()

        self.assertEqual(new_artist.name, 'The Melons')
        self.assertEqual(new_artist.is_approved, True)
