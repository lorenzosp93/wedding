from datetime import datetime
from typing import Type
from django.db.models import Q, F
from django.http.request import HttpRequest
from django.http.response import HttpResponseBase
from django.db.models import QuerySet
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.contrib.auth.models import AbstractBaseUser, AnonymousUser
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.serializers import ModelSerializer
from inbox.models import Message
from wedding.settings import CACHE_TTL
from .models import Deactivate
from .advanced_models import HasAudience


class CachedViewsetMixin(ViewSet):
    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_headers("Authorization"))
    def dispatch(
        self, request: HttpRequest, *args: list, **kwargs: dict
    ) -> HttpResponseBase:
        return super().dispatch(request, *args, **kwargs)


class BaseGetQuerysetMixin(ViewSet):
    serializer_class: Type[ModelSerializer]

    def get_queryset(self) -> QuerySet:
        return self.serializer_class.Meta.model.objects.all()


class PrerequisiteViewSetMixin(BaseGetQuerysetMixin):
    def get_queryset(self) -> QuerySet[Message]:
        """
        Logic to correctly return messages with no prerequisites and messages
        for which the prerequisite is met by the user.
        """
        user = self.request.user
        cohort = super().get_queryset()
        cohort_pre = cohort.filter(option_pre__isnull=False) \
            .values('pk', 'option_pre')
        obj_list = self.get_list_pre(user, cohort_pre)
        return cohort.filter(
            Q(option_pre__isnull=True)
            |
            Q(pk__in=obj_list)
        )

    def get_list_pre(
        self,
        user: AbstractBaseUser | AnonymousUser,
        cohort_pre: QuerySet[Message],
        obj_list: list = []
    ) -> list:
        if cohort_pre:
            user_options = user.response_set.filter(
                active=True,
            ).values_list('option', flat=True)
            for obj in cohort_pre:
                pre = obj.get('option_pre')
                if (
                    hasattr(pre, '__iter__')  # pre is iterable
                    and all(
                        item in user_options
                        for item in pre
                    )  # all prerequisites in pre are found in user_options
                    or pre in user_options  # single prerequisite is found
                ):
                    obj_list = [*obj_list, obj.get('pk')]
        return obj_list


class AudienceViewSetMixin(BaseGetQuerysetMixin):
    def get_queryset(self) -> QuerySet[HasAudience]:
        user = self.request.user
        return super().get_queryset() \
            .annotate(audience_mod=F('audience') % user.profile.type) \
            .filter(audience_mod=0)


class DeactivateViewSetMixin(ModelViewSet):
    def perform_destroy(self, instance: Deactivate) -> None:
        instance.active = False
        instance.deleted_at = datetime.now()
        instance.save()
