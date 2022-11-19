from operator import truediv
from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

# Create your tests here.


class TestProfileModels(TestCase):
    def setUp(self):
        username = 'someuser'
        email = 'some@email.com'
        self.user = User.objects.create_user(
            username=username,
            email=email
        )
        self.profile = UserProfile.objects.create(user=self.user)
        self.profile.language = 'it'
        self.profile.plus = 3
        self.profile.save()

    def test_profile_creation(self):
        self.assertIsInstance(self.profile, UserProfile)

    def test_profile_update(self):
        self.assertEqual(self.profile.language, 'it')
        self.assertEqual(self.profile.plus, 3)

    def test_setup_plus_one(self):
        self.plus_one, created = self.profile.setup_plus_one(
            first_name='some name',
            last_name='some last name',
            email='someother@email.com',
        )
        self.assertTrue(created)
        self.assertIsInstance(self.plus_one, User)
        self.assertEqual(self.plus_one.email, 'someother@email.com')
        self.assertEqual(
            self.plus_one.profile,
            UserProfile.objects.get(user=self.plus_one)
        )
        self.assertEqual(
            self.plus_one.profile.language,
            self.profile.language
        )
        self.assertEqual(
            self.plus_one.profile.parent,
            self.user
        )
