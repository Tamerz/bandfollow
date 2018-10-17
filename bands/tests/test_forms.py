from django.test import TestCase

from bands.forms import CustomUserCreationForm, LoginForm, ArtistCreationForm
from bands.models import User, Artist


class CustomUserCreationFormTest(TestCase):

    def test_form_has_css_classes(self):
        form = CustomUserCreationForm()
        for item in form:
            self.assertIn('class="form-control"', str(item))

    def test_form_saves_user(self):
        form = CustomUserCreationForm(data={
            'username': 'jjazz',
            'name': 'Jimmy Jazz',
            'email': 'jimmy.jazz@coolguy.com',
            'password1': 'youneverknow8',
            'password2': 'youneverknow8'
        })
        new_user = form.save()
        self.assertEqual(new_user, User.objects.first())
        self.assertEqual(new_user.username, 'jjazz')
        self.assertEqual(new_user.name, 'Jimmy Jazz')
        self.assertEqual(new_user.email, 'jimmy.jazz@coolguy.com')


class UserLoginFormTest(TestCase):

    def test_form_has_css_classes(self):
        form = LoginForm()
        for item in form:
            self.assertIn('class="form-control"', str(item))


class ArtistCreationFormTest(TestCase):

    def test_form_saves_artist(self):
        form = ArtistCreationForm(data={'name': 'The Melons'})
        new_artist = form.save()
        self.assertEqual(new_artist, Artist.objects.first())
        self.assertEqual(new_artist.name, 'The Melons')
