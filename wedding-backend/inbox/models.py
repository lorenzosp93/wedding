from itertools import chain
from django.apps import apps
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from wedding.settings import AUTH_USER_MODEL
from shared.models import (
    Serializable, TimeStampable,
    HasContent, HasSubject, Deactivate
)
from shared.advanced_models import (
    HasAudience, HasUserList,
    TriggersNotifications,
)


class HasPrerequisiteOptions(HasUserList):
    option_pre: models.Field = models.ManyToManyField(
        'Option', blank=True
    )

    def get_users(self) -> models.QuerySet[AbstractBaseUser]:
        if self.option_pre.count() > 0:
            return super().get_users().filter(
                pk__in=self.get_user_list_pre()
            )
        return super().get_users()

    def get_user_list_pre(self) -> list[str]:
        return list(chain.from_iterable([
            [*apps.get_model('inbox', 'Response').objects.filter(
                option=option,
                active=True,
            ).values_list('user__pk', flat=True)]
            for option in self.option_pre.all()
        ]))

    class Meta:
        abstract = True


class Message(
    TriggersNotifications,  HasPrerequisiteOptions,
    HasAudience, Serializable, HasContent, TimeStampable
):
    "Model to define generic messages to users"

    def __str__(self) -> str:
        return f"{self.subject}"

    class Meta:
        ordering = ['pk']


class Question(Serializable, HasSubject, HasContent):
    "Model to define questions for users"
    message: models.Field = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name='questions',
    )
    multi_select: models.Field = models.BooleanField(default=False)
    free_text: models.Field = models.BooleanField(default=False)
    mandatory: models.Field = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.message} - {self.subject}"

    class Meta:
        ...


class Option(Serializable, HasContent):
    """Model to define selectable options for questions - 'Other' 
    option is omitted for SingleSelectOther or MultiSelectOther questions"""
    question: models.Field = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='options',
    )

    class Meta:
        ...

    def __str__(self) -> str:
        return f"{self.question} - {self.content}"


class Response(Serializable, TimeStampable, Deactivate):
    "Model to capture the response from a specific user"
    question: models.Field = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='responses'
    )
    option: models.Field = models.ManyToManyField(
        Option,
        blank=True,
    )
    text: models.Field = models.TextField(null=True, blank=True)
    user: models.Field = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user}'s reply to {self.question.subject}"

    def get_options(self) -> str:
        return ",\n".join([o.content.value for o in self.option.all()])

    class Meta:
        unique_together = ['question', 'user', 'active', 'deleted_at']
        ordering = ['-pk']
