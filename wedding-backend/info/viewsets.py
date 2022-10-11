from django.db.models import Q
from rest_framework.viewsets import ReadOnlyModelViewSet 
from rest_framework.pagination import LimitOffsetPagination
from .serializers import (
    InformationSerializer, PhotoSerializer
)
from .models import (
    Information, Photo
)
from shared.viewsets import SerializerContextUserMixin

class InformationViewSet(SerializerContextUserMixin, ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve`
    actions.

    A simple viewset to view Information entires.
    """
    queryset = Information.objects.all()
    serializer_class = InformationSerializer

class PhotoViewSet(ReadOnlyModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        return Photo.objects.filter(Q(tag__id=self.request.user.id) | Q(private=False))
    