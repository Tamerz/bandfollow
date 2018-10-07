from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm


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
        self.assertIsInstance(response.context['form'], UserCreationForm)
