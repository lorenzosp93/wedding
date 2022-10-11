from rest_framework.serializers import (
    ModelSerializer, CharField, SerializerMethodField
)
from shared.serializers import (
    AddressSerializer,
    UserSerializer,
)
from .models import (
    UserProfile
)
from shared.models import get_translated_content

def translated_string(self, obj, field):
    profile = UserProfile.objects.get(user__id=self.context.get('user_id'))
    return get_translated_content(getattr(obj, field), profile.language)

class TranslationContentMixin(ModelSerializer):
    def translated_content(self, obj):
        return translated_string(self, obj, 'content')

    content = SerializerMethodField('translated_content')

class TranslationSubjectMixin(ModelSerializer):
    def translated_subject(self, obj):
        return translated_string(self, obj, 'subject')

    subject = SerializerMethodField('translated_subject')

class UserProfileAddressSerializer(ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = UserProfile
        fields = ['address']

class BaseUserProfileSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = ['user']

class UserProfileSerializer(BaseUserProfileSerializer):
    language = CharField(source='get_language_display')
    type = CharField(source='get_type_display')
    parent = UserSerializer(required=False,)
    childs = BaseUserProfileSerializer(
        source='user.childs',
        many=True,
        required=False,
    )

    class Meta:
        model = UserProfile
        depth = 1
        fields = '__all__'
