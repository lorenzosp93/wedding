from django.db import models
from django.contrib.auth.models import User
from shared.models import (
    Serializable, Named, TimeStampable,
    ContentString, HasContent, get_translated_content
)


class Message(Serializable, Named, HasContent):
    "Model to define generic messages to users"
    
class Question(Serializable, Named, HasContent):
    "Model to define questions for users"
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name='questions',
    )
    isMultiSelect = models.BooleanField()

    def get_content(self, language) -> str:
        return get_translated_content(self.content, language)
    
    def get_options(self, language) -> list:
        return [option.get_content(language) for option in self.options.all()]

class Option(Named, HasContent):
    "Model to define selectable options for questions"
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
    isRead = models.BooleanField(default=False)

    @property
    def language(self) -> str:
        return self.user.extended.language
    
    @property
    def get_message_content(self) -> str:
        return get_translated_content(
            content=self.message.content,
            language=self.language
        )
    
    @property
    def get_questions_content(self) -> dict:
        return {
            q.get_content(self.language): {
                'options': q.get_options(self.language),
                'isMultiSelect': q.isMultiSelect,
            }
            for q in self.message.questions.all()
        }
    
    def read(self):
        self.read = True
    
    @property
    def isReplied(self) -> bool:
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
