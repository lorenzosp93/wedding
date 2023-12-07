from django.db.models import QuerySet
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    BasePermission,
    IsAuthenticated,
)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from shared.viewsets import DeactivateViewSet
from .serializers import EntrySerializer


# Create your views here.

WRITE_ACTIONS = ["create", "update", "partial_update", "destroy"]


class EntryViewset(DeactivateViewSet, ModelViewSet):
    serializer_class = EntrySerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        if self.action in WRITE_ACTIONS:
            queryset = queryset.filter(user=self.request.user)
        return queryset
