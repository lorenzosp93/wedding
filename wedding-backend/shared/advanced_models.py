from functools import reduce
from itertools import combinations, chain
from operator import mul
from django.db import models
from django.apps import apps
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from wedding.tasks import send_notifications_for_subscriptions
from wedding.settings import FRONTEND_HOST
from profile.models import USER_TYPES
from .models import HasSubject


audience_types = list(chain(*[
    [(reduce(mul, el, 1),
      f"{' & '.join(dict(USER_TYPES)[k] for k in el)}") for el in comb]
    for comb in [combinations(
        [idx for (idx, _) in USER_TYPES],
        r=ii+1
    ) for ii in range(len(USER_TYPES))]
]))


class HasUserList(models.Model):
    def get_users(self) -> models.QuerySet[AbstractBaseUser]:
        return get_user_model().objects.all()

    class Meta:
        abstract = True


class HasAudience(HasUserList):
    audience: models.Field = models.IntegerField(
        choices=audience_types,
        default=30,
    )

    def get_users(self) -> models.QuerySet[AbstractBaseUser]:
        return super().get_users().annotate(
            audience_mod=self.audience % models.F(
                'profile__type'
            )
        ).filter(audience_mod=0)

    class Meta:
        abstract = True


class TriggersNotifications(
    HasSubject,
    HasUserList
):
    """Abstract mixin to trigger notification"""
    submit: models.Field = models.BooleanField(default=False)

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
        image_link = ''
        if (picture := getattr(self, 'picture', None)):
            image_link = picture.url
        return {
            'image': image_link,
            'body': _(
                "There is a new message for you: %(subject)s"
            ) % {'subject': self.subject},
            'data': {
                'url': f"""{FRONTEND_HOST}/{
                    'inbox' if self.__class__.__name__ == 'Message'
                    else f'info/{self.get_type_display()}'
                }/"""
            }
        }

    def get_subscriptions(self, user_list: list[str]) -> models.QuerySet:
        return apps.get_model('profile', 'Subscription') \
                   .objects.filter(user__pk__in=user_list)

    class Meta:
        abstract = True
