from datetime import timedelta
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory
from .authentication import ExpiringTokenAuthentication
from wedding.settings import TOKEN_EXPIRED_AFTER_SECONDS
from rest_framework.exceptions import AuthenticationFailed


class TestAuthentication(TestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.auth = ExpiringTokenAuthentication()
        self.user = get_user_model().objects.create(username='testUser')
        self.token = Token.objects.create(
            key=Token.generate_key(),
            user=self.user,
        )
        self.request = self.factory.get(reverse('profile:profile-list'))
        self.request.META['HTTP_AUTHORIZATION'] = f"Token {self.token.key}"

    def test_token_new(self) -> None:
        user, token = self.auth.authenticate((self.request))
        self.assertEqual(self.user, user)
        self.assertEqual(self.token, token)

    def test_token_expired(self) -> None:
        self.token.created -= timedelta(
            seconds=TOKEN_EXPIRED_AFTER_SECONDS + 10,
        )
        self.token.save()
        with self.assertRaises(AuthenticationFailed):
            self.auth.authenticate_credentials(self.request)
