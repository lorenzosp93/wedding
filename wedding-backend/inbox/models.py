from django.db import models
from django.contrib.auth.models import User
from shared.models import (
    Serializable, Named, TimeStampable,
)
I18N = (
    (1, 'en'),
    (2, 'it'),
    (3, 'es'),
)
# Create your models here.
class ContentString(Named):
    pass

class TranslatedString(models.Model):
    language = models.IntegerField(choices=I18N)
    string = models.TextField()

class Message(Serializable, Named):
    content = models.ForeignKey(ContentString, on_delete=models.CASCADE)

class Question(Serializable, Named):
    content = models.ForeignKey(ContentString, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

class Option(Named):
    content = models.ForeignKey(ContentString, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Response(TimeStampable):
    option = models.ForeignKey(Option, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
