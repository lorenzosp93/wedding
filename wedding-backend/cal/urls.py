
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import RSVPViewSet, EventViewSet

router = DefaultRouter()
router.register(r'event', EventViewSet, 'event')
router.register(r'rsvp', RSVPViewSet, 'rsvp')

urlpatterns = [
    path('', include(router.urls)),
]