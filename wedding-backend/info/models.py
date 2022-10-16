from django.db import models
from django.contrib.auth.models import User
from shared.models import (
    Named, HasPicture, HasContent, HasSubject
)

INFO_TYPES = (
    (0, 'Venues'),
    (1, 'Food'),
    (2, 'Attractions'),
    (3, 'Tips'),
    (4, 'Travel'),
    (5, 'Events'),
)

# Create your models here.
class Information(HasPicture, HasContent, HasSubject):
    type = models.IntegerField(choices=INFO_TYPES,)

    def __str__(self) -> str:
        return f"{self.subject}"

class Photo(Named, HasPicture):
    tag = models.ManyToManyField(User, blank=True,)
    private = models.BooleanField(default=False,)
