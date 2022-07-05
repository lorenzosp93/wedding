from django.db import models
from shared.models import (
    Named, HasPicture, HasContent
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
    type = models.IntegerField(choices=INFO_TYPES,)

class Photo(Named, HasPicture):
    pass
