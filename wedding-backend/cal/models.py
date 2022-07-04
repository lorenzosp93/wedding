from django.db import models
from django.contrib.auth.models import User
from shared.models import (
    Named, Serializable, Datable, Localizable, HasPicture, HasContent
)

# Create your models here.
class Event(Named, Serializable, Datable, Localizable, HasPicture, HasContent):
    pass

class RSVP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    response = models.BooleanField()

    class Meta:
        constraints = [
            models.constraints.UniqueConstraint(
                fields=('event', 'user'),
                name='unique_user_event',
            )
        ]

