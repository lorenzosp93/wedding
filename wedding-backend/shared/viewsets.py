from datetime import datetime
from typing import Type
from django.db.models import F
from django.http.request import HttpRequest
from django.http.response import HttpResponseBase
from django.db.models import QuerySet
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.serializers import ModelSerializer
from wedding.settings import CACHE_TTL
from .models import Deactivate
from .advanced_models import HasAudience


class CachedViewSet(ViewSet):
    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_headers("Authorization"))
    def dispatch(
        self, request: HttpRequest, *args: list, **kwargs: dict
    ) -> HttpResponseBase:
        return super().dispatch(request, *args, **kwargs)


class BaseGetQuerySet(ModelViewSet):
    serializer_class: Type[ModelSerializer]

    def get_queryset(self) -> QuerySet:
        return self.serializer_class.Meta.model.objects.all()


class AudienceViewSet(BaseGetQuerySet):
    def get_queryset(self) -> QuerySet[HasAudience]:
        user = self.request.user
        return super().get_queryset() \
            .annotate(audience_mod=F('audience') % user.profile.type) \
            .filter(audience_mod=0)


class DeactivateViewSet(BaseGetQuerySet):
    def perform_destroy(self, instance: Deactivate) -> None:
        instance.active = False
        instance.deleted_at = datetime.now()
        instance.save()

    def get_queryset(self) -> QuerySet[Deactivate]:
        return super().get_queryset() \
            .filter(active=True)
