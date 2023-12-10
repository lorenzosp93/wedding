from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    DictField,
)
from .models import Information, Photo, InformationWidget
from profile.serializers import (
    TranslationContentMixin,
    TranslationSubjectMixin,
)


class InformationWidgetSerializer(ModelSerializer):
    type = CharField(source="get_type_display")

    class Meta:
        model = InformationWidget
        fields = ["type", "content"]


class InformationSerializer(
    TranslationContentMixin,
    TranslationSubjectMixin,
    ModelSerializer,
):
    type = CharField(source="get_type_display")
    widget = InformationWidgetSerializer(many=True, required=False)

    def to_representation(self, instance: Information) -> dict:
        return super().to_representation(instance)

    class Meta:
        model = Information
        exclude = [
            "audience",
            "submit",
        ]


class PhotoSerializer(
    TranslationContentMixin,
    ModelSerializer,
):
    type = CharField(source="get_type_display")

    class Meta:
        model = Photo
        fields = ["picture", "type", "thumbnail", "content", "id"]
