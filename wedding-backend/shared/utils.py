import logging
from django.contrib.auth.models import AbstractUser
from django.template import loader
from django.utils.translation import override, gettext_lazy as _
from django.urls import reverse
from drfpasswordless.settings import api_settings
from drfpasswordless.utils import inject_template_context
from drfpasswordless.models import CallbackToken
from wedding.settings import BACKEND_HOST, HOST
from wedding.tasks import send_email

logger = logging.getLogger(__name__)


def send_email_with_callback_token(
    user: AbstractUser, email_token: CallbackToken, **kwargs: str
) -> bool:
    """
    Sends a Email to user.email.

    Passes silently without sending in test environment
    """

    try:
        if api_settings.PASSWORDLESS_EMAIL_NOREPLY_ADDRESS:
            # Make sure we have a sending address before sending.

            # Get email subject and message
            email_plaintext: str = kwargs.get(
                'email_plaintext',
                api_settings.PASSWORDLESS_EMAIL_PLAINTEXT_MESSAGE,
            )
            email_html: str = kwargs.get(
                'email_html',
                api_settings.PASSWORDLESS_EMAIL_TOKEN_HTML_TEMPLATE_NAME,
            )

            email = user.email
            # activate user language
            with override(user.profile.language):
                email_subject: str = _(
                    'Here is your login link for %(host)s'
                ) % {
                    'host': HOST,
                }
                # Inject context if user specifies.
                context = inject_template_context({
                    'callback_token': email_token.key,
                    'user_email': email,
                    'auth_url': reverse('shared:magic-auth'),
                    'site_name': BACKEND_HOST,
                })
                html_message = loader.render_to_string(email_html, context,)
            send_email.delay(
                recipient_list=[email],
                subject=email_subject,
                message=email_plaintext % email_token.key,
                html_message=html_message,
            )

        else:
            logger.debug(
                """Failed to send token email.
                Missing PASSWORDLESS_EMAIL_NOREPLY_ADDRESS."""
            )
            return False
        return True

    except Exception as e:
        logger.debug("Failed to send token email to user: %d."
                     "Possibly no email on user object. Email entered was %s" %
                     (user.pk, user.email))
        logger.debug(e)
        return False
