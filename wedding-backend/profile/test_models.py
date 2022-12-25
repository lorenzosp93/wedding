from unittest.mock import Mock, patch
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Keys, Subscription, UserProfile

# Create your tests here.


class TestProfileModels(TestCase):
    def setUp(self) -> None:
        username = 'someuser'
        email = 'some@email.com'
        self.user = get_user_model().objects.create(
            username=username,
            email=email,
        )
        self.profile = UserProfile.objects.create(user=self.user)
        self.profile.language = 'it'
        self.profile.plus = 3
        self.profile.save()
        self.keys = Keys.objects.create(
            p256dh='BLc4xRzKlKORKWlbdgFaBrrPK3ydWAHo4M0gs0i1oEKgPpWC5cW8OCzVrOQRv-1npXRWk8udnW3oYhIO4475rds=',
            auth='5I2Bu2oKdyy9CwL8QVF0NQ=='
        )
        self.subscription = Subscription.objects.create(
            user=self.user,
            endpoint='',
            keys=self.keys,
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15'
        )

    def test_profile_creation(self) -> None:
        self.assertIsInstance(self.profile, UserProfile)

    def test_profile_update(self) -> None:
        self.assertEqual(self.profile.language, 'it')
        self.assertEqual(self.profile.plus, 3)

    def test_subscription_creation(self) -> None:
        self.assertIsInstance(self.subscription, Subscription)
        self.assertIsInstance(self.keys, Keys)

    @patch('wedding.tasks.send_email.delay')
    def test_setup_plus_one(self, send_email: Mock) -> None:
        self.plus_one, created = self.profile.setup_plus_one(
            first_name='some name',
            last_name='some last name',
            email='someother@email.com',
        )
        self.assertTrue(created)
        self.assertIsInstance(self.plus_one, get_user_model())
        if self.plus_one:
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
            send_email.assert_called_once()
