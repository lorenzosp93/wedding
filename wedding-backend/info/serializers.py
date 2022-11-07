from rest_framework.serializers import (
    ModelSerializer, CharField,
)
from .models import (
    Information, Photo
)
from profile.serializers import TranslationContentMixin, TranslationSubjectMixin

class InformationSerializer(
    TranslationContentMixin,
    TranslationSubjectMixin,
    ModelSerializer,
):
    type = CharField(source="get_type_display")

    class Meta:
        model = Information
        fields = '__all__'

class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ['picture', 'thumbnail', 'id']
