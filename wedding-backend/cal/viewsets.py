from django.conf import Settings
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from .serializers import (
    EventSerializer, RSVPSerializer
)
from .models import (
    Event, RSVP
)

class EventViewSet(ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve`
    actions.

    A simple viewset to view Event entires.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class RSVPViewSet(ModelViewSet):
    queryset = RSVP.objects.all()
    serializer_class = RSVPSerializer
