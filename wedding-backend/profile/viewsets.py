from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    UserProfileRWSerializer, UserProfileReadSerializer
)
from .models import (
    UserProfile
)

class UserProfileRWViewSet(ModelViewSet):
    """
    This viewset automatically provides CRUD
    actions for UserProfile entries.

    """
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileRWSerializer
    def get_queryset(self):
        return super().get_queryset().filter(user__id=self.request.user.id)


class UserProfileReadOnlyViewSet(ReadOnlyModelViewSet):
    """
    This viewset automatically provides read
    actions for UserProfile entries.
    """
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all() # should only include authenticated user or any +1
    serializer_class = UserProfileRWSerializer
    def get_queryset(self):
        return super().get_queryset().filter(user__id=self.request.user.id)
