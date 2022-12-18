from typing import Type
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
from django.db.models import QuerySet
from .serializers import (
    UserProfileWriteSerializer, UserProfileSerializer, SubscriptionSerializer
)
from .models import (
    UserProfile,
    Subscription,
)

WRITE_ACTIONS = ["create", "update", "partial_update", "destroy"]


class UserProfileViewset(ModelViewSet):
    """
    This viewset automatically provides CRUD
    actions for UserProfile entries.

    """

    def get_serializer_class(self) -> Type[ModelSerializer]:
        if self.action in WRITE_ACTIONS:
            return UserProfileWriteSerializer
        return UserProfileSerializer

    def get_queryset(self) -> QuerySet[UserProfile]:
        return UserProfile.objects.filter(user__pk=self.request.user.pk)


class SubscriptionViewset(ModelViewSet):
    serializer_class = SubscriptionSerializer

    def get_queryset(self) -> QuerySet[Subscription]:
        return Subscription.objects.filter(user_pk=self.request.user.pk)
