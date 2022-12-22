from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIRequestFactory, force_authenticate

from .serializers import SubscriptionSerializer
from .viewsets import SubscriptionViewset
from .models import Subscription, Keys


class TestSubscriptionViewset(TestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.user = get_user_model().objects.create(username='testuser')
        self.keys = Keys.objects.create(
            p256dh='12345abcd',
            auth='54321dcba',
        )
        self.sub = Subscription.objects.create(
            user=self.user,
            keys=self.keys,
            user_agent='someAgent',
            endpoint='https://mock.com'
        )

    def test_get_subscriptions(self) -> None:
        request = self.factory.get(reverse('profile:subscription-list'))
        request.META['HTTP_USER_AGENT'] = 'someAgent'
        force_authenticate(request, self.user)
        response = SubscriptionViewset.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)
        sub_dict = SubscriptionSerializer().to_representation(self.sub)
        self.assertIn(sub_dict, response.data)

    def test_get_subscriptions_no_user_agent(self) -> None:
        request = self.factory.get(reverse('profile:subscription-list'))
        request.META['HTTP_USER_AGENT'] = 'someOtherAgent'
        force_authenticate(request, self.user)
        response = SubscriptionViewset.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)
        sub_dict = SubscriptionSerializer().to_representation(self.sub)
        self.assertNotIn(sub_dict, response.data)

    def test_post_subscription(self) -> None:
        request = self.factory.post(
            reverse('profile:subscription-list'),
            {
                "endpoint": "https://test.endpoint.com",
                "keys": {
                    "p256dh": "test256DiffieHellman",
                    "auth": "someAuthKey"
                }
            },
            format='json'
        )
        request.META['HTTP_USER_AGENT'] = 'testUserAgent'
        force_authenticate(request, self.user)
        response = SubscriptionViewset.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 201)
        sub = Subscription.objects.filter(
            user=self.user,
            user_agent='testUserAgent',
            endpoint='https://test.endpoint.com',
        ).first()
        self.assertIsInstance(sub, Subscription)
