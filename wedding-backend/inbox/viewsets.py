from rest_framework.viewsets import (
    ReadOnlyModelViewSet,
    ModelViewSet,
)
from rest_framework.pagination import LimitOffsetPagination
from shared.viewsets import (
    AudienceViewSetMixin,
    BaseGetQuerysetMixin,
    PrerequisiteViewSetMixin
)
from .serializers import MessageSerializer, ResponseSerializer
from .models import Response


class MessageViewSet(
    PrerequisiteViewSetMixin,
    AudienceViewSetMixin,
    BaseGetQuerysetMixin,
    ReadOnlyModelViewSet,
):
    """
        This ViewSet enables retrieval and listing of
        UserMessage objects
    """
    pagination_class = LimitOffsetPagination
    serializer_class = MessageSerializer


class ResponseViewSet(ModelViewSet):
    """
        This ViewSet enables creation, modification, retrieval 
        and listing of Response objects
    """
    serializer_class = ResponseSerializer

    def get_queryset(self):
        return Response.objects.filter(user__id=self.request.user.id)
