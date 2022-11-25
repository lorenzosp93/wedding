from rest_framework.viewsets import ModelViewSet
from .serializers import (
    UserProfileWriteSerializer, UserProfileSerializer
)
from .models import (
    UserProfile
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

    def get_queryset(self):
        return UserProfile.objects.filter(user__id=self.request.user.id)
