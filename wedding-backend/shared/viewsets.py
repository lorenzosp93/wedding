from typing import Type
from django.db.models import Q, F
from django.http import HttpRequest
from django.http.response import HttpResponseBase
from rest_framework.request import Request
from django.db.models import QuerySet
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.contrib.auth.models import AbstractBaseUser, AnonymousUser
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet
from rest_framework.serializers import ModelSerializer
from .serializers import (
    SettingsSerializer
)
from .models import (
    SiteSetting
)
from wedding.settings import CACHE_TTL

class CachedViewsetMixin(ViewSet):
    @method_decorator(cache_page(CACHE_TTL))
    @method_decorator(vary_on_headers("Authorization"))
    def dispatch(self, request: HttpRequest, *args: list, **kwargs: dict) -> HttpResponseBase:
        return super().dispatch(request, *args, **kwargs)

class BaseGetQuerysetMixin:
    serializer_class: Type[ModelSerializer]
    request: Request | HttpRequest
    def get_queryset(self) -> QuerySet:
        return self.serializer_class.Meta.model.objects.all()


class PrerequisiteViewSetMixin(BaseGetQuerysetMixin):
    def get_queryset(self) -> QuerySet:
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
        cohort_pre: QuerySet,
        obj_list: list=[]
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
                    or pre in user_options  # single prerequisite is found in user_options
                ):
                    obj_list = [*obj_list, obj.get('pk')]
        return obj_list


class AudienceViewSetMixin(BaseGetQuerysetMixin):
    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return super().get_queryset() \
            .annotate(audience_mod=F('audience') % user.profile.type) \
            .filter(audience_mod=0)


class SettingsViewSet(ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve`
    actions.

    A simple viewset to view Settings entires.
    """
    queryset = SiteSetting.objects.all()
    serializer_class = SettingsSerializer
