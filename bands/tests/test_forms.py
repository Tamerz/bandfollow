from django.test import TestCase
from django.contrib.auth.models import User

from bands.forms import CustomUserCreationForm


class CustomUserCreationFormTest(TestCase):

    def test_form_has_css_classes(self):
        form = CustomUserCreationForm()
        self.assertIn('class="form-control"', form.as_p())

    def test_form_saves_user(self):
        form = CustomUserCreationForm(data={
            'username': 'jjazz',
            'first_name': 'Jimmy',
            'last_name': 'Jazz',
            'email': 'jimmy.jazz@coolguy.com',
            'password1': 'youneverknow8',
            'password2': 'youneverknow8'
        })
        new_user = form.save()
        self.assertEqual(new_user, User.objects.first())
        self.assertEqual(new_user.username, 'jjazz')
        self.assertEqual(new_user.first_name, 'Jimmy')
        self.assertEqual(new_user.last_name, 'Jazz')
        self.assertEqual(new_user.email, 'jimmy.jazz@coolguy.com')
