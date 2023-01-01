from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import EntryViewset

app_name = 'guestbook'

router = DefaultRouter()
router.register(r'entry', EntryViewset, 'entry')

urlpatterns = [
    path('', include(router.urls)),
]
