from django.db.models import Q, F
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import (
    SettingsSerializer
)
from .models import (
    SiteSetting
)


class PrerequisiteViewSetMixin:
    def get_queryset(self):
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

    def get_list_pre(self, user, cohort_pre, obj_list=[]):
        if cohort_pre:
            user_options = user.response_set.values_list('option', flat=True)
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


class AudienceViewSetMixin:
    def get_queryset(self):
        user = self.request.user
        return super().get_queryset() \
            .annotate(audience_mod=F('audience') % user.profile.type) \
            .filter(audience_mod=0)


class BaseGetQuerysetMixin:
    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()


class SettingsViewSet(ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve`
    actions.

    A simple viewset to view Settings entires.
    """
    queryset = SiteSetting.objects.all()
    serializer_class = SettingsSerializer
