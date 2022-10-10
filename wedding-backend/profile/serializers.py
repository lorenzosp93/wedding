from rest_framework.serializers import (
    ModelSerializer, CharField,
)
from shared.serializers import (
    AddressSerializer,
    UserSerializer
)
from .models import (
    UserProfile
)


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
