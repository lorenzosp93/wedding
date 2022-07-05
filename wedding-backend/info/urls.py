
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import InformationViewSet, PhotoViewSet

router = DefaultRouter()
router.register(r'info', InformationViewSet, 'info')
router.register(r'photo', PhotoViewSet, 'photo')

urlpatterns = [
    path('', include(router.urls)),
]