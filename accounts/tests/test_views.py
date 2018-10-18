from django.test import TestCase
from django.contrib.auth import get_user_model

from accounts.forms import CustomUserCreationForm


class LoginTest(TestCase):

    def test_uses_login_template(self):
        response = self.client.get('/accounts/login/')
        self.assertTemplateUsed(response, 'accounts/login.html')


class UserCreationTest(TestCase):

    def test_uses_user_creation_template(self):
        response = self.client.get('/accounts/create_account')
        self.assertTemplateUsed(response, 'accounts/create_account.html')

    def test_uses_user_creation_form(self):
        response = self.client.get('/accounts/create_account')
        self.assertIsInstance(response.context['form'], CustomUserCreationForm)

    def test_can_save_a_POST_request(self):
        self.client.post('/accounts/create_account', data={
            'username': 'jjazz',
            'name': 'Jimmy Jazz',
            'email': 'jimmy.jazz@coolguy.com',
            'password1': 'youneverknow8',
            'password2': 'youneverknow8'
        })
        self.assertEqual(get_user_model().objects.count(), 1)
        new_user = get_user_model().objects.first()
        self.assertEqual(new_user.username, 'jjazz')
        self.assertEqual(new_user.name, 'Jimmy Jazz')
        self.assertEqual(new_user.email, 'jimmy.jazz@coolguy.com')
