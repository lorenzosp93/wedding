from django.utils.translation import gettext_lazy as _
from django.forms import ValidationError
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.http import HttpRequest
from django.db.models import Model
from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    ModelSerializer, CharField, SerializerMethodField,
    Serializer, EmailField, BaseSerializer
)
from shared.serializers import (
    UserSerializer,
)
from .models import (
    Keys,
    Subscription,
    UserProfile
)
from shared.models import get_translated_content


def translated_string(
    serializer: BaseSerializer, obj: Model, field: str
) -> str | None:
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
            user_agent: str = self.get_user_agent(request)
            user = request.user
            keys = Keys.objects.create(**keys_data)
            subscription = Subscription.objects.create(
                user=user,
                user_agent=user_agent,
                keys=keys,
                **validated_data,
            )
            return subscription
        return None

    @staticmethod
    def get_user_agent(request: HttpRequest) -> str:
        return request.META.get('HTTP_USER_AGENT', '')


class RegisterUserSerializer(ModelSerializer):
    user: AbstractBaseUser | None = None

    def validate(self, attrs: dict[str, str]) -> dict[str, str]:
        try:
            self.user = self.Meta.model.objects.get(
                first_name__iexact=attrs.get('first_name', '').strip(),
                last_name__iexact=attrs.get('last_name', '').strip(),
            )
        except Exception:
            raise ValidationError({
                "non_field_errors": _(
                    """First and Last Name not found in invitee list,
                    did you write it correcly?"""
                )
            })
        if (
            isinstance(self.user, AbstractUser)
            and self.user.email != ''
            and self.user.email != attrs.get('email', '')
        ):
            raise ValidationError({
                "email": _(
                    """A user was already set up for this invitee with a different email"""
                )
            })
        return super().validate(attrs)

    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'email'
        ]
        extra_kwargs = {'email': {'required': True, 'allow_blank': False}}
