from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserProfileViewset, SubscriptionViewset
from .views import setup_plus_one

app_name = 'profile'

router = DefaultRouter()
router.register(r'profile', UserProfileViewset, 'profile')
router.register(r'subscription', SubscriptionViewset, 'subscription')

urlpatterns = [
    path('', include(router.urls)),
    path('setup-plus-one/', setup_plus_one, name='setup-plus-one')
]
