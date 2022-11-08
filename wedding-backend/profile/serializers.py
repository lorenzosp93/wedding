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

def translated_string(serializer, obj, field):
    profile = UserProfile.objects.get(user__id=serializer.context.get('request').user.id)
    content = getattr(obj,field)
    if content:
        return get_translated_content(content, profile.language)
    return None

class TranslationContentMixin(ModelSerializer):
    def translated_content(self, obj):
        return translated_string(self, obj, 'content')

    content = SerializerMethodField('translated_content')

class TranslationSubjectMixin(ModelSerializer):
    def translated_subject(self, obj):
        return translated_string(self, obj, 'subject')

    subject = SerializerMethodField('translated_subject')

class UserProfileWriteSerializer(ModelSerializer):
    address = AddressSerializer(required=False)
    class Meta:
        model = UserProfile
        fields = ['address', 'language']

class BaseUserProfileSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = ['user']

class UserProfileSerializer(BaseUserProfileSerializer):
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
