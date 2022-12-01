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
    BaseGetQuerysetMixin,
)


class InformationViewSet(
    AudienceViewSetMixin,
    BaseGetQuerysetMixin,
    ReadOnlyModelViewSet,
):
    """
    This viewset automatically provides `list` and `retrieve`
    actions.

    A simple viewset to view Information entires.
    """
    serializer_class = InformationSerializer


class PhotoViewSet(ReadOnlyModelViewSet):
    serializer_class = PhotoSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self) -> QuerySet[Photo]:
        return Photo.objects.filter(Q(tag__id=self.request.user.id) | Q(private=False))
