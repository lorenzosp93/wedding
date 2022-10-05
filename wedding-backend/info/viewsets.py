from django.conf import Settings
from django.db.models import Q
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from .serializers import (
    InformationSerializer, PhotoSerializer
)
from .models import (
    Information, Photo
)

class InformationViewSet(ReadOnlyModelViewSet):
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
    def get_queryset(self):
        return Photo.objects.filter(Q(tag__id=self.request.user.id) | Q(private=False))
    