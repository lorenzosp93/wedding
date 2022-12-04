import json
from celery import shared_task
from django.core.mail import send_mail
from pywebpush import webpush, WebPushException
from profile.models import Subscription
from wedding.settings import WEBPUSH_SETTINGS
from profile.serializers import SubscriptionSerializer

@shared_task
def send_email(user_email:str, token:str, subject:str, plaintext:str, html_message:str, email_from:str):
    send_mail(
        subject=subject,
        message=plaintext % token,
        from_email=email_from,
        recipient_list=[user_email],
        fail_silently=False,
        html_message=html_message,
    )


@shared_task
def send_notifications_for_subscriptions(subscriptions_list:list[str], payload:dict) -> None:
    subscriptions = Subscription.objects.filter(pk__in=subscriptions_list)

    for subscription in subscriptions:
        try:
            webpush(
                SubscriptionSerializer(subscription).data,
                json.dumps(payload),
                vapid_private_key=WEBPUSH_SETTINGS.get('VAPID_PRIVATE_KEY'),
                vapid_claims={"sub": f"mailto:{WEBPUSH_SETTINGS.get('VAPID_ADMIN_EMAIL')}"},
            )
        except WebPushException:
            subscription.delete()
