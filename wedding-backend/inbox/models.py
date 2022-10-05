from random import choices
from secrets import choice
from tabnanny import check
from django.db import models
from django.contrib.auth.models import User
from shared.models import (
    Serializable, Named, TimeStampable,
    HasContent, get_translated_content
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

class Message(Serializable, Named, HasContent):
    "Model to define generic messages to users"
    type = models.IntegerField(choices=MESSAGE_TYPES, default=0)
    
class Question(Serializable, Named):
    "Model to define questions for users"
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name='questions',
    )
    type = models.IntegerField(choices=QUESTION_TYPES, default=0)
    mandatory = models.BooleanField(default=True)
    
    def get_options(self, language=0) -> list:
        return [option.get_content(language) for option in self.options.all()]

class Option(Named, HasContent):
    """Model to define selectable options for questions - 'Other' 
    option is omitted for SingleSelectOther or MultiSelectOther questions"""
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='options',
    )

    def get_content(self, language=0):
        return get_translated_content(self.content, language)

class UserMessage(Serializable, TimeStampable):
    "Model to define a message to a specific user"
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    @property
    def language(self) -> str:
        return self.user.profile.language
    
    @property
    def message_content(self) -> dict:
        return {
            'name': self.message.name,
            'content': get_translated_content(
                content=self.message.content,
                language=self.language,
            ),
            'type': self.message.type,
        }
    
    @property
    def questions_content(self) -> dict:
        return {
            q.message: {
                'type': q.get_type_display(),
                'mandatory': q.mandatory,
                'options': q.get_options(self.language)
            }
            for q in self.message.questions.all()
        }
    
    def read(self):
        self.read = True
    
    @property
    def replied(self) -> bool:
        return all([
            q.responses.filter(user=self.user).count() > 1
            for q in self.message.questions
        ])
    
    def __str__(self) -> str:
        return f"'{self.message}' to '{self.user}'"

    class Meta:
        ordering = ["-created_at"]
    
class Response(TimeStampable):
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
