from datetime import date
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse
from rest_framework.test import force_authenticate
from .models import (
    Message,
    Response,
    Question,
    Option,
)
from .serializers import MessageSerializer
from .viewsets import (MessageViewSet, ResponseViewSet)
from shared.models import ContentString
from profile.models import UserProfile

# Create your tests here.


class TestInboxViewsets(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create(username='testuser')
        UserProfile.objects.create(user=self.user)
        self.message = Message.objects.create(
            subject=ContentString.objects.create(value='something'),
        )
        self.question = Question.objects.create(
            message=self.message,
            subject=ContentString.objects.create(value='else'),
        )
        self.option = Option.objects.create(
            question=self.question,
            content=ContentString.objects.create(value='opt1')
        )

        self.factory = RequestFactory()
        self.request = self.factory.get(reverse('inbox:message-list'))
        force_authenticate(self.request, self.user)

    def test_queryset_audience_all(self) -> None:
        response = MessageViewSet.as_view({'get': 'list'})(self.request)
        serialized_obj = MessageSerializer(
            context={'request': self.request}
        ).to_representation(self.message)
        self.assertIn(serialized_obj, response.data)

    def test_queryset_audience_not_in(self) -> None:
        new_message = Message.objects.create(
            subject=ContentString.objects.create(value='2'),
            audience=15
        )
        response = MessageViewSet.as_view({'get': 'list'})(self.request)
        serialized_obj = MessageSerializer(
            context={'request': self.request}
        ).to_representation(new_message)
        self.assertNotIn(serialized_obj, response.data)
        new_user = get_user_model().objects.create(username='new')
        UserProfile.objects.create(user=new_user, type=3)
        new_request = self.factory.get(reverse('inbox:message-list'))
        force_authenticate(new_request, new_user)
        new_response = MessageViewSet.as_view({'get': 'list'})(new_request)
        self.assertIn(serialized_obj, new_response.data)

    def test_prerequisite_message(self) -> None:
        response = Response.objects.create(
            question=self.question,
            user=self.user,
        )
        response.option.add(self.option)
        new_message = Message.objects.create(
            subject=ContentString.objects.create(value='3'),
            audience=30,
        )
        new_message.option_pre.add(self.option)
        new_message.option_pre.add(self.option)
        response = MessageViewSet.as_view({'get': 'list'})(self.request)
        serialized_obj = MessageSerializer(
            context={'request': self.request}
        ).to_representation(new_message)
        self.assertIn(serialized_obj, response.data)
        new_user = get_user_model().objects.create(username='new')
        UserProfile.objects.create(user=new_user)
        new_request = self.factory.get(reverse('inbox:message-list'))
        force_authenticate(new_request, new_user)
        new_response = MessageViewSet.as_view({'get': 'list'})(new_request)
        self.assertNotIn(serialized_obj, new_response.data)

    def test_response_submit(self) -> None:
        request = self.factory.post(
            reverse('inbox:response-list'),
            {
                "question": self.question.uuid,
                "option": [self.option.uuid],
                "text": "someText",
            }
        )
        force_authenticate(request, self.user)
        response = ResponseViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 201)
        created_response = Response.objects.get(
            user=self.user,
            question=self.question,
        )
        self.assertIsInstance(created_response, Response)
        self.assertEqual(created_response.question, self.question)
        self.assertIn(self.option, created_response.option.all())
        self.assertEqual(created_response.text, 'someText')

    def test_response_errors_options(self) -> None:
        request = self.factory.post(
            reverse('inbox:response-list'),
            {
                "question": self.question.uuid,
                "option": [],
                "text": "",
            }
        )
        force_authenticate(request, self.user)
        response = ResponseViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 400)
        self.assertIn("option", response.data)

    def test_response_errors_text_options(self) -> None:
        self.question.free_text = True
        self.question.save()
        request = self.factory.post(
            reverse('inbox:response-list'),
            {
                "question": self.question.uuid,
                "option": [],
                "text": "",
            }
        )
        force_authenticate(request, self.user)
        response = ResponseViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 400)
        self.assertIn("text", response.data)

    def test_response_errors_text(self) -> None:
        question = Question.objects.create(
            subject=ContentString.objects.create(value='someQ'),
            message=self.message,
            free_text=True,
        )
        request = self.factory.post(
            reverse('inbox:response-list'),
            {
                "question": question.uuid,
                "option": [],
                "text": "",
            }
        )
        force_authenticate(request, self.user)
        response = ResponseViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 400)
        self.assertIn("text", response.data)

    def test_response_delete(self) -> None:
        self.response = Response.objects.create(
            user=self.user,
            question=self.question
        )
        self.response.option.add(self.option)
        request = self.factory.delete(
            reverse('inbox:response-detail', [self.response.uuid])
        )
        force_authenticate(request, self.user)
        response = ResponseViewSet.as_view(
            {'delete': 'destroy'})(request, pk=self.response.uuid)
        self.response.refresh_from_db()
        self.assertEqual(response.status_code, 204)
        self.assertFalse(self.response.active)
        self.assertIsInstance(self.response.deleted_at, date)
