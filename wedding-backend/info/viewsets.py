from django.db.models import Q, QuerySet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from .serializers import (
    InformationSerializer,
    PhotoSerializer,
)
from .models import (
    Photo,
)
from shared.viewsets import (
    AudienceViewSet,
)


class InformationViewSet(
    AudienceViewSet,
    ReadOnlyModelViewSet,
):
    """
    This viewset automatically provides `list` and `retrieve`
    actions.

    A simple viewset to view Information entires.
    """

    serializer_class = InformationSerializer


class PhotoViewSet(
    ReadOnlyModelViewSet,
):
    serializer_class = PhotoSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self) -> QuerySet[Photo]:
        query = Q(private=False)
        user_pk = self.request.user.pk
        if user_pk:
            query = query | Q(tag__pk=user_pk)
        return Photo.objects.filter(query)
