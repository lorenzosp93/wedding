"Define abstract models to be used in all apps"
from io import BytesIO
import os
import uuid
from PIL import Image
from PIL.ImageOps import exif_transpose
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.html import strip_tags
from wedding.settings import AUTH_USER_MODEL


THUMBNAIL_SIZE = 640, 640
I18N = (
    ('en', _('English')),
    ('it', _('Italian')),
    ('es', _('Spanish')),
)


class Address(models.Model):
    "Model to capture an address from a user"
    address1: models.Field = models.TextField(max_length=128)
    address2: models.Field = models.TextField(
        max_length=128, null=True, blank=True)
    city: models.Field = models.CharField(max_length=20)
    postal_code: models.Field = models.CharField(max_length=10)
    province_or_state: models.Field = models.CharField(
        max_length=10, null=True, blank=True)
    country: models.Field = models.CharField(max_length=20)


class Serializable(models.Model):
    "Abstract model to define an uuid based id field"
    uuid: models.Field = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )

    class Meta:
        abstract = True


class TimeStampable(models.Model):
    "Abstract model to define timestamps for the entries"
    created_at: models.Field = models.DateTimeField(
        verbose_name="Created date",
        auto_now_add=True,
        editable=False,
    )
    modified_at: models.Field = models.DateTimeField(
        verbose_name="Last modified date",
        auto_now=True,
        editable=False,
    )

    class Meta:
        abstract = True
        ordering = ['-created_at']


class Described(models.Model):
    "Abstract model to define descriptions"
    description: models.Field = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class Authorable(models.Model):
    "Abstract model to describe the author"
    active: models.Field = models.BooleanField(default=True)
    created_by: models.Field = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name="Created by",
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related_creator",
        related_query_name="%(app_label)s_%(class)s_created",
        editable=False,
    )
    modified_by: models.Field = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name="Last modified by",
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related_modifier",
        related_query_name="%(app_label)s_%(class)s_modified",
        editable=False,
    )

    class Meta:
        abstract = True


class HasPicture(models.Model):
    "Abstract class to capture a picture"
    picture: models.Field = models.ImageField(
        upload_to="pictures/",
        blank=True,
        null=True,
    )
    thumbnail: models.Field = models.ImageField(
        upload_to="thumb/",
        blank=True,
        null=True,
        editable=False,
    )

    def save(self, *args, **kwargs) -> None:
        if not self.thumbnail and self.picture:
            self.save_thumb()
        return super(HasPicture, self).save(*args, **kwargs)

    def save_thumb(self) -> None:
        with Image.open(self.picture) as img:
            thumb = self.create_thumb(img)
            save_path = f"{os.path.split(self.picture.name)[1]}"
            suf = self.save_img(thumb, save_path)
            self.thumbnail.save(save_path, suf, save=False)

    def create_thumb(self, img: Image.Image) -> Image.Image:
        thumb = exif_transpose(img)
        thumb.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
        return thumb

    def save_img(self, img: Image.Image, save_path: str) -> SimpleUploadedFile:
        with BytesIO() as io:
            img.save(
                io,
                quality=90,
                optimize=True,
                format='png'
            )
            io.seek(0)
            return SimpleUploadedFile(
                save_path,
                content=io.read(),
            )

    class Meta:
        abstract = True


class ContentString(models.Model):
    """
        Model to define a string of content
    """
    value: models.Field = models.TextField()

    def __str__(self) -> str:
        return f"{strip_tags(self.value)} - {self.pk}"


class TranslatedString(models.Model):
    "Model to define translations for a `ContentString`"
    language: models.Field = models.CharField(
        choices=I18N,
        max_length=2,
        default='en',
    )
    t9n: models.Field = models.TextField()
    content: models.Field = models.ForeignKey(
        ContentString,
        on_delete=models.CASCADE,
        related_name='translated_strings'
    )

    class Meta:
        unique_together = ['language', 'content']

    def __str__(self) -> str:
        return f'{strip_tags(self.content.value)} -> {self.language}'


def get_translated_content(
    content: ContentString, language: str = 'en'
) -> str:
    """
        Helper function to return the translated string
        for a given content and language
    """
    if (translated_str := content.translated_strings.filter(
        language=language
    ).first()):
        return translated_str.t9n
    return content.value


class HasContent(models.Model):
    "Abstract class to define content"
    content: models.Field = models.ForeignKey(
        ContentString,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class HasSubject(models.Model):
    "Abstract class to define subject content"
    subject: models.Field = models.ForeignKey(
        ContentString,
        on_delete=models.CASCADE,
        related_name='%(class)s_subject'
    )

    class Meta:
        abstract = True


class Deactivate(models.Model):
    "Abstract class for models that can be deactivated"
    active: models.Field = models.BooleanField(default=True)
    deleted_at: models.Field = models.DateTimeField(
        default=None, null=True, blank=True)

    class Meta:
        abstract = True
