from django.db import models
from django.contrib.auth.models import User
from shared.models import (
    Named, HasPicture, HasContent, ContentString
)

INFO_TYPES = (
    (0, 'Accomodations'),
    (1, 'Food'),
    (2, 'Attractions'),
    (3, 'Tips'),
    (4, 'Travel')
)

# Create your models here.
class Information(Named, HasPicture, HasContent):
    subject = models.ForeignKey(
        ContentString,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    type = models.IntegerField(choices=INFO_TYPES,)

class Photo(Named, HasPicture):
    tag = models.ManyToManyField(User, blank=True,)
    private = models.BooleanField(default=False,)

