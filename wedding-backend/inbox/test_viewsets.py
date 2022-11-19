from django.test import TestCase
from django.test.client import RequestFactory
from rest_framework.reverse import reverse
from rest_framework.test import force_authenticate
from .models import (
    Message,
    Response,
    Question,
    Option,
)
from .serializers import MessageSerializer
from .viewsets import MessageViewSet
from shared.models import ContentString
from profile.models import UserProfile, User

# Create your tests here.


class TestInboxViewsets(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        UserProfile.objects.create(user=self.user)
        self.message = Message.objects.create(
            subject=ContentString.objects.create(value='something'),
        )
        self.question = Question.objects.create(
            message=self.message,
            subject=ContentString.objects.create(value='else')
        )
        self.option = Option.objects.create(
            question=self.question,
            content=ContentString.objects.create(value='opt1')
        )

        self.factory = RequestFactory()
        self.request = self.factory.get(reverse('inbox:message-list'))
        force_authenticate(self.request, self.user)

    def test_queryset_audience_all(self):
        response = MessageViewSet.as_view({'get': 'list'})(self.request)
        serialized_obj = MessageSerializer(
            context={'request': self.request}
        ).to_representation(self.message)
        self.assertIn(serialized_obj, response.data)

    def test_queryset_audience_not_in(self):
        new_message = Message.objects.create(
            subject=ContentString.objects.create(value='2'),
            audience=15
        )
        response = MessageViewSet.as_view({'get': 'list'})(self.request)
        serialized_obj = MessageSerializer(
            context={'request': self.request}
        ).to_representation(new_message)
        self.assertNotIn(serialized_obj, response.data)
        new_user = User.objects.create(username='new')
        UserProfile.objects.create(user=new_user, type=3)
        new_request = self.factory.get(reverse('inbox:message-list'))
        force_authenticate(new_request, new_user)
        new_response = MessageViewSet.as_view({'get': 'list'})(new_request)
        self.assertIn(serialized_obj, new_response.data)

    def test_prerequisite_message(self):
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
        new_user = User.objects.create(username='new')
        UserProfile.objects.create(user=new_user)
        new_request = self.factory.get(reverse('inbox:message-list'))
        force_authenticate(new_request, new_user)
        new_response = MessageViewSet.as_view({'get': 'list'})(new_request)
        self.assertNotIn(serialized_obj, new_response.data)
