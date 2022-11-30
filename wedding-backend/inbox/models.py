from django.db import models
from django.contrib.auth.models import User
from shared.models import (
    Serializable, TimeStampable,
    HasContent, HasSubject,
)
from profile.models import audience_types

class Response(Serializable, TimeStampable):
    "Model to capture the response from a specific user"
    question = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE,
        related_name='responses'
    )
    option = models.ManyToManyField(
        'Option',
        blank=True,
    )
    text = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.user}'s reply to {self.question.subject}"

    class Meta:
        unique_together = ['question', 'user', 'active', 'deleted_at']

from shared.mixins import TriggersNotifications

class Message(TriggersNotifications, Serializable, HasSubject, HasContent, TimeStampable):
    "Model to define generic messages to users"
    option_pre = models.ManyToManyField('Option', blank=True)
    audience = models.IntegerField(
        choices=audience_types,
        default=30,
    )

    def __str__(self) -> str:
        return f"{self.subject}"

    class Meta:
        ordering = ['created_at']


class Question(Serializable, HasSubject, HasContent):
    "Model to define questions for users"
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name='questions',
    )
    multi_select = models.BooleanField(default=False)
    free_text = models.BooleanField(default=False)
    mandatory = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.message} - {self.subject}"


class Option(Serializable, HasContent):
    """Model to define selectable options for questions - 'Other' 
    option is omitted for SingleSelectOther or MultiSelectOther questions"""
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='options',
    )

    def __str__(self) -> str:
        return f"{self.question} - {self.content}"
