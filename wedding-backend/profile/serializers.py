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


class UserProfileRWSerializer(ModelSerializer):
    address = AddressSerializer()
    user = UserSerializer()
    setup_plus_one = CharField()
    class Meta:
        model = UserProfile
        fields = ['address', 'setup_plus_one', 'user']


class UserProfileReadSerializer(ModelSerializer):
    user = UserSerializer()
    childs = UserSerializer(many=True) # review to enable nested objects serializers
    class Meta:
        model = UserProfile
        fields = '__all__'