from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserProfileRWViewSet, UserProfileReadOnlyViewSet

router = DefaultRouter()
router.register(r'user-profile/edit', UserProfileRWViewSet, 'profile-edit')
router.register(r'user-profile', UserProfileReadOnlyViewSet, 'profile-view')

urlpatterns = [
    path('', include(router.urls)),
]