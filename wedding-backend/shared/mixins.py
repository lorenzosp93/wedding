
import json
from pywebpush import webpush
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from inbox.models import Response
from profile.models import Subscription
from profile.serializers import SubscriptionSerializer
from wedding.settings import WEBPUSH_SETTINGS, FRONTEND_HOST


class TriggersNotifications(
    models.Model
):
    """Abstract mixin to trigger notification"""
    submit = models.BooleanField(default=False)

    def save(self) -> None:
        if self.submit:
            self.send_notifications()
            self.submit = False
        super().save()

    def send_notifications(self) -> None:
        user_list = self.get_user_list()
        subscriptions = self.get_subscriptions(user_list)
        payload = self.build_payload()
        self.send_notifications_for_subscriptions(subscriptions, payload)

    def build_payload(self) -> dict:
        payload = {
            'image': getattr(self, 'picture', None),
            'body': _("There is a new message for you: %(subject)s") % {'subject': self.subject},
            'data': {
                'url': f"{FRONTEND_HOST}/{'inbox' if self.__class__.__name__ == 'Message' else 'info'}/"
            }
        }
        return payload

    def send_notifications_for_subscriptions(self, subscriptions:models.QuerySet[Subscription], payload:dict) -> None:
        for subscription in subscriptions:
            webpush(
                SubscriptionSerializer(subscription).data,
                json.dumps(payload),
                vapid_private_key=WEBPUSH_SETTINGS.get('VAPID_PRIVATE_KEY'),
                vapid_claims={"sub": f"mailto:{WEBPUSH_SETTINGS.get('VAPID_ADMIN_EMAIL')}"},
            )

    def get_subscriptions(self, user_list:list[str]) -> models.QuerySet[Subscription]:
        return Subscription.objects.filter(user__pk__in=user_list)

    def get_user_list(self) -> list[str]:
        user_list_audience = self.get_user_list_audience()
        user_list_pre = User.objects.all()
        if hasattr(self, 'option_pre') and self.option_pre.count() > 0:
            user_list_pre = self.get_user_list_pre()
        return User.objects.filter(
            models.Q(pk__in=user_list_audience)
            &
            models.Q(pk__in=user_list_pre)
        ).values_list('pk', flat=True)

    def get_user_list_audience(self) -> list[str]:
        return User.objects.annotate(
            audience_mod=self.audience % models.F('profile__type')
        ).filter(audience_mod=0).values_list('pk', flat=True)

    def get_user_list_pre(self):
        return [
            Response.objects.filter(option=option)
                            .values_list('user__pk', flat=True)
            for option in self.option_pre.all()
        ]

    class Meta:
        abstract = True
