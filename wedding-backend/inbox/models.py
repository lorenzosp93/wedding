from django.db import models
from django.contrib.auth.models import User
from shared.models import (
    Serializable, Named, TimeStampable,
)
I18N = (
    (0, 'en'),
    (1, 'it'),
    (2, 'es'),
)
USER_TYPES = (
    (0, 'family'),
    (1, 'friend'),
    (2, 'colleague')
)

class UserExtended(User):
    language = models.IntegerField(choices=I18N)
    type = models.IntegerField(choices=USER_TYPES)

# Create your models here.
class ContentString(Named):
    pass

class TranslatedString(models.Model):
    language = models.IntegerField(choices=I18N)
    string = models.TextField()
    content = models.ForeignKey(ContentString, on_delete=models.CASCADE)

class Message(Serializable, Named):
    content = models.ForeignKey(TranslatedString, on_delete=models.CASCADE)

class UserMessage(Serializable):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    recipient = models.ForeignKey(UserExtended, on_delete=models.CASCADE)

class Question(Serializable, Named):
    content = models.ForeignKey(TranslatedString, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

class Option(Named):
    content = models.ForeignKey(TranslatedString, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Response(TimeStampable):
    option = models.ForeignKey(Option, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
