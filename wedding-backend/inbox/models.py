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

)

class Message(Serializable, Named, HasContent):
    "Model to define generic messages to users"
    type = models.IntegerField(choices=MESSAGE_TYPES, default=0)
    
class Question(Serializable, Named, HasContent):
    "Model to define questions for users"
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name='questions',
    )
    type = models.IntegerField(choices=QUESTION_TYPES, default=0)
    mandatory = models.BooleanField(default=True)

    def get_content(self, language) -> str:
        return get_translated_content(self.content, language)
    
    def get_options(self, language) -> list:
        return [option.get_content(language) for option in self.options.all()]

class Option(Named, HasContent):
    """Model to define selectable options for questions - 'Other' 
    option is omitted for SingleSelectOther questions"""
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='options',
    )

    def get_content(self, language):
        return get_translated_content(self.content, language)

class UserMessage(Serializable):
    "Model to define a message to a specific user"
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    @property
    def language(self) -> str:
        return self.user.extended.language
    
    @property
    def get_message_content(self) -> str:
        return {
            'content': get_translated_content(
                content=self.message.content,
                language=self.language,
            ),
            'type': self.message.type,
        }
    
    @property
    def get_questions_content(self) -> dict:
        return {
            q.get_content(self.language): {
                'options': q.get_options(self.language),
                'type': q.type,
                'mandatory': q.mandatory,
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
    
class Response(TimeStampable):
    "Model to capture the response from a specific user"
    option = models.ManyToManyField(
        Option,
        blank=True,
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='responses'
    )
    text = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'question'],
                name='unique_user_response',
            ),
        ]
