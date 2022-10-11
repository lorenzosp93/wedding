from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from .serializers import MessageSerializer, ResponseSerializer
from .models import Message, Response
from shared.viewsets import SerializerContextUserMixin

class MessageViewSet(SerializerContextUserMixin, ReadOnlyModelViewSet):
    """
        This ViewSet enables retrieval and listing of
        UserMessage objects
    """
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

class ResponseViewSet(SerializerContextUserMixin, ModelViewSet):
    """
        This ViewSet enables creation, modification, retrieval 
        and listing of Response objects
    """
    serializer_class = ResponseSerializer
    def get_queryset(self):
        return Response.objects.filter(user__id=self.request.user.id)
