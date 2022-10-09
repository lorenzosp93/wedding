from django.conf import Settings
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import (
    SettingsSerializer
)
from .models import (
    SiteSetting
)

class SettingsViewSet(ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve`
    actions.

    A simple viewset to view Settings entires.
    """
    queryset = SiteSetting.objects.all()
    serializer_class = SettingsSerializer


