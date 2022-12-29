from django.db.models import QuerySet
from rest_framework.viewsets import (
    ReadOnlyModelViewSet,
)
from shared.viewsets import (
    AudienceViewSetMixin,
    PrerequisiteViewSetMixin,
    DeactivateViewSetMixin,
)
from .serializers import MessageSerializer, ResponseSerializer
from .models import Response


class MessageViewSet(
    PrerequisiteViewSetMixin,
    AudienceViewSetMixin,
    ReadOnlyModelViewSet,
):
    """
        This ViewSet enables retrieval and listing of
        Message objects
    """
    serializer_class = MessageSerializer


class ResponseViewSet(DeactivateViewSetMixin):
    """
        This ViewSet enables creation, modification, retrieval 
        and listing of Response objects
    """
    serializer_class = ResponseSerializer

    def get_queryset(self) -> QuerySet[Response]:
        return Response.objects.filter(user__pk=self.request.user.pk)
