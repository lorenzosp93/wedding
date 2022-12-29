from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from shared.viewsets import DeactivateViewSet
from .serializers import EntrySerializer


# Create your views here.


class EntryViewset(DeactivateViewSet, ModelViewSet):
    serializer_class = EntrySerializer
    pagination_class = LimitOffsetPagination
