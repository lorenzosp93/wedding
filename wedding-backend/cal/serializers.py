from rest_framework.serializers import (
    ModelSerializer
)
from .models import (
    Event, RSVP
)

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class RSVPSerializer(ModelSerializer):
    class Meta:
        model = RSVP
        fields = '__all__'
