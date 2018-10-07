from django.test import TestCase

from bands.models import CustomUser


class CustomUserModelTest(TestCase):

    def test_saving_and_retrieving_users(self):
        user = CustomUser()
        user.username = 'jjazz'
        user.first_name = 'Jimmy Jazz'
        user.email = 'jimmy.jazz@coolguy.com'
