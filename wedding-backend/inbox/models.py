from random import choices
from secrets import choice
from tabnanny import check
from django.db import models
from django.contrib.auth.models import User
from shared.models import (
    Serializable, Named, TimeStampable,
    HasContent, get_translated_content, 
)

MESSAGE_TYPES = (
    (0, "Information"),
    (1, "Question"),
)

QUESTION_TYPES = (
    (0, "Freetext"),
    (1, "SingleSelect"),
    (2, "MultiSelect"),
    (3, "SingleSelectOther"),
    (4, "MultiSelectOther"),
)

class Message(Serializable, HasContent):
    "Model to define generic messages to users"
    type = models.IntegerField(choices=MESSAGE_TYPES, default=0)
    def __str__(self) -> str:
        return f"{self.content}"
    
class Question(Serializable, HasContent):
    "Model to define questions for users"
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name='questions',
    )
    type = models.IntegerField(choices=QUESTION_TYPES, default=0)
    mandatory = models.BooleanField(default=True)
    def __str__(self) -> str:
        return f"{self.message} - {self.content}"
    
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

class Response(Serializable, TimeStampable):
    "Model to capture the response from a specific user"
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='responses'
    )
    option = models.ManyToManyField(
        Option,
        blank=True,
    )
    text = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s reply to {self.question.name}"
    

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'question'],
                name='unique_user_response',
            ),
        ]
