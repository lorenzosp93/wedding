from typing import Any
from itertools import combinations
from django.db import models
from django.apps import apps
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from wedding.tasks import send_notifications_for_subscriptions
from wedding.settings import FRONTEND_HOST
from profile.models import USER_TYPES
from .models import HasSubject

audience_types = [
    *USER_TYPES,
    *list(
        (a*b, f"{dict(USER_TYPES)[a]} & {dict(USER_TYPES)[b]}")  # type: ignore
        for (a, b) in combinations(
            [idx for (idx, _) in USER_TYPES],
            r=2
        )
    ),
    (30, 'all')
]


class HasUserList(models.Model):
    def get_users(self) -> models.QuerySet[User]:
        return User.objects.all()

    class Meta:
        abstract = True


class HasAudience(HasUserList):
    audience = models.IntegerField(
        choices=audience_types,
        default=30,
    )

    def get_users(self) -> models.QuerySet[User]:
        return super().get_users().annotate(
            audience_mod=self.audience % models.F(
                'profile__type'
            )
        ).filter(audience_mod=0)

    class Meta:
        abstract = True


class TriggersNotifications(
    HasSubject,
    HasUserList,
):
    """Abstract mixin to trigger notification"""
    submit = models.BooleanField(default=False)

    def save(self, *args, **kwargs) -> None:
        if self.submit:
            self.send_notifications()
            self.submit = False
        super().save(*args, **kwargs)

    def send_notifications(self) -> None:
        users = self.get_users()
        subscriptions = self.get_subscriptions(
            [*users.values_list('pk', flat=True)]
        )
        payload = self.build_payload()
        send_notifications_for_subscriptions.delay(
            [*subscriptions.values_list('pk', flat=True)], payload)

    def build_payload(self) -> dict[str, str | dict[str, str] | None]:
        return {
            'image': getattr(self, 'picture', None),
            'body': _("There is a new message for you: %(subject)s") % {'subject': self.subject},
            'data': {
                'url': f"{FRONTEND_HOST}/{'inbox' if self.__class__.__name__ == 'Message' else 'info'}/"
            }
        }

    def get_subscriptions(self, user_list: list[str]) -> models.QuerySet[Any]:
        return apps.get_model('profile', 'Subscription') \
                   .objects.filter(user__pk__in=user_list)

    class Meta:
        abstract = True
