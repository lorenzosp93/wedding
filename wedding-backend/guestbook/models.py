from django.db import models
from shared.models import (
    TimeStampable,
    Deactivate,
    Serializable
)
from wedding.settings import AUTH_USER_MODEL

# Create your models here.


class Entry(Serializable, TimeStampable, Deactivate):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    text = models.TextField(max_length=280,)

    def __str__(self) -> str:
        return f"{self.user} - {self.text}"

    class Meta:
        ordering = ['-created_at']
