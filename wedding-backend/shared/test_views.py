# type: ignore
from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.module_loading import import_string
from drfpasswordless.settings import api_settings
from drfpasswordless.utils import create_callback_token_for_user
from wedding.settings import FRONTEND_HOST
from .views import get_auth_token

# Create your tests here.


class TestSharedViews(TestCase):
    """
    Class to test the shared views
    """

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.email = 'some@email.com'
        user = get_user_model().objects.create(
            username='test_user',
            email=self.email
        )
        token_creator = import_string(
            api_settings.PASSWORDLESS_AUTH_TOKEN_CREATOR)
        (self.authToken, _) = token_creator(user)
        self.otp = create_callback_token_for_user(user, 'email', 'AUTH')

    def test_get_auth_token(self) -> None:
        request = self.factory.get(
            f"{reverse('shared:magic-auth')}?email={self.email}&token={self.otp}"
        )
        response = get_auth_token(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url, f"{FRONTEND_HOST}/?token={self.authToken}")
