from rest_framework.serializers import (
    ModelSerializer, CharField, SerializerMethodField
)
from .models import (
    Information, Photo
)
from shared.models import get_translated_content
from profile.models import UserProfile
from profile.serializers import TranslationContentMixin

class InformationSerializer(TranslationContentMixin, ModelSerializer):

    def translated_subject(self, obj):
        profile = UserProfile.objects.get(user__id=self.context.get('user_id'))
        return get_translated_content(obj.subject, profile.language)

    type = CharField(source="get_type_display")
    subject = SerializerMethodField("translated_subject")

    class Meta:
        model = Information
        fields = '__all__'

class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ['picture']
