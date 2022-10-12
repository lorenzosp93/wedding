from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserProfileViewset
from .views import setup_plus_one

router = DefaultRouter()
router.register(r'profile', UserProfileViewset, 'profile')

urlpatterns = [
    path('', include(router.urls)),
    path('setup-plus-one/', setup_plus_one, name='setup-plus-one')
]