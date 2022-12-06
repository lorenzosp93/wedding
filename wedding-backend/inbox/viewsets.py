from datetime import datetime
from django.db.models import QuerySet
from rest_framework.viewsets import (
    ReadOnlyModelViewSet,
    ModelViewSet,
)
from shared.viewsets import (
    AudienceViewSetMixin,
    PrerequisiteViewSetMixin
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
        UserMessage objects
    """
    serializer_class = MessageSerializer


class ResponseViewSet(ModelViewSet):
    """
        This ViewSet enables creation, modification, retrieval 
        and listing of Response objects
    """
    serializer_class = ResponseSerializer

    def get_queryset(self) -> QuerySet[Response]:
        return Response.objects.filter(user__id=self.request.user.id)

    def perform_destroy(self, instance: Response) -> None:
        instance.active = False
        instance.deleted_at = datetime.now()
        instance.save()
