from rest_framework.serializers import (
    ModelSerializer, CharField, DictField, RelatedField
)
from .models import (
    Information, Photo, InformationWidget
)
from profile.serializers import TranslationContentMixin, TranslationSubjectMixin


class InformationWidgetSerializer(ModelSerializer):
    type = CharField(source="get_type_display")
    content = DictField(source="get_content_dict")

    class Meta:
        model = InformationWidget
        fields = ['type', 'content']


class InformationSerializer(
    TranslationContentMixin,
    TranslationSubjectMixin,
    ModelSerializer,
):
    type = CharField(source="get_type_display")
    widget = InformationWidgetSerializer(many=True, required=False)

    def to_representation(self, instance):
        return super().to_representation(instance)

    class Meta:
        model = Information
        fields = [
            'id', 'content', 'subject', 'type',
            'widget', 'picture', 'thumbnail',
        ]


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ['picture', 'thumbnail', 'id']
