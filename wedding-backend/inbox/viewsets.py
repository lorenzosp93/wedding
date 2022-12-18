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
        Message objects
    """
    serializer_class = MessageSerializer


class ResponseViewSet(ModelViewSet):
    """
        This ViewSet enables creation, modification, retrieval 
        and listing of Response objects
    """
    serializer_class = ResponseSerializer

    def get_queryset(self) -> QuerySet[Response]:
        return Response.objects.filter(user__pk=self.request.user.pk)

    def perform_destroy(self, instance: Response) -> None:
        instance.active = False
        instance.deleted_at = datetime.now()
        instance.save()
