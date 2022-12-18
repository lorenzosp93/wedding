from django.http import HttpRequest
from django.db.models import Model
from rest_framework.serializers import (
    ModelSerializer, CharField, SerializerMethodField,
    Serializer, EmailField, BaseSerializer
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


def translated_string(serializer: BaseSerializer, obj: Model, field: str) -> str | None:
    request: HttpRequest | None = serializer.context.get('request')
    if request:
        profile = UserProfile.objects.get(
            user__pk=request.user.pk)
        content = getattr(obj, field)
        if content:
            return get_translated_content(content, profile.language)
    return None


class TranslationContentMixin(ModelSerializer):
    def translated_content(self, obj: Model) -> str | None:
        return translated_string(self, obj, 'content')

    content = SerializerMethodField('translated_content')


class TranslationSubjectMixin(ModelSerializer):
    def translated_subject(self, obj: Model) -> str | None:
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

    def create(self, validated_data: dict) -> Subscription | None:
        keys_data = validated_data.pop('keys')
        request: HttpRequest | None = self.context.get('request')
        if request:
            user = request.user
            keys = Keys.objects.create(**keys_data)
            subscription = Subscription.objects.create(
                user=user, keys=keys, **validated_data)
            return subscription
        return None
