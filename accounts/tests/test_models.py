from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

User = get_user_model()


class CustomUserModelTest(TestCase):

    def test_saving_and_retrieving_users(self):
        user = User()
        user.username = 'jjazz'
        user.name = 'Jimmy Jazz'
        user.email = 'jimmy.jazz@coolguy.com'
        user.password = 'youneverknow8'
        user.save()

        new_user = User.objects.first()
        self.assertEqual(user, new_user)

    def test_cannot_save_without_email(self):
        user = User()
        user.username = 'jjazz'
        user.name = 'Jimmy Jazz'
        user.password = 'youneverknow8'
        with self.assertRaises(ValidationError):
            user.save()
            user.full_clean()

    def test_cannot_have_duplicate_email(self):
        user1 = User()
        user1.username = 'user1'
        user1.name = 'User One'
        user1.password = 'IAmTheFirstUser'
        user1.email = 'user@domain.com'
        user1.save()
        user1.full_clean()

        user2 = User()
        user2.username = 'user2'
        user2.name = 'User Two'
        user2.password = 'IAmTheSecondUser'
        user2.email = 'user@domain.com'
        with self.assertRaises(IntegrityError):
            user2.save()
            user2.full_clean()