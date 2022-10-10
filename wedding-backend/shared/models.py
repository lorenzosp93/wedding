"Define abstract models to be used in all apps"
from unittest.util import _MAX_LENGTH
import uuid
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Address(models.Model):
    "Model to capture an address from a user"
    address1 = models.TextField(max_length=128)
    address2 = models.TextField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=10)
    province_or_state = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=20)

class Serializable(models.Model):
    "Abstract model to define an uuid based id field"
    uuid = models.UUIDField(
        editable=False,
        default=uuid.uuid4,
    )

    class Meta:
        abstract = True

class Named(models.Model):
    "Abstract model to define names and slug behavior"
    name = models.CharField(max_length=90, unique=True)
    slug = models.SlugField(max_length=100, editable=False)

    def save(self, **kwargs): # pylint: disable=W0221
        "Override save method to create slug from name"
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(**kwargs)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class TimeStampable(models.Model):
    "Abstract model to define timestamps for the entries"
    created_at = models.DateTimeField(
        verbose_name="Created date",
        auto_now_add=True,
        editable=False,
    )
    modified_at = models.DateTimeField(
        verbose_name="Last modified date",
        auto_now=True,
        editable=False,
    )

    class Meta:
        abstract = True
        ordering = ['-created_at']

class Datable(models.Model):
    "Abstract model to define dates for the entries"
    start_date = models.DateTimeField(
        verbose_name="Start date"
    )
    end_date = models.DateTimeField(
        verbose_name="End date",
        blank=True,
        null=True,
    )

    def save(self, **kwargs): # pylint: disable=W0221
        "Override save method to validate end date"
        if self.end_date:
            self.end_date_validation()
        self.start_date_validation()
        super().save(**kwargs)

    def end_date_validation(self):
        if self.end_date <= self.start_date:
            raise ValidationError(
                "End date: %(end)s cannot be before start date: %(start)s",
                params={"end": self.end_date, "start": self.start_date},
            )
        elif self.end_date > timezone.now().date():
            raise ValidationError(
                "End date: %(end)s cannot be in the future",
                params={"end": self.end_date},
            )

    class Meta:
        abstract = True

class Location(Named,):
    url = models.URLField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=17, decimal_places=15,blank=True, null=True)
    longitude = models.DecimalField(max_digits=17, decimal_places=15,blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)

class Localizable(models.Model):
    "Abstract model to define locations"
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True

class Described(models.Model):
    "Abstract model to define descriptions"
    description = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class Attachment(Named, Serializable):
    "Concrete model to define attachments"
    file = models.FileField(
        upload_to='attachments/',
        verbose_name="File",
    )

class Attachable(models.Model):
    "Abstract model to allow attachments"
    attachments = models.ManyToManyField(
        Attachment,
        verbose_name="attachment",
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        blank=True,
    )

    class Meta:
        abstract = True

class Authorable(models.Model):
    "Abstract model to describe the author"
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User,
        verbose_name="Created by",
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related_creator",
        related_query_name="%(app_label)s_%(class)s_created",
        editable=False,
    )
    modified_by = models.ForeignKey(
        User,
        verbose_name="Last modified by",
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related_modifier",
        related_query_name="%(app_label)s_%(class)s_modified",
        editable=False,
    )

class HasPicture(models.Model):
    "Abstract class to capture a picture"
    picture = models.ImageField(
        verbose_name='Header picture',
        upload_to="pictures/",
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class SingletonBaseModel(models.Model):
    "Abstract class to implement the singleton design pattern"
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class SiteSetting(SingletonBaseModel):
    "Concrete model for the settings for the website"
    about_text = models.TextField()

I18N = (
    (0, 'en'),
    (1, 'it'),
    (2, 'es'),
)


class ContentString(Named):
    """
        Model to define a string of content
    """

class TranslatedString(models.Model):
    "Model to define translations for a `ContentString`"
    language = models.IntegerField(choices=I18N)
    t9n = models.TextField()
    content = models.ForeignKey(
        ContentString,
        on_delete=models.CASCADE,
        related_name='translated_strings'
    )
    def __str__(self) -> str:
        return f'{self.content.name} -> {self.get_language_display()}'

def get_translated_content(content: ContentString, language: str = 0) -> str:
    "Helper function to return the translated string for a given content and language"
    if (translated_str := content.translated_strings.filter(language=language).first()):
        return translated_str.t9n
    return content.name

class HasContent(models.Model):
    "Abstract class to define content"
    content = models.ForeignKey(ContentString, on_delete=models.CASCADE)

    class Meta:
        abstract = True
