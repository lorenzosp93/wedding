from django.db import models
from shared.models import (
    TimeStampable,
    Deactivate,
)
from wedding.settings import AUTH_USER_MODEL

# Create your models here.


class Entry(TimeStampable, Deactivate):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    text = models.TextField(max_length=280)

    class Meta:
        ordering = ['-pk']
