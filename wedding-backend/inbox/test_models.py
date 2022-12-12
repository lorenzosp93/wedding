from django.test import TestCase
from django.contrib.auth import get_user_model
from shared.models import ContentString
from profile.models import UserProfile
from .models import Message, Response, Option, Question


class TestInboxModels(TestCase):
    """
        Class to test inbox models.
    """

    def setUp(self):
        self.user = get_user_model().objects.create(username="TestUser")
        UserProfile.objects.create(
            user=self.user,
            type=2,  # family
        )
        self.message = Message.objects.create(
            subject=ContentString.objects.create(value='sub'),
            content=ContentString.objects.create(value='cont'),
            audience=30,
        )
        self.question = Question.objects.create(
            message=self.message,
            subject=ContentString.objects.create(value='qst')
        )
        self.option = Option.objects.create(
            question=self.question,
            content=ContentString.objects.create(value='opt1')
        )
        self.new_user = get_user_model().objects.create(username="NewTestUser")
        UserProfile.objects.create(
            user=self.new_user,
            type=3,  # friend
        )
        self.new_message = Message.objects.create(
            subject=ContentString.objects.create(value='sub1'),
            content=ContentString.objects.create(value='cont'),
            audience=15,  # friends & colleagues
        )

    def test_has_audience_user_list(self):
        message_user_list = self.message.get_users()
        new_message_user_list = self.new_message.get_users()
        self.assertIn(self.user, message_user_list)
        self.assertIn(self.new_user, message_user_list)
        self.assertIn(self.new_user, new_message_user_list)
        self.assertNotIn(self.user, new_message_user_list)

    def test_option_prereq_user_list(self):
        self.message.option_pre.add(self.option)
        response = Response.objects.create(
            user=self.new_user,
            question=self.question,
            active=True,
        )
        response.option.add(self.option)
        message_user_list = self.message.get_users()
        self.assertIn(self.new_user, message_user_list)
        self.assertNotIn(self.user, message_user_list)
