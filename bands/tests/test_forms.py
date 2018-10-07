from django.test import TestCase

from bands.forms import CustomUserCreationForm
from bands.models import CustomUser


class CustomUserCreationFormTest(TestCase):

    def test_form_has_css_classes(self):
        form = CustomUserCreationForm()
        self.assertIn('class="form-control"', form.as_p())

    def test_form_saves_user(self):
        form = CustomUserCreationForm(data={
            'username': 'jjazz',
            'name': 'Jimmy Jazz',
            'email': 'jimmy.jazz@coolguy.com',
            'password1': 'youneverknow8',
            'password2': 'youneverknow8'
        })
        new_user = form.save()
        self.assertEqual(new_user, CustomUser.objects.first())
        self.assertEqual(new_user.username, 'jjazz')
        self.assertEqual(new_user.name, 'Jimmy Jazz')
        self.assertEqual(new_user.email, 'jimmy.jazz@coolguy.com')
