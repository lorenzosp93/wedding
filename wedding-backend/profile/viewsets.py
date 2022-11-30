from rest_framework.viewsets import ModelViewSet
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

    def get_serializer_class(self):
        if self.action in WRITE_ACTIONS:
            return UserProfileWriteSerializer
        return UserProfileSerializer

    def get_queryset(self) -> QuerySet[UserProfile]:
        return UserProfile.objects.filter(user__id=self.request.user.id)


class SubscriptionViewset(ModelViewSet):
    serializer_class = SubscriptionSerializer

    def get_queryset(self) -> QuerySet[Subscription]:
        return Subscription.objects.filter(user_id=self.request.user.id)
