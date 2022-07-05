from django.conf import Settings
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
    serializer_class = Photo
