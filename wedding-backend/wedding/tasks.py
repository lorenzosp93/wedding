import json
import base64
from io import BytesIO
from PIL import Image
from smtplib import SMTPConnectError, SMTPServerDisconnected
from django.core.files.uploadedfile import SimpleUploadedFile
from django.apps import apps
from django.core.mail import send_mail
from pywebpush import webpush, WebPushException
from wedding.settings import WEBPUSH_SETTINGS, EMAIL_TO
from wedding.celery import app
from shared.models import HasPicture

@app.task(
    ignore_result=True,
    autoretry_for=(
        SMTPConnectError,
        SMTPServerDisconnected,
    ),
    retry_kwargs={'max_retries': 3},
    retry_backoff=True,
    default_retry_delay=15
)
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


@app.task(
    ignore_result=True,
)
def send_notifications_for_subscriptions(
    subscriptions_list: list[str], payload: dict
) -> None:
    subscriptions = apps.get_model(
        'profile', 'Subscription').objects.filter(pk__in=subscriptions_list)

    for subscription in subscriptions:
        try:
            webpush(
                apps.get_model('profile', 'Subscription')(subscription).data,
                json.dumps(payload),
                vapid_private_key=WEBPUSH_SETTINGS.get('VAPID_PRIVATE_KEY'),
                vapid_claims={
                    "sub": f"mailto:{WEBPUSH_SETTINGS.get('VAPID_ADMIN_EMAIL')}"},
            )
        except WebPushException:
            subscription.delete()

@app.task(
    ignore_result=True,
    autoretry_for=(

    ),
    retry_kwargs={'max_retries': 3},
    retry_backoff=True,
    default_retry_delay=15
)
def process_photos_task(type: str,
                        encoded_photo: str=[],
                        filename: str=[]
                        ) -> None:
    photo_model = apps.get_model('info', 'Photo')

    decoded_photo = base64.urlsafe_b64decode(encoded_photo)

    with BytesIO(decoded_photo) as f:
        with Image.open(f) as img:
            suf = HasPicture.save_img(img, filename)
            photo_model.objects.update_or_create(
                type=type,
                picture=suf,
            )
