from random import choices
from secrets import choice
from tabnanny import check
from django.db import models
from django.contrib.auth.models import User
from shared.models import (
    Serializable, TimeStampable,
    HasContent, HasSubject, 
)


class Message(Serializable, HasSubject, HasContent, TimeStampable):
    "Model to define generic messages to users"
    def __str__(self) -> str:
        return f"{self.subject}"

    class Meta:
        ordering = ['-created_at']
    
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
        return f"{self.user}'s reply to {self.question.subject}"
    
    class Meta:
        unique_together = ['question', 'user']
    

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'question'],
                name='unique_user_response',
            ),
        ]
