from django.db.models import QuerySet, Q
from django.contrib.auth.models import AbstractBaseUser, AnonymousUser
from rest_framework.viewsets import (
    ReadOnlyModelViewSet
)
from shared.viewsets import (
    AudienceViewSet,
    DeactivateViewSet,
    BaseGetQuerySet,
)
from .serializers import MessageSerializer, ResponseSerializer
from .models import Response, HasPrerequisiteOptions


class PrerequisiteViewSet(BaseGetQuerySet):
    def get_queryset(self) -> QuerySet[HasPrerequisiteOptions]:
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
        cohort_pre: QuerySet[HasPrerequisiteOptions],
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


class MessageViewSet(
    PrerequisiteViewSet,
    AudienceViewSet,
    ReadOnlyModelViewSet,
):
    """
        This ViewSet enables retrieval and listing of
        Message objects
    """
    serializer_class = MessageSerializer


class ResponseViewSet(DeactivateViewSet):
    """
        This ViewSet enables creation, modification, retrieval 
        and listing of Response objects
    """
    serializer_class = ResponseSerializer

    def get_queryset(self) -> QuerySet[Response]:
        return super().get_queryset().filter(user__pk=self.request.user.pk)
