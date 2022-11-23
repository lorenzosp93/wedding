from django.urls import path
from .views import get_auth_token, get_languages

app_name = 'shared'

urlpatterns = [
    path('magic-auth/', get_auth_token, name='magic-auth'),
    path('get-languages/', get_languages, name='get-languages'),
]
