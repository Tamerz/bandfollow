from django.test import TestCase

from bands.forms import ArtistCreationForm
from bands.models import Artist


class ArtistCreationFormTest(TestCase):

    def test_form_saves_artist(self):
        form = ArtistCreationForm(data={'name': 'The Melons'})
        new_artist = form.save()
        self.assertEqual(new_artist, Artist.objects.first())
        self.assertEqual(new_artist.name, 'The Melons')
