from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from shared.models import (
    HasPicture,
    HasContent,
    HasSubject,
)
from shared.advanced_models import (
    TriggersNotifications,
    HasAudience,
)

INFO_TYPES = (
    (3, _("Tips")),
    (4, _("Travel")),
    (5, _("Events")),
    (6, _("Gifts")),
)

PHOTO_TYPES = (
    (0, _("Before")),
    (1, _("Ice-breaker")),
    (2, _("Ceremony")),
    (3, _("Reception")),
    (4, _("Dinner")),
    (5, _("Dance")),
)

WIDGET_TYPES = (
    (0, "calendar"),
    (1, "maps"),
)

# Create your models here.


class Information(
    TriggersNotifications, HasAudience, HasPicture, HasContent, HasSubject
):
    type: models.Field = models.IntegerField(
        choices=INFO_TYPES,
    )

    def __str__(self) -> str:
        return f"{self.subject}"

    class Meta:
        ordering = ["pk"]


class InformationWidget(models.Model):
    info: models.Field = models.ForeignKey(
        Information, on_delete=models.CASCADE, related_name="widget"
    )
    type: models.Field = models.IntegerField(
        choices=WIDGET_TYPES,
    )
    content: models.Field = models.JSONField()

    def __str__(self) -> str:
        return f"{self.type} - {self.info}"

    def save(self, **kwargs) -> None:
        self.full_clean()
        return super().save(**kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["info", "type"],
                name="unique_widget_per_info_type",
            ),
        ]


class Photo(HasPicture, HasContent):
    tag: models.Field = models.ManyToManyField(
        User,
        blank=True,
    )
    private: models.Field = models.BooleanField(
        default=False,
    )
    type: models.Field = models.IntegerField(choices=PHOTO_TYPES, default=0)

    def __str__(self) -> str:
        return f"{self.picture.name} - {self.type}"

    class Meta:
        ordering = ["pk"]
