from django.middleware.csrf import get_token
from django.shortcuts import redirect
from django.contrib.sites.models import Site
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
import requests
import json

BACKEND = Site.objects.get_current()
FRONTEND = Site.objects.get(name='FRONTEND')

# Create your views here.
@api_view(('GET',))
@permission_classes((AllowAny,))
def get_csrf_token(request):
    """
        Function to return CSRF token. 
    """
    token = get_token(request)
    return Response({"token": token}, status=status.HTTP_200_OK)

@api_view(['GET',])
@permission_classes([AllowAny,])
def get_auth_token(request, *args, **kwargs):
    """
        Function to retrieve auth token from email + OTP combination.
    """
    email = request.GET.get('email')
    otp = request.GET.get('token')
    if email and otp:
        r = requests.post(
            f"{BACKEND}/auth/token/",
            data=json.dumps({"email": email, "token": int(otp)}),
            headers={'Content-Type': 'application/json'}
        )
        if r.status_code == 200:
            return redirect(f"{FRONTEND}/?token={r.json().get('token')}" )
        return Response(r.text, status=r.status_code)
    return Response("Email and Token must be provided", status=status.HTTP_400_BAD_REQUEST)
