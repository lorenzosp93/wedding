from django.middleware.csrf import get_token
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from drfpasswordless.views import ObtainAuthTokenFromCallbackToken

# Create your views here.
@api_view(('GET',))
@permission_classes((AllowAny,))
def get_csrf_token(request):
    token = get_token(request)
    return Response({"token": token}, status=status.HTTP_200_OK)

@api_view(['GET',])
@permission_classes([AllowAny,])
def get_auth_token(request):
    email = request.GET.get('email')
    otp = request.GET.get('token')
    if email and otp:
        postRequest = HttpRequest()
        postRequest.method = 'POST'
        postRequest.META = request.META
        postRequest.data = {'email': email, 'token': otp}
        view = ObtainAuthTokenFromCallbackToken.as_view()
        return view(postRequest)
    return Response("Email and Token must be provided", status=status.HTTP_400_BAD_REQUEST)
