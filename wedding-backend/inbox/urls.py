
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import MessageViewSet, ResponseViewSet

app_name = 'inbox'

router = DefaultRouter()
router.register(r'message', MessageViewSet, 'message')
router.register(r'response', ResponseViewSet, 'response')

urlpatterns = [
    path('', include(router.urls)),
]