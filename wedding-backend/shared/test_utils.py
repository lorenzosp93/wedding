from unittest.mock import patch, Mock
from django.test import TestCase
from django.contrib.auth.models import User
from drfpasswordless.utils import create_callback_token_for_user
from profile.models import UserProfile
from .utils import send_email_with_callback_token

class TestSendEmailWithCallback(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username='test_user',
            email='test@email.com',
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            language='it',
        )
        self.otp = create_callback_token_for_user(self.user, 'email', 'AUTH')
    
    @patch('wedding.tasks.send_email.delay')
    def test_send_email_with_callback(self, send_email_delay:Mock) -> None:
        send_email_with_callback_token(
            self.user,
            self.otp,
        )
        send_email_delay.assert_called()