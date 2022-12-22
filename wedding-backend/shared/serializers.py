from rest_framework.serializers import (
    ModelSerializer
)
from django.contrib.auth import get_user_model
from .models import (
    Address,
)


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
