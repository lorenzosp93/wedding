from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory, force_authenticate
from .models import UserProfile
from .views import register_user, setup_plus_one


class TestPlusOneView(TestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.user = get_user_model().objects.create(
            username='some@email.com',
            first_name='someFirstName',
            last_name='someLastName',
            email='some@email.com'
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            plus=1,
        )

    def test_setup_plus_one(self) -> None:
        request = self.factory.post(reverse('profile:setup-plus-one'), {
            "first_name": "a",
            "last_name": "b c",
            "email": "a@b.com",
        })
        force_authenticate(request, self.user)
        response = setup_plus_one(request)
        self.assertEqual(response.status_code, 201)

    def test_setup_plus_one_user_exists(self) -> None:
        request = self.factory.post(reverse('profile:setup-plus-one'), {
            "first_name": "a",
            "last_name": "b",
            "email": "some@email.com",
        })
        force_authenticate(request, self.user)
        response = setup_plus_one(request)
        self.assertEqual(response.status_code, 400)
        non_field_errors = response.data.get('non_field_errors')
        self.assertIsNotNone(non_field_errors)
        self.assertIn('some@email.com', non_field_errors)

    def test_setup_plus_one_no_plusone(self) -> None:
        self.profile.plus = 0
        self.profile.save()
        request = self.factory.post(reverse('profile:setup-plus-one'), {
            "first_name": "a",
            "last_name": "b c",
            "email": "a@b.com",
        })
        force_authenticate(request, self.user)
        response = setup_plus_one(request)
        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.data.get('non_field_errors'))

    def test_setup_plus_one_errors(self) -> None:
        request = self.factory.post(reverse('profile:setup-plus-one'), {
            "first_name": "a",
            "last_name": "b c",
            "email": "a@b",
        })
        force_authenticate(request, self.user)
        response = setup_plus_one(request)
        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.data.get('email'))


class TestRegisterUserView(TestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.user = get_user_model().objects.create(
            username='someUser',
            first_name='someFirstName',
            last_name='someLastName',
            email=''
        )

    def test_register_user(self) -> None:
        request = self.factory.post(
            reverse('profile:register-user'),
            {
                "first_name": "someFirstName",
                "last_name": "someLastName",
                "email": "some@email.com",
            }
        )
        response = register_user(request)
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.user.email, 'some@email.com')
        self.assertEqual(self.user.username, 'some@email.com')

    def test_reguster_user_already_exist(self) -> None:
        self.user.email = 'some@email.com'
        self.user.save()
        request = self.factory.post(
            reverse('profile:register-user'),
            {
                "first_name": "someFirstName",
                "last_name": "someLastName",
                "email": "some@email.com",
            }
        )
        response = register_user(request)
        self.assertEqual(response.status_code, 200)

    def test_register_user_errors(self) -> None:
        request = self.factory.post(
            reverse('profile:register-user'),
            {
                "first_name": "someFirstName",
                "last_name": "someLastName",
                "email": "",
            }
        )
        response = register_user(request)
        self.assertEqual(response.status_code, 400)
        self.assertIsNotNone(response.data.get('email'))
