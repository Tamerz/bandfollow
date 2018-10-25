from django.test import TestCase

from bands.forms import ArtistCreationForm


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'bands/index.html')


class ArtistListTest(TestCase):

    def test_uses_artists_template(self):
        response = self.client.get('/artists')
        self.assertTemplateUsed(response, 'bands/artists.html')


class ArtistCreationTest(TestCase):

    def test_uses_artist_creation_template(self):
        response = self.client.get('/add_artist')
        self.assertTemplateUsed(response, 'bands/add_artist.html')

    def test_uses_artist_creation_form(self):
        response = self.client.get('/add_artist')
        self.assertIsInstance(response.context['form'], ArtistCreationForm)


class AboutPageTest(TestCase):

    def test_uses_about_template(self):
        response = self.client.get('/about')
        self.assertTemplateUsed(response, 'bands/about.html')
