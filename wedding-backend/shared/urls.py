from django.urls import path
from .views import get_csrf_token

urlpatterns = [
    path('get-token/', get_csrf_token),
]