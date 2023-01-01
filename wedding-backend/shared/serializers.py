from typing import Protocol
from django.db.models import ForeignKey
from django.http import HttpRequest
from rest_framework.serializers import (
    ModelSerializer, PrimaryKeyRelatedField
)
from django.contrib.auth import get_user_model
from .models import (
    Address,
)


class HasUser(Protocol):
    user: ForeignKey


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        ]


class HasUserSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True)

    def save(self, **kwargs) -> HasUser:
        """Include default for read_only `user` field"""
        request: HttpRequest | None = self.context.get('request')
        if request:
            kwargs["user"] = request.user
        return super().save(**kwargs)


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
