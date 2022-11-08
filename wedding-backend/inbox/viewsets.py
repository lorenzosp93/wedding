from django.db.models import Q
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from .serializers import MessageSerializer, ResponseSerializer
from .models import Message, Response, Option

class MessageViewSet(ReadOnlyModelViewSet):
    """
        This ViewSet enables retrieval and listing of
        UserMessage objects
    """
    pagination_class = LimitOffsetPagination
    serializer_class = MessageSerializer

    def get_queryset(self):
        """
        Logic to correctly return messages with no prerequisites and messages
        for which the prerequisite is met by the user.
        """
        messages_pre = Message.objects.filter(option_pre__isnull=False) \
                                      .values('pk', 'option_pre')
        messages_list = []
        if messages_pre:
            user_options = Response.objects.filter(
                user__id=self.request.user.id,
            ).values_list('option', flat=True)
            for message in messages_pre:
                pre = message.get('option_pre')
                if (
                    hasattr(pre, '__iter__') and all(item in user_options for item in pre)
                    or pre in user_options
                ):
                    messages_list = [*messages_list, message.get('pk')]
        return Message.objects.filter(
            Q(option_pre__isnull=True)
            |
            Q(pk__in=messages_list)
        )

class ResponseViewSet(ModelViewSet):
    """
        This ViewSet enables creation, modification, retrieval 
        and listing of Response objects
    """
    serializer_class = ResponseSerializer
    def get_queryset(self):
        return Response.objects.filter(user__id=self.request.user.id)
