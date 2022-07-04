from django.shortcuts import render
from django.middleware.csrf import get_token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

# Create your views here.
@api_view(('GET',))
@permission_classes((AllowAny,))
def get_csrf_token(request):
    token = get_token(request)
    return Response({"token": token}, status=status.HTTP_200_OK)