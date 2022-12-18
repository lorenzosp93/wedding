from django.db.models import Q, QuerySet
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from .serializers import (
    InformationSerializer, PhotoSerializer,
)
from .models import (
    Photo,
)
from shared.viewsets import (
    AudienceViewSetMixin,
    CachedViewsetMixin
)


class InformationViewSet(
    CachedViewsetMixin,
    AudienceViewSetMixin,
    ReadOnlyModelViewSet,
):
    """
    This viewset automatically provides `list` and `retrieve`
    actions.

    A simple viewset to view Information entires.
    """
    serializer_class = InformationSerializer


class PhotoViewSet(
    CachedViewsetMixin,
    ReadOnlyModelViewSet,
):
    serializer_class = PhotoSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self) -> QuerySet[Photo]:
        return Photo.objects.filter(Q(tag__pk=self.request.user.pk) | Q(private=False))
