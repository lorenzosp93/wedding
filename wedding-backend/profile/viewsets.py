from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    UserProfileAddressSerializer, UserProfileSerializer
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
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()

    def get_serializer_class(self):
        if self.action in WRITE_ACTIONS:
            return UserProfileAddressSerializer
        return UserProfileSerializer

    def get_queryset(self):
        if self.action in WRITE_ACTIONS:
            return super().get_queryset().filter(user__id=self.request.user.id)
        return super().get_queryset().filter(user__id=self.request.user.id)
        
