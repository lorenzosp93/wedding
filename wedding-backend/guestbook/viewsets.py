from django.db.models import QuerySet
from rest_framework.viewsets import ModelViewSet
from .models import Entry
from .serializers import EntrySerializer

# Create your views here.


class EntryViewset(ModelViewSet):
    serializer_class = EntrySerializer

    def get_queryset(self) -> QuerySet[Entry]:
        return Entry.objects.filter(active=True)
