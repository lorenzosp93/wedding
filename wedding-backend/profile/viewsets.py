from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django.db.models import QuerySet
from .serializers import (
    UserProfileSerializer, SubscriptionSerializer
)
from .models import (
    UserProfile,
    Subscription,
)

WRITE_ACTIONS = ["create", "update", "partial_update", "destroy"]


class UserProfileViewset(ReadOnlyModelViewSet):
    """
    This viewset automatically provides CRUD
    actions for UserProfile entries.

    """
    serializer_class = UserProfileSerializer

    def get_queryset(self) -> QuerySet[UserProfile]:
        return UserProfile.objects.filter(user__pk=self.request.user.pk)


class SubscriptionViewset(ModelViewSet):
    serializer_class = SubscriptionSerializer

    def get_queryset(self) -> QuerySet[Subscription]:
        return Subscription.objects.filter(
            user__pk=self.request.user.pk,
            user_agent=self.request.META.get('HTTP_USER_AGENT')
        )
