from django.urls import path
from .views import get_csrf_token, get_auth_token

urlpatterns = [
    path('get-token/', get_csrf_token),
    path('magic-auth/', get_auth_token, name='magic-auth')
]