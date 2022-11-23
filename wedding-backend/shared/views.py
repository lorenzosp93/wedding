from django.middleware.csrf import get_token
from django.shortcuts import redirect
from django.utils.module_loading import import_string
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

import logging

from drfpasswordless.serializers import CallbackTokenAuthSerializer
from drfpasswordless.settings import api_settings
from wedding.settings import FRONTEND_HOST
from .models import I18N

logger = logging.getLogger(__name__)

# Create your views here.


@api_view(('GET',))
@permission_classes((AllowAny,))
def get_languages(request):
    """
        Return supported languages
    """
    return Response([{'iso': x, 'display': y} for x, y in I18N], status=status.HTTP_200_OK)


@api_view(['GET', ])
@permission_classes([AllowAny, ])
def get_auth_token(request, *args, **kwargs):
    """
        Function to retrieve auth token from email/mobile + OTP combination.
    """
    serializer = CallbackTokenAuthSerializer(data=request.GET)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        token_creator = import_string(
            api_settings.PASSWORDLESS_AUTH_TOKEN_CREATOR)

        (token, _) = token_creator(user)

        if token:
            TokenSerializer = import_string(
                api_settings.PASSWORDLESS_AUTH_TOKEN_SERIALIZER)
            token_serializer = TokenSerializer(
                data=token.__dict__, partial=True)
            if token_serializer.is_valid():
                return redirect(f"{FRONTEND_HOST}/?token={token_serializer.data.get('token')}")

    logger.error("Couldn't log in unknown user. Errors on serializer: {}".format(
        serializer.error_messages))
    return Response({'detail': 'Couldn\'t log you in. Try again later.'}, status=status.HTTP_400_BAD_REQUEST)
