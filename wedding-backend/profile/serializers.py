from typing import Optional
from rest_framework.serializers import (
    ModelSerializer, CharField, SerializerMethodField,
    Serializer, EmailField,
)
from shared.serializers import (
    AddressSerializer,
    UserSerializer,
)
from .models import (
    Keys,
    Subscription,
    UserProfile
)
from shared.models import get_translated_content


def translated_string(serializer, obj, field: str) -> Optional[str]:
    profile = UserProfile.objects.get(
        user__id=serializer.context.get('request').user.id)
    content = getattr(obj, field)
    if content:
        return get_translated_content(content, profile.language)
    return None


class TranslationContentMixin(ModelSerializer):
    def translated_content(self, obj) -> Optional[str]:
        return translated_string(self, obj, 'content')

    content = SerializerMethodField('translated_content')


class TranslationSubjectMixin(ModelSerializer):
    def translated_subject(self, obj) -> Optional[str]:
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


class PlusOneSerializer(Serializer):
    email = EmailField()
    first_name = CharField()
    last_name = CharField()


class KeysSerializer(ModelSerializer):
    class Meta:
        model = Keys
        fields = '__all__'


class SubscriptionSerializer(ModelSerializer):
    keys = KeysSerializer()

    class Meta:
        model = Subscription
        fields = ['endpoint', 'keys']

    def create(self, validated_data):
        keys_data = validated_data.pop('keys')
        user = self.context.get('request').user
        keys = Keys.objects.create(**keys_data)
        subscription = Subscription.objects.create(
            user=user, keys=keys, **validated_data)
        return subscription
