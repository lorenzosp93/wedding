
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserMessageViewSet, ResponseViewSet

router = DefaultRouter()
router.register(r'user-message', UserMessageViewSet, 'user-message')
router.register(r'response', ResponseViewSet, 'response')

urlpatterns = [
    path('', include(router.urls)),
]