import json
from celery import shared_task
from django.apps import apps
from django.core.mail import send_mail
from pywebpush import webpush, WebPushException
from wedding.settings import WEBPUSH_SETTINGS, EMAIL_TO
from profile.serializers import SubscriptionSerializer


@shared_task
def send_email(
    recipient_list: list[str],
    subject: str,
    message: str,
    html_message: str
) -> None:
    send_mail(
        subject=subject,
        message=message,
        from_email=EMAIL_TO,
        recipient_list=recipient_list,
        fail_silently=False,
        html_message=html_message,
    )


@shared_task
def send_notifications_for_subscriptions(subscriptions_list: list[str], payload: dict) -> None:
    subscriptions = apps.get_model(
        'profile', 'Subscription').objects.filter(pk__in=subscriptions_list)

    for subscription in subscriptions:
        try:
            webpush(
                SubscriptionSerializer(subscription).data,
                json.dumps(payload),
                vapid_private_key=WEBPUSH_SETTINGS.get('VAPID_PRIVATE_KEY'),
                vapid_claims={
                    "sub": f"mailto:{WEBPUSH_SETTINGS.get('VAPID_ADMIN_EMAIL')}"},
            )
        except WebPushException:
            subscription.delete()
