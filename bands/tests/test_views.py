from django.test import TestCase
from django.contrib.auth import get_user_model

from bands.forms import ArtistCreationForm
User = get_user_model()


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'bands/index.html')


class ArtistListTest(TestCase):

    def test_uses_artists_template(self):
        response = self.client.get('/artists/')
        self.assertTemplateUsed(response, 'bands/artists.html')


class ArtistCreationTest(TestCase):

    def setUp(self):
        # This logs in a test user since this view requires login
        self.client.force_login(User.objects.get_or_create(username='test_user')[0])

    def test_uses_artist_creation_template(self):

        response = self.client.get('/add_artist/')
        self.assertTemplateUsed(response, 'bands/add_artist.html')

    def test_uses_artist_creation_form(self):

        response = self.client.get('/add_artist/')
        self.assertIsInstance(response.context['form'], ArtistCreationForm)


class AboutPageTest(TestCase):

    def test_uses_about_template(self):
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'bands/about.html')


class VenueListTest(TestCase):

    def test_uses_venue_template(self):
        response = self.client.get('/venues/')
        self.assertTemplateUsed(response, 'bands/venues.html')
