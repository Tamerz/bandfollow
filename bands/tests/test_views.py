from django.test import TestCase

from bands.forms import CustomUserCreationForm
from bands.models import User


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'bands/index.html')


class UserCreationTest(TestCase):

    def test_uses_user_creation_template(self):
        response = self.client.get('/create_account')
        self.assertTemplateUsed(response, 'bands/create_account.html')

    def test_uses_user_creation_form(self):
        response = self.client.get('/create_account')
        self.assertIsInstance(response.context['form'], CustomUserCreationForm)

    def test_can_save_a_POST_request(self):
        self.client.post('/create_account', data={
            'username': 'jjazz',
            'name': 'Jimmy Jazz',
            'email': 'jimmy.jazz@coolguy.com',
            'password1': 'youneverknow8',
            'password2': 'youneverknow8'
        })
        self.assertEqual(User.objects.count(), 1)
        new_user = User.objects.first()
        self.assertEqual(new_user.username, 'jjazz')
        self.assertEqual(new_user.name, 'Jimmy Jazz')
        self.assertEqual(new_user.email, 'jimmy.jazz@coolguy.com')
