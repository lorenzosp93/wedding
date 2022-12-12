from rest_framework.serializers import (
    ModelSerializer
)
from django.contrib.auth import get_user_model
from .models import (
    SiteSetting,
    Attachment,
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

class AttachmentSerializer(ModelSerializer):
    class Meta:
        model = Attachment
        fields = [
            'uuid',
            'file'
        ]

class SettingsSerializer(ModelSerializer):
    class Meta:
        model = SiteSetting
        fields = [
            'about_text'
        ]
