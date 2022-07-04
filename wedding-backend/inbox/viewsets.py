from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import UserMessageSerializer, ResponseSerializer
from .models import UserMessage, Response


class UserMessageViewSet(ReadOnlyModelViewSet):
    """
        This ViewSet enables retrieval and listing of
        UserMessage objects
    """
    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializer
    permission_classes = [IsAuthenticated]

class ResponseViewSet(ModelViewSet):
    """
        This ViewSet enables creation, modification, retrieval 
        and listing of Response objects
    """
    permission_classes = [IsAuthenticated]
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
