from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from shared.models import (
    HasPicture, HasContent, HasSubject
)
from profile.models import audience_types

INFO_TYPES = (
    (0, _('Venues')),
    (1, _('Food')),
    (2, _('Attractions')),
    (3, _('Tips')),
    (4, _('Travel')),
    (5, _('Events')),
)

PHOTO_TYPES = (
    (0, _('Ice-breaker')),
    (1, _('Ceremony')),
    (2, _('Reception')),
    (3, _('Dinner')),
    (4, _('Dance')),
    (5, _('Before')),
)

# Create your models here.


class Information(HasPicture, HasContent, HasSubject):
    type = models.IntegerField(choices=INFO_TYPES,)
    audience = models.IntegerField(choices=audience_types, default=30)

    def __str__(self) -> str:
        return f"{self.subject}"


class Photo(HasPicture):
    tag = models.ManyToManyField(User, blank=True,)
    private = models.BooleanField(default=False,)
    type = models.IntegerField(choices=PHOTO_TYPES,)
