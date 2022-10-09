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

class UserProfileSerializer(ModelSerializer):
    user = UserSerializer()
    childs = UserSerializer(many=True, required=False,) # review to enable nested objects serializers
    class Meta:
        model = UserProfile
        depth = 1
        fields = '__all__'