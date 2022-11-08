from unicodedata import name
from django.urls import path
from .views import get_csrf_token, get_auth_token, get_languages

app_name = 'shared'

urlpatterns = [
    path('get-token/', get_csrf_token, name="get-token"),
    path('magic-auth/', get_auth_token, name='magic-auth'),
    path('get-languages/', get_languages, name='get-languages'),
]